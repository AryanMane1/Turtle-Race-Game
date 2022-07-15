import turtle,time,random,os

# Globle
PenSize = 2
colors = ['red','blue','yellow','orange','green','brown']
Players_colors = ['red','blue','yellow','orange','green','brown','maroon','purple','aqua','lime','tomato']
speed = 5
is_win = False


winner = None
break_loop = False
text = turtle.Turtle()
text.hideturtle()
turtle1 = None
turtle2 = None
turtle3 = None
turtle4 = None
turtle5 = None
turtle6 = None
turtle7 = None
turtle8 = None
turtle9 = None
turtle10 = None
turtle11 = None
lis = [turtle1,turtle2,turtle3,turtle4,turtle5,turtle6,turtle7,turtle8,turtle9,turtle10,turtle11]
wel = turtle.Turtle()
wel.hideturtle()
wel.color('green','gray')
wel.width(7)
wel.speed(5)

def welcome():
    wel.write(f"** Click Space to Start Tutle Game **", font=("Verdana",23, "bold"),align='center')
    wel.setpos((350,0))
    wel.setpos((350,300))
    wel.setpos((-350,300))
    wel.setpos((-350,-300))
    wel.setpos((350,-300))
    wel.setpos((350,0))
    wel.end_fill()
    turtle.listen()
    turtle.onkey(initialize,'space')
    input("....")


class Player(turtle.Turtle):
    def __init__(self,x,y,name):
        self.x = x
        self.y = y
        self.name = name
        super().__init__()
        rand_color = random.choice(Players_colors)
        Players_colors.remove(rand_color)
        self.color('black',rand_color)
        self.pensize(PenSize)
        self.shape('turtle')
        self.penup()
        self.speed(7)
        self.turtlesize(2)
        self.setpos((x,y))
        self.left(90)
        # self.pendown()
        self.speed(speed)
    
    def run(self):
        global winner,is_win
        rand_forward = random.randint(1,random.randint(50,200))
        self.y+=rand_forward
        self.setpos((self.x,self.y))
        if(self.y>=250):
            is_win = True
            winner = self
            

    def spin(self):
        global break_loop
        # self.turtlesize(3)
        # self.setpos((300,-280))
        # self.speed(7)
        # self.forward(560)
        # self.left(90)
        # self.forward(620)
        # self.left(90)
        # self.forward(560)
        # self.left(90)
        # self.forward(620)
        # self.left(90)
        restart()
        


def draw_finish_line():
    finish_line = turtle.Turtle()
    finish_line.hideturtle()
    finish_line.shape('arrow')
    finish_line.speed(7)
    finish_line.width(3)
    finish_line.penup()
    finish_line.setpos((-290,250))
    finish_line.showturtle()
    finish_line.pendown()
    finish_line.speed(2)
    finish_line.setpos((290,250))
    finish_line.hideturtle()



def restart():
    global lis,Players_colors,speed,is_win,winner,break_loop,text,turtle1,turtle2,turtle3,turtle4,turtle5,turtle6,turtle7,turtle8,turtle9,turtle10,turtle11
    text.clear()
    text = turtle.Turtle()
    text.hideturtle()
    Players_colors = ['red','blue','yellow','orange','green','brown','maroon','purple','aqua','lime','tomato']
    speed = 5
    is_win = False
    winner = None
    break_loop = False
    turtle1.x = -250
    turtle2.x = -200
    turtle3.x = -150
    turtle4.x = -100
    turtle5.x = -50
    turtle6.x = 0
    turtle7.x = 50
    turtle8.x = 100
    turtle9.x = 150
    turtle10.x = 200
    turtle11.x = 250
    for player in lis:
        player.y = -250
        player.speed(10)
        player.turtlesize(2)
        player.setpos((player.x,player.y))
        player.setheading(90)
    
    main()

def initialize():
    global turtle1,turtle2,turtle3,turtle4,turtle5,turtle6,turtle7,turtle8,turtle9,turtle10,turtle11,wel,winner,is_win,lis
    wel.clear()
    draw_finish_line()
    turtle1 = Player(-250,-250,'Newton')
    turtle2 = Player(-200,-250,'Aryan')
    turtle3 = Player(-150,-250,'Dolly')
    turtle4 = Player(-100,-250,'John')
    turtle5 = Player(-50,-250,'Roman')
    turtle6 = Player(0,-250,'Elon')
    turtle7 = Player(50,-250,'Bill')
    turtle8 = Player(100,-250,'Ajay')
    turtle9 = Player(150,-250,'Mark')
    turtle10 = Player(200,-250,'Undertaker')
    turtle11 = Player(250,-250,'Brock')
    lis = [turtle1,turtle2,turtle3,turtle4,turtle5,turtle6,turtle7,turtle8,turtle9,turtle10,turtle11]
    main()

def main():
    global turtle1,turtle2,turtle3,turtle4,turtle5,turtle6,turtle7,turtle8,turtle9,turtle10,turtle11,wel,winner,is_win
    
    while not is_win:
        lis = [turtle1,turtle2,turtle3,turtle4,turtle5,turtle6,turtle7,turtle8,turtle9,turtle10,turtle11]
        for i in range(11):
            player = random.choice(lis)
            player.run()
            lis.remove(player)

    text.speed(1)
    text.write(f"Winner is {winner.name}", font=("Verdana",25, "bold"),move=True,align='center')

    if os.path.exists("data.txt") == False:
        with open("data.txt",'w') as f:
            f.write('''Newton = 0 \nAryan = 0 \nDolly = 0 \nJohn = 0 \nRoman = 0 \nElon = 0 \nBill = 0 \nAjay = 0 \nMark = 0 \nUndertaker = 0 \nBrock = 0''')
    before_points = {"Newton":0 ,"Aryan":0, "Dolly":0,"John":0,"Roman":0,"Elon":0,"Bill":0 ,"Ajay":0, "Mark":0,"Undertaker":0,"Brock":0}
    
    with open("data.txt",'r') as f:
        lis = f.readlines()
        for line in lis:
            if line!="" and line!="\n" and ">" not in line:
                l = line.split("=")
                p_name = l[0].replace(" ","")
                p_points = l[1].replace("\n","").replace(" ","")
                print(p_name,p_points)
                if p_name == winner.name:
                    before_points[p_name] = int(p_points)+1
                else:
                    before_points[p_name] = int(p_points)

    name_lis = []
    points_lis = []

    for name in before_points.keys():
        name_lis.append(name)
        points_lis.append(before_points[name])

    for i in range(len(points_lis)):
        for j in range(len(points_lis)):
            if(points_lis[i]>points_lis[j]):
                points_lis[i],points_lis[j] = points_lis[j],points_lis[i]
                name_lis[i],name_lis[j] = name_lis[j],name_lis[i]


    with open("data.txt",'w') as f:
        for name,points in zip(name_lis,points_lis):
            f.write(f"{name} = {points} \n")
        f.write(f"\nWinner Of last Match => {winner.name}")

    
    
    winner.spin()


welcome()