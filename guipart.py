from tkinter import *
from sudoku import solver
rootOld=Tk()
rootOld.geometry("250x200")
def sudokuRules():
        print('''•	Rule 1: Know the Game First
•	Rule 2: Use digits from 1 – 9
•	Rule 3: Avoid repetition of figures
•	Rule 4: Avoid guesswork
•	Rule 5: Use the elimination method

''')
    
def newWin():
    
    root = Tk()
     
    root.title("Sudoku Solver")
    root.geometry("549x490")

    label = Label(root, text="Fill the numbers and click solve to the Sudoku",fg="white", bg="green").grid(
        row=0, column=1, columnspan=10)

    errLabel = Label(root, text="")

    errLabel.grid(row=15, column=1, columnspan=10, pady=5)

    solvedLabel = Label(root, text="")
    solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)
    cells = {}


    def ValidateNumber(P):
        out = (P.isdigit() or P == "") and len(P) < 2 
        return out


    reg = root.register(ValidateNumber)


    def draw3x3Grid(row, column, bgcolor):
        for i in range(1):
            for j in range(1):
                e = Entry(root, width=5, bg=bgcolor, justify="center",
                        validate="key", validatecommand=(reg, "%P"),fg="orange",font="bold")
                e.grid(row=row+i+1, column=column+j+1,
                    sticky="nsew", padx=1, pady=1, ipady=5)
                cells[(row+i+1, column+j+1)] = e


    def draw9x9Grid():
        color = "black"
        for rowNo in range(1, 10, 1):
            for colNo in range(0, 9, 1):
                draw3x3Grid(rowNo, colNo, color)
                if color == "black":
                    color = "white"
                else:
                    color = "black"


    def clearValues():
        errLabel.configure(text="")
        solvedLabel.configure(text="")
        for row in range(2, 11):
            for col in range(1, 10):
                cell = cells[(row, col)]
                cell.delete(0, "end")


    def getValues():
        board = []
        errLabel.configure(text="")
        solvedLabel.configure(text="")
        for row in range(2, 11):
            rows = []
            for col in range(1, 10):
                val = cells[(row, col)].get()
                if val == "":
                    rows.append(0)
                else:
                    rows.append(int(val))
            board.append(rows)
        updateValues(board)


    btn = Button(root, command=getValues, text="Solve", width=10,bg="purple" ,foreground="yellow",font="bold")
    btn.grid(row=20, column=1, columnspan=5, pady=20)

    btn = Button(root, command=clearValues, text="Clear", width=10,bg="purple",foreground="yellow",font="bold")
    btn.grid(row=20, column=3, columnspan=5, pady=20)

    btn = Button(root, text="Close", width=10,bg="purple",foreground="yellow",font="bold")
    btn.grid(row=20, column=5, columnspan=5, pady=20)
    btn.bind('<Double-1>' , quit)


    def updateValues(s):
        sol=solver(s)
        if(sol !="no"):
            for rows in range(2,11):
                for col in range(1,10):
                    cells[(rows,col)].delete(0,"end")
                    cells[(rows,col)].insert(0,sol[rows-2][col-1])
            solvedLabel.configure(text="Suduko solved",font="bold" , fg="red" , bg="black")
        else:
            errLabel.configure(text="No solution exists for this suduko")
            
    draw9x9Grid()
    # rootOld.destroy()

rootOld.title('Sudoku!')   
canvas=Canvas(rootOld,width=549,height=490)
canvas.pack()
path='pic1.png'
bg=PhotoImage(file=path)
canvas.create_image(0,0,image=bg)
button=Button(rootOld,text='Click',command=newWin,font=('sans serif',14),bg='lime')
buttonWin=canvas.create_window(70,100,anchor=NW,window=button)
button2=Button(rootOld,text='Rules',command=sudokuRules,font=('sans serif',14),bg='lime')
buttonWin=canvas.create_window(130,100,anchor=NW,window=button2)
rootOld.mainloop()


Button(rootOld,text='Click',command=newWin).pack()
Button(rootOld,text='Rules',command=sudokuRules).pack()
rootOld.mainloop()