import tkinter as tk
from tkinter import ttk,messagebox

places = [["","",""],
          ["","",""],
          ["","",""]]

def is_end():
    # Check rows for a win
    for place in places:
        mark = place[0]
        count = 0
        if mark != "":
            for sheet in place:
                if sheet == mark:
                    count += 1
                else:
                    break
        if count == 3:
            return True, mark
    
    # Check columns for a win
    for col in range(3):
        mark = places[0][col]
        count = 0
        if mark != "":
            for row in range(3):
                sheet = places[row][col]
                if sheet == mark:
                    count += 1
                else:
                    break
        if count == 3:
            return True, mark
    
    # Check diagonals for a win
    if (places[0][0] != "") and (places[0][0] == places[1][1]) and (places[0][0] == places[2][2]):
        return True, places[0][0]
    if (places[0][2] != "") and (places[0][2] == places[1][1]) and (places[0][2] == places[2][0]):
        return True, places[0][2]
    
    # Check for a draw
    for col in range(3):
        for row in range(3):
            sheet = places[row][col]
            if sheet == "":
                return False, None
    
    # If no empty cells and no win, it's a draw
    return True, "DRAW"

            

class game(tk.Tk):
    bgExt = "#172026"
    bgMid = "#027373"
    bgInt = "#04BFAD"
    bgbtn = "#F2E3D5"
    fg = "#FFFFFF"
    mark = "X"
    
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("Tic Tac Toe")
        self.resizable(0,0)
        self.config(bg=self.bgExt)
        self.components()
        self.buttons = []  # List to store button references
        self.create_buttons()
            
    def components(self):
        container = tk.Frame(self,
                          width=300,
                          height=300,
                          bg=self.bgMid,
                          highlightthickness=2,
                          highlightbackground=self.fg,
                          highlightcolor=self.fg)
        container.pack(fill="both",padx=10,pady=10)
        container.pack_propagate(False)
        
        title = tk.Label(container,
                         text="Tic Tac Toe",
                         bg=self.bgMid,
                         font=("arial",16),
                         fg=self.fg)
        title.pack(side="top",fill="x",padx=10,pady=10)
        
        self.table = tk.Frame(container,
                        width=260,
                        height=200,
                        bg=self.bgMid,
                        highlightthickness=2,
                        highlightbackground=self.fg,
                        highlightcolor=self.fg)
        self.table.pack(ipadx=2,ipady=2)
        self.table.grid_propagate(False)
        self.table.grid_columnconfigure(0,weight=3)
        self.table.grid_columnconfigure(1,weight=3)
        self.table.grid_columnconfigure(2,weight=3)
        self.table.grid_rowconfigure(0,weight=3)
        self.table.grid_rowconfigure(1,weight=3)
        self.table.grid_rowconfigure(2,weight=3)

    def create_buttons(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.table, command=lambda p=[i, j]: self.place(p),fg=self.fg,bg=self.bgbtn,font=("arial",10,"bold"))
                button.grid(row=i, column=j, sticky="NSEW", padx=1, pady=1)
                row.append(button)  # Add the button to the current row
            self.buttons.append(row)  # Add the row to the buttons list
        clean_button = tk.Button(self.table,text="Clean",command= self.clean,fg=self.bgMid,bg=self.bgbtn,font=("arial",10,"bold"))
        clean_button.grid(row=3, column=1, sticky="NSEW", padx=1, pady=1)
        self.x_turn = tk.Button(self.table,text="  X  ",command= self.turn,fg=self.bgMid,bg="#DFDFE9",font=("arial",10,"bold"),state="disabled")
        self.x_turn.grid(row=3, column=0, sticky="NSEW", padx=1, pady=1)
        self.o_turn = tk.Button(self.table,text="  O  ",command= self.turn,fg=self.bgMid,bg="#DFDFE9",font=("arial",10,"bold"),state="disabled")
        self.o_turn.grid(row=3, column=2, sticky="NSEW", padx=1, pady=1)
    
    def clean(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="",state ="normal")
                places[row][col] = ""
    
    def turn(self,mark):
        if mark == "O":
            self.x_turn.config(bg="#DFDFE9")
            self.o_turn.config(bg="#ACEAC7")
        else :
            self.o_turn.config(bg="#DFDFE9")
            self.x_turn.config(bg="#ACEAC7")

    def place(self, place):
        row, col = place
        self.buttons[row][col].config(text=self.mark,state ="disabled")  # Example action: set text to "X"
        # You can add more logic here to handle the game's state
        places[row][col] = self.mark
        self.turn(self.mark)
        if self.mark == "X":
            self.mark = "O"
            
        else:
            self.mark = "X" 
        self.turn(self.mark)
        
        is_ended,mark = is_end()
        if is_ended:
            if mark != "DRAW":
                messagebox.showinfo("The End","The Winner is "+ mark)
            else:
                messagebox.showinfo("The End","There is a DRAW")
             
        
if __name__== "__main__":
    game = game()
    game.mainloop()
    print(places)