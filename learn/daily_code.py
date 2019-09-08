#WELCOME TO MICHELIA'S DAILY CODE
#SCREEN PET ISON LINE 28

#print('Hi, what is your name !')

#name_string = input()

#print('{0}, what is your age?'.format(name_string))
#age_string = input()

#print('you are {0} '.format (age_string))


#age = int(age_string)

#year = 2019
#birth_date =(year-age)
#if age <= 2 or age > 110 :
   # print('Ha ha!Good joke!!!')
    #print('I am smarter than you think')
#print(' you were born in {0}'.format(birth_date))

#if age == 9 :
 #   print('Hey! You are the same age as me!!')



 #Screen pet !!!

from tkinter import HIDDEN, NORMAL, Tk ,Canvas


def toggle_eyes ():
    current_color = c.itemcget(eye_left,'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c. itemcget (l_pupil,'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(l_pupil , state = new_state)
    c.itemconfigure(r_pupil, state = new_state)
    c.itemconfigure(eye_left, fill = new_color)
    c.itemconfigure(eye_right, fill = new_color)

def blink ():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(5000,blink)


def toggle_pupils () :
    if not c.eyes_crossed :
        c.move(r_pupil,10,-5)
        c.move(r_pupil,-10,-5)
        c.eyes_crossed = True
    else:
        c.move(l_pupil,-10,5)
        c.move(r_pupil,-10,-5)
        c.eyes_crossed = False








def toggle_tongue ():
    if not c.tongue_out :
        c.itemconfigure(tongue_tip, state = NORMAL)
        c.itemconfigure(tongue_main, state = NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue_tip, state = HIDDEN)
        c.itemconfigure(tongue_main,state = HIDDEN)
        c.tongue_out = False


def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    root.after(1000,toggle_tongue)
    root.after(1000,toggle_pupils)
    return



def show_happy (event) :
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheek_left, state= NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(happy_mouth,state = NORMAL)
        c.itemconfigure(norm_mouth,state = HIDDEN)
        c.itemconfigure(sad_mouth,state = HIDDEN)
    return

def hide_happy (event) :
        c.itemconfigure(cheek_left, state= HIDDEN)
        c.itemconfigure(cheek_right, state=HIDDEN)
        c.itemconfigure(happy_mouth,state = HIDDEN)
        c.itemconfigure(norm_mouth,state = NORMAL)
        c.itemconfigure(sad_mouth,state = HIDDEN)
        return










root = Tk()
c = Canvas(root,width = 400,height = 400)
c.configure(bg = 'black', highlightthickness = 0)
c.body_color = 'dark gray'
body = c.create_oval(10,2,320,300,outline = c.body_color, fill  = c.body_color)

ear_left = c.create_polygon(65,70,75,10,150,45,outline = c.body_color,fill = c.body_color)
ear_right = c.create_polygon(240,35,315,5,310,75,outline = c.body_color,fill = c.body_color)

eye_left = c.create_oval(130,110,160,170,outline = 'white',fill = 'white')
l_pupil = c.create_oval(140,145,150 ,155, outline= 'black' , fill ='black')
eye_right = c.create_oval(230,110,260,170,outline = 'white',fill = 'white')
r_pupil = c.create_oval(240,145,250 ,155, outline= 'black' , fill ='black')

norm_mouth = c.create_line (170,230,200,252,230,250,smooth = 1, width = 2,state = NORMAL)
happy_mouth = c. create_line (170 ,230,200,272,230,230,smooth = 1, width = 2,state = HIDDEN)
sad_mouth = c. create_line (170 ,230,200,202,230,230,smooth = 1, width = 2,state = HIDDEN)
tongue_main = c.create_rectangle(170,240,230,280,outline = 'pink', fill ='pink', state = HIDDEN)
tongue_tip = c.create_oval(170,275,230,290,outline = 'pink', fill = 'pink', state = HIDDEN)

cheek_left = c. create_oval(70,180,120,230,outline = 'light pink',fill ='light pink', state = HIDDEN)
cheek_right = c. create_oval(280,180,330,230,outline = 'light pink',fill ='light pink', state = HIDDEN)


c.pack()


c.bind('<Motion>' , show_happy)
c.bind('<Leave>' , hide_happy)
c.bind ('<Double-1>,cheeky')



c. eyes_crossed = False
c.tongue_out = False

root.after(1000,blink)
root.mainloop()
