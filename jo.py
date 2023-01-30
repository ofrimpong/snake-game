
from time import sleep
from tkinter import *
import random

def reset():
    global snake
    global food
    snake = Snake()
    food = Food()
GAME_WIDHT = 1000
GAME_HIEGHT = 700  
BODY = 1
SPEED = 50
SPACE_SIZE = 20
SNAKE_COLOR = "orange"
FOOD_COLOR = "red"
BG = "purple"

def get_items(x,y):
    if x == food.cordinates[0] and y == food.cordinates[1]:
        return True
def check_coloshin(snake):
    x,y = snake.cordinates[0]
    vo= snake.cordinates[1:]
    if x < 0 or x >= GAME_WIDHT:
        
        return True

    if y < 0 or y >= GAME_HIEGHT:
        restart_button.pack()
        return True

    return False
def game_over():
    d.delete("snake")
    sleep(1)
window = Tk()

laet = Label(window,font=("Ink Free",10))
laet.pack()
direction = "down"
score = 0
restart_button = Button(window, command=reset,text="restart button",fg="#FF0000")
window_widht = window.winfo_width()
window_height = window.winfo_height()
screen_widht = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int(screen_widht/2-(screen_widht/2))
y = int(screen_height/2-(screen_height/2))
l = Label(window,font=("Ink Free", 25))
l.config(text="score:{}".format(score))
l.pack()
d = Canvas(window, bg = BG, height=GAME_HIEGHT,width=GAME_WIDHT)
restart_button.pack()
window.update()
window.geometry("1000x1000")
d.pack()
def addtaging():
            ycore =  random.randint(1,7)
            xcore = random.randint(1,7)
            d.create_text(x/3,y/3,text="xcore:{} ycore:{}".format(xcore,ycore),fill="red",font=("Ink Free", 30))
class Snake:
    def __init__(self):
        self.body_size=BODY
        self.cordinates = []
        self.squares=[]
        for i in range(0,BODY):
            self.cordinates.append([0,0])
        for x,y in self.cordinates:
            s = d.create_oval(x,y,0,0,fill=SNAKE_COLOR,tags="snake")
            self.squares.append(s)
class Food:
    def __init__(self):
        x= random.randint(0, (GAME_WIDHT/SPACE_SIZE)-1)*SPACE_SIZE
        y= random.randint(0, (GAME_HIEGHT/SPACE_SIZE)-1)*SPACE_SIZE
        d.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tags="food")
        self.cordinates = [x,y]

snake = Snake()
food = Food()
direction = "right"
def next_turn(snakd,aplly):
    global food
    global snake
    global BODY
    global score
    global SPEED
    global SPACE_SIZE
    def down(f):
        global direction  
        if direction != "up":
            direction = "down"
    def up(f):
        global direction  
        if direction != "down":
            direction = "up"
    def left(f):
        global direction
        if direction != "right":  
            direction = "left"
    def right(f):
        global direction 
        if direction != "left": 
            direction = "right"
    def stop(f):
        global direction  
        direction = "stop"
    global direction
    global y
    global x
    if direction == "up":
        y -= SPACE_SIZE
    if direction == "down":
        y += SPACE_SIZE
    if direction == "left":
        x -= SPACE_SIZE
    if direction == "right":
        x += SPACE_SIZE
    if direction == "stop":
        sleep(1)
    snake.cordinates.insert(0,(x,y))
    n = d.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
    snake.squares.insert(0,n)
    del snake.cordinates[-1]
    d.delete(snake.squares[-1])
    del snake.squares[-1]
    if get_items(x,y):
        for i in range(BODY):
            del snake.cordinates[-1]
            d.delete(snake.squares[-1])
            del snake.squares[-1]
        d.delete("food")
        score += 1
        BODY += 1
        snake= Snake()
        l.config(text="score:{}".format(score))
        snake.__init__()
        food = Food()

    window.after(SPEED, next_turn,snakd,aplly)
    window.bind("<Down>", down)
    window.bind("<Up>", up)
    window.bind("<Left>", left)
    window.bind("<Right>", right)
    window.bind("<Return>", stop)   
    if check_coloshin(snake):
        stop(1)
        game_over()

next_turn(1,1)

window.mainloop()
