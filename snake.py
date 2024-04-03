from tkinter import *
import random

score = 0
direction = 'down'


class Attribute:
    def __init__(self):
        global score, direction
        self.game_width = 1000
        self.game_height = 600
        self.speed = 100
        self.space_size = 50
        self.body = 3
        self.snake_color = 'Blue'
        self.foodcolor = 'yellow'
        self.bg_color = 'black'

        self.root = Tk()
        self.root.title('Snake Game')
        self.root.resizable(False, False)

        self.lblscr = Label(self.root, text=f'Score: {score}', font=('Terminal', 30))
        self.lblscr.pack()

        self.cnvs = Canvas(self.root, bg=self.bg_color, height=self.game_height, width=self.game_width)
        self.cnvs.pack()

        self.rstbtn = Button(text='Reset', command=self.reset)
        self.rstbtn.pack()

        self.set_Snake()
        self.set_Food()

        self.root.bind('<Left>', self.change_Dir_left)
        self.root.bind('<Right>', self.change_Dir_right)
        self.root.bind('<Up>', self.change_Dir_up)
        self.root.bind('<Down>', self.change_Dir_down)

        self.next_Turn()
        self.root.mainloop()

    def set_Snake(self):
        self.body_size = self.body
        self.coordinates = []
        self.squares = []

        for i in range(0, self.body):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = self.cnvs.create_rectangle(x, y, x + self.space_size, y + self.space_size, fill=self.snake_color,
                                                tag='snake')
            self.squares.append(square)

    def set_Food(self):
        x = random.randint(0, (self.game_width // self.space_size) - 1) * self.space_size
        y = random.randint(0, (self.game_height // self.space_size) - 1) * self.space_size
        self.food_coordinates = [x, y]
        self.cnvs.create_oval(x, y, x + self.space_size, y + self.space_size, fill=self.foodcolor, tag='food')

    def next_Turn(self):
        x, y = self.coordinates[0]
        if direction == 'up':
            y -= self.space_size
        elif direction == 'down':
            y += self.space_size
        elif direction == 'left':
            x -= self.space_size
        elif direction == 'right':
            x += self.space_size

        self.coordinates.insert(0, (x, y))

        square = self.cnvs.create_rectangle(x, y, x + self.space_size, y + self.space_size, fill=self.snake_color)

        self.squares.insert(0, square)

        if x == self.food_coordinates[0] and y == self.food_coordinates[1]:
            global score
            score += 1
            self.lblscr['text'] = f'Score: {score}'
            self.cnvs.delete('food')
            self.set_Food()
        else:
            del self.coordinates[-1]
            self.cnvs.delete(self.squares[-1])
            del self.squares[-1]

        if self.check_Collision():
            self.game_Over()
        else:
            self.root.after(self.speed, self.next_Turn)

    def change_Dir_left(self, event):
        global direction
        if direction != 'right':
            direction = 'left'

    def change_Dir_right(self, event):
        global direction
        if direction != 'left':
            direction = 'right'

    def change_Dir_up(self, event):
        global direction
        if direction != 'down':
            direction = 'up'

    def change_Dir_down(self, event):
        global direction
        if direction != 'up':
            direction = 'down'

    def check_Collision(self):
        x, y = self.coordinates[0]
        if x < 0 or x >= self.game_width:
            return True
        elif y < 0 or y >= self.game_height:
            return True

        for body in self.coordinates[1:]:
            if x == body[0] and y == body[1]:
                return True

        return False

    def game_Over(self):
        self.cnvs.delete(ALL)
        self.cnvs.create_text(self.cnvs.winfo_width() / 2, self.cnvs.winfo_height() / 2, font=('terminal', 20),
                              text='Game Over', fill='red', tag='over')

    def reset(self):
        global score, direction
        score = 0
        direction = 'down'
        self.lblscr.config(text=f'Score: {score}')
        self.cnvs.delete(ALL)
        self.set_Snake()
        self.set_Food()
        self.next_Turn()


a1 = Attribute()


"""from tkinter import *
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLORE = "#0000FF"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
class Snake :
    
    def __init__(self):
         self.boody_size = BODY_PARTS
         self.coordinates = []
         self.squares = []

         for i in range(0, BODY_PARTS):
              self.coordinates.append([0,0])
        
         for x, y in self.coordinates:
              square = canvas.create_rectangle(x,y,x+SPACE_SIZE, y+SPACE_SIZE,fill=SNAKE_COLORE,tag="snake")
              self.squares.append(square)

class Food :
    
    def __init__(self):
         
         x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
         y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

         self.coordonates =[x,y]

         canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE, fill = FOOD_COLOR, tag="food")
def next_turn(snake, food):
        
        x,y=snake.coordinstes[0]

        if direction == "up":
             y-=SPACE_SIZE
        elif direction == "down":
             y+=SPACE_SIZE
        elif direction == "left":
            x-=SPACE_SIZE

        elif direction == "right":
            x+=SPACE_SIZE

        snake.coordinates.insert(0.(x,y))

        square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLORE)
       
        snake.squares.insert(0, square)

        if x== food.coordinates[0] and y == food.coordinates[-1]:

            global score

            score += 1

            label.config(text="Score:{}".format(score))

            canvas.delete("food")

            food = Food()

        else:             
           del snake.coordinates[-1]

           canvas.delete(snake.squares[-1])
        
           del snake.squares[-1]
        
        if check_collisions(snake):
             game_over()
        else:
          window.after(SPEED,next_turn,snake,food)
        

def change_directoin(new_direction):
     
     global direction 

     if new_direction == 'left':
          if direction != 'reght':
                direction = new_direction
     elif new_direction == 'right':
          if direction != 'left':
               direction = new_direction
     elif new_direction != 'up':
          if direction != 'down':
               direction = new_direction
     elif new_direction != 'down':
          if direction != 'up':
               direction = new_direction
def check_collisions(snake):
     
     x,y = snake.coordinates[0]

     if x<0 or x>= GAME_WIDTH:
          return True
     elif y<0 or y>= GAME_HEIGHT:
          return True
     
     for body_part in snake.coordinates[1:]:
          if x == body_part[0] and y==body_part[1]:
               print("GAME OVER")
               return True
     return False

def game_over():
     canvas.delete(ALL)
     canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="GAME OVER", fill="red", tag="gameover")


window = Tk()

window.title("Snake game")

window.resizable(False,False)

score = 0

direction = 'down'

label = Label(window, text = "Score:{}".format(score),font=('consolas',40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()

window.update()

window_widht = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height =window.winfo_screenheight()

x = int((screen_width/2)-(window_widht/2))
y = int((screen_height/2)-(window_height/2))

window.geometry(f"{window_widht}x{window_height}+{x}+{y}")

window.bind('<left>',lambda event : change_directoin('left'))
window.bind('<right>', lambda event : change_directoin('right'))
window.bind('<Up>',lambda event : change_directoin('up'))
window.bind('<Down>',lambda event : change_directoin('down'))

snake = Snake()
food = Food()


next_turn(snake,food)
window.mainloop()"""
