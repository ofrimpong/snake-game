import random
from tkinter import *
def next_turn(r,c):
    global player
    if player == "x" and check_winner() is False:
        
        
        if player == players[0] :
            butons[r][c]['text'] = player            
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
            elif check_winner() is True:
                label.config(text="player 0 wins")
            elif check_winner() == "Tie":
                label.config(text="Tie")
    else:
        if player == players[1] :
            butons[r][c]['text'] = player
            
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[1]+" turn"))
            elif check_winner() is True:
                label.config(text="player 1 wins")
            elif check_winner() == "Tie":
                label.config(text="Tie")
def check_winner():
    for i in range(3):
            if butons[i][0]['text'] == butons[i][1]['text'] == butons[i][2]['text'] != "":
                butons[i][0].config(fg="red")
                butons[i][1].config(fg="red")
                butons[i][2].config(fg="red")
                return True
    for j in range(3):
            if butons[0][j]['text'] == butons[1][j]['text'] == butons[2][j]['text'] != "":
                butons[0][j].config(fg="red")
                butons[1][j].config(fg="red")
                butons[2][j].config(fg="red")
                return True
    if butons[0][0]['text'] == butons[1][1]['text'] == butons[2][2]['text'] != "":
                butons[0][0].config(fg="red")
                butons[1][1].config(fg="red")
                butons[2][2].config(fg="red")
                return True
    if butons[2][0]['text'] == butons[1][1]['text'] == butons[0][2]['text'] != "":
                butons[0][2].config(fg="red")
                butons[1][1].config(fg="red")
                butons[2][0].config(fg="red")
                return True

    if empty_spaces() is False:
        for i in range(3):
            for j in  range(3):
                butons[i][j].config(fg="red")
        return "Tie"
    return False
def empty_spaces():
    spaces = 9
    for i in range(3):
        for j in range(3):
            if butons[i][j]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

window = Tk()
window.title("Tic Tac Toe * widht + heaight")
players = ["x","o"]
player = random.choice(players)
player = players[0]
butons = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
label = Label(window, text=player+" turn",font=("Ink Free", 30))
label.pack()

frame = Frame(window,width=4,height=4)
frame.pack()
def new_game():
    global butons
    global frame
    for i in range(3):
        for j in  range(3):
            butons[i][j] = Button(frame,command=lambda row = i,colmi=j:next_turn(row,colmi),width=1,height=1)
            butons[i][j].grid(row=i,column=j)
new_game()
reset_butoon = Button(window, text="reset fonting icens",font=("Ink Free", 30),command=new_game)
reset_butoon.pack()
window.mainloop()