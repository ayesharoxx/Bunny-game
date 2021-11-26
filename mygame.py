import tkinter as tk
import time
import random
import os


root=tk.Tk()
WIDTH,HEIGHT=1280,720
def show_frame(frame):
    frame.tkraise()
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)


#Creating all frames
frame1=tk.Frame(root)
loading=tk.Frame(root)
main=tk.Frame(root)
lost=tk.Frame(root)
win=tk.Frame(root)
leader=tk.Frame(root)
playerentry=tk.Frame(root)
mypause=tk.Frame(root)
myboss=tk.Frame(root)
controlframe=tk.Frame(root)
for f in (frame1,loading,main,lost,win,leader,playerentry,mypause,myboss,controlframe):
    f.grid(row=0,column=0,sticky='nsew')


#importing all pictures
p1=tk.PhotoImage(file='newgame.gif')
p2=tk.PhotoImage(file='loadgamenew.gif')
p3=tk.PhotoImage(file='leaderboardnew1.gif')
p4=tk.PhotoImage(file='realquit.gif')
p5=tk.PhotoImage(file='controlbuttonnew.gif')
photo=tk.PhotoImage(file='bgnew.gif')
photo2=tk.PhotoImage(file='bggame.gif')

l1=tk.PhotoImage(file='load0.gif')
l2=tk.PhotoImage(file='load50.gif')
l3=tk.PhotoImage(file='load100.gif')

mainrabbit=tk.PhotoImage(file='rabbitmain.gif')
bg1=tk.PhotoImage(file='bggame.gif')
photo3=tk.PhotoImage(file='rabbitbig.gif')
l=tk.PhotoImage(file='leaf.gif')
ps=tk.PhotoImage(file='pausebutton.gif')
h1=tk.PhotoImage(file='heart.gif')
h2=tk.PhotoImage(file='heart.gif')
h3=tk.PhotoImage(file='heart.gif')
img=tk.PhotoImage(file='character.gif')
gameover=tk.PhotoImage(file='gameovr.gif')
youlost=tk.PhotoImage(file='youlose.gif')
nameentry=tk.PhotoImage(file='entername.gif')
nextimg=tk.PhotoImage(file='nextbutton.gif')
resume=tk.PhotoImage(file='resumebutton.gif')
excel=tk.PhotoImage(file='excelsheet.gif')
bunnyboo=tk.PhotoImage(file='bunnyboonew.gif')
ctrlimg=tk.PhotoImage(file='controlpage.gif')

#creating canvas
canvas=tk.Canvas(frame1,width=1280,height=720)
canvas.pack(fill='both',expand=True)
canvas1=tk.Canvas(loading,width=1280,height=720)
canvas1.pack(fill='both',expand=True)

canvas3 = tk.Canvas(main, width=WIDTH, height=HEIGHT)
canvas3.pack(fill='both',expand=True)

canvas5=tk.Canvas(lost,width=1280,height=720)
canvas5.pack(fill='both',expand=True)  
canvas6=tk.Canvas(win,width=1280,height=720)
canvas6.pack(fill='both',expand=True)
canvas7=tk.Canvas(leader,width=1280,height=720,bg='SteelBlue1')
canvas7.pack()
canvas8=tk.Canvas(playerentry,width=1280,height=720)
canvas8.pack(fill='both',expand=True)
canvas9=tk.Canvas(mypause,width=1280,height=720)
canvas9.pack(fill='both',expand=True)
canvas10=tk.Canvas(myboss,width=1280,height=720)
canvas10.pack(fill='both',expand=True)
canvas11=tk.Canvas(controlframe,width=1280,height=720)
canvas11.pack(fill='both',expand=True)

#creating images and text
canvas.create_image(0,0,image=photo,anchor='nw')
canvas.create_image(30,300,image=mainrabbit,anchor='nw')
canvas.create_image(100,20,image=bunnyboo,anchor='nw')
canvas3.create_image(0,0,image=bg1,anchor='nw')
ch=canvas3.create_image(10,375,image=photo3,anchor='nw')
imgl1=canvas3.create_image(600,20,image=h1,anchor='nw')
imgl2=canvas3.create_image(660,20,image=h1,anchor='nw')
imgl3=canvas3.create_image(720,20,image=h1,anchor='nw')
canvas5.create_image(0,0,image=gameover,anchor='nw')
canvas5.create_image(350,50,image=youlost,anchor='nw')
canvas6.create_image(0,0,image=gameover,anchor='nw')
canvas8.create_image(0,0,image=photo,anchor='nw')
canvas8.create_image(220,40,image=nameentry,anchor='nw')
canvas9.create_image(0,0,image=bg1,anchor='nw')
canvas10.create_image(0,0,image=excel,anchor='nw')
canvas10.create_text(100,700,text='Press <r> to return')
canvas11.create_image(0,0,image=ctrlimg,anchor='nw')


#def variables
leaf=[]
paused=False
#creating list of leaves
for i in range(7):
    start=random.randrange(150,1080,150)   #getting random start position of each leaf
    end=random.randrange(60,600,80)        #getting random end position for each leaf
    leaf.append(canvas3.create_image(start,end,image=l,anchor='nw'))
called=''
c=''
y=[2]*7
life=3
score=350
mylist=[]
d={}
v=tk.StringVar()

#def functions
def loadingFrame1():
    loadimg1=canvas1.create_image(0,0,image=l1,anchor='nw')  #create first load image
    root.after(500, loadingFrame2)                           #calling function after 0.5 seconds to display next load image
    show_frame(loading)                                                

def loadingFrame2():
    loadimg2=canvas1.create_image(0,0,image=l2,anchor='nw')  #creating next load image
    root.after(500,loadingFrame3)                            #calling function after 0.5 seconds to display next load image
    show_frame(loading)

def loadingFrame3():
    loadimg3=canvas1.create_image(0,0,image=l3,anchor='nw')  #creating last load image
    root.after(500,loadingentry)                             #calling next functiom after 0.5 seconds to get name entry
def loadingentry():
    show_frame(playerentry)
def getentry():
    global myname
    myname=v.get()
    show_frame(main)

#Defining game controls
def left(event):
    if not paused:
        x,y,p,q=canvas3.bbox(ch)
        if x<3:
            canvas3.move(ch, 0, 0)
        else:
            canvas3.move(ch,-10,0)
    
def right(event):
    if not paused:
        x,y,p,q=canvas3.bbox(ch)
        if x>1200:
            canvas3.move(ch, 0, 0)
        else:
            canvas3.move(ch,10,0)
    
def up(event):
    if not paused:
        x,y,p,q=canvas3.bbox(ch)
        if y<5:
            canvas3.move(ch, 0, 0)
        else:
            canvas3.move(ch,0,-10)
   
def down(event):
    if not paused:
        x,y,p,q=canvas3.bbox(ch)
        if q>544:
            canvas3.move(ch, 0, 0)
        else:
            canvas3.move(ch,0,10)
def overlapping(leafyy,ch):
    a,b,c,d=canvas3.bbox(leafyy)
    e,f,g,h=canvas3.bbox(ch)
    if (a<g and c>e and b<h and d>f):
        return True
    else:
        return False

def savegame(leaf,ch):      #saving game
    show_frame(frame1)
    
def loadgame(leaf,ch):      #loading saved game
    show_frame(main)
   

    
def update_image(h):       
    canvas3.delete(h)
    canvas3.update()
def replace_image(img1,img2):
    canvas3.itemconfig(img1,image=img2)
    canvas3.coords(img1,v1,v2)

#Defining function for cheat code , boss key and return to main menu
def press(event):
    global ch
    global photo3
    global img
    global v1
    global v2
    global called 
    if event.char=='a':
        called='True'
        v1,v2=canvas3.coords(ch)
        v1=v1
        v2=v2+70
        replace_image(ch,img)
    if event.char=='b':
        v1,v2=canvas3.coords(ch)
        v1=v1
        v2=v2-70
        replace_image(ch,photo3)
    if event.char=='e':
        show_frame(myboss)
    if event.char=='r':
        show_frame(frame1)
    

#Calculating life and score of character
#If character hits an obstacle , it loses one life and the score reduces by 20
#If character manages to pass by an obstacle without hitting it , character gets 50 points
def chrlife():
    global score
    global o
    global life
    global leaflife
    global value 
    if o:
        mylist.append(value)
        if mylist.count(value)==1:
            life-=1
            score-=20
    return life
def flash():
    global widthl
    global heightl
    global myflash
    fl=tk.PhotoImage(file='flash.gif')
    myflash=canvas3.create_image(widthl-20,heightl-20,image=fl,anchor='nw')       #Creating flash near point of collision   
    canvas3.update()
def flashdel():
    canvas3.delete(myflash)      
def handler(event):          #For Keys such as boss key ,return and show leaderboard to work in all frames and not just main frame
    if event.char=='v':
        show_frame(leader)
    if event.char=='e':
        show_frame(myboss)
    if event.char=='r':
        show_frame(frame1)
def pausegame():
    show_frame(mypause)
def resumegame():
    show_frame(main)
if not os.path.isfile('leaderboard3.txt'):
    text1=''
else:
    file1=open('leaderboard3.txt','r')
    text1=file1.read()
    file1.close() 
canvas7.create_text(500,50,text='LEADERBOARD',fill='black',font=('Helvetica',35))
canvas7.create_text(500,600,text=text1,fill='black',font=('Helvetica',24))
def quit_game():
    root.destroy()
def bosskey(event):  #for boss key to work in all frames and not just main frame
    if event.char=='e':
        show_frame(myboss)
    if event.char=='r':
        show_frame(frame1)
def controls(event):
    if event.char=='z':
        show_frame(controlframe)
'''frame codes'''
'''frame1 code'''
root.bind('<Key>',bosskey)
b1=tk.Button(frame1,image=p1,borderwidth=0,highlightthickness=0,bd=0,bg='SteelBlue1',activebackground='SteelBlue1',command=lambda:loadingFrame1())
b2=tk.Button(frame1,image=p2,borderwidth=0,highlightthickness=0,bd=0,bg='SteelBlue1',activebackground='SteelBlue1',command=lambda:show_frame(main))
b3=tk.Button(frame1,image=p3,borderwidth=0,highlightthickness=0,bd=0,bg='SteelBlue1',activebackground='SteelBlue1',command=lambda:show_frame(leader))
b4=tk.Button(frame1,image=p4,borderwidth=0,highlightthickness=0,bd=0,bg='SteelBlue1',activebackground='SteelBlue1',command=lambda:quit_game())
b5=tk.Button(frame1,image=p5,borderwidth=0,highlightthickness=0,bd=0,bg='SteelBlue1',activebackground='SteelBlue1',command=lambda:show_frame(controlframe))
b1window=canvas.create_window(850,20,anchor='nw',window=b1)
b2window=canvas.create_window(850,130,anchor='nw',window=b2)
b3window=canvas.create_window(850,240,anchor='nw',window=b3)
b4window=canvas.create_window(850,350,anchor='nw',window=b4)
b5window=canvas.create_window(850,460,anchor='nw',window=b5)

canvas9.create_text(650,170,text='GAME PAUSED....',fill='black',font=('Helvetica',45))
buttonpause=tk.Button(main,image=ps,borderwidth=0,highlightthickness=0,bd=2,bg='SteelBlue1',activebackground='SteelBlue1',command=lambda:pausegame())
buttonpausewindow=canvas3.create_window(1150,10,anchor='nw',window=buttonpause)
buttonresume=tk.Button(mypause,image=resume,borderwidth=0,highlightthickness=0,bd=2,bg='SteelBlue1',activebackground='SteelBlue1',command=lambda:resumegame())
buttonresumewindow=canvas9.create_window(600,350,anchor='nw',window=buttonresume)


#showing frame1---menu frame
show_frame(frame1)

#frame main code
button1=tk.Button(main,text='SAVE GAME',borderwidth=5,highlightthickness=5,bd=5,bg='SteelBlue1',activebackground='SteelBlue1',command=lambda:savegame(leaf,ch))
button1window=canvas3.create_window(20,20,anchor='nw',window=button1)

#Getting name entry from user
#Please write name in CAPITAL
canvas8.create_text(600,170,text='Please enter name in CAPITAL letters',font=('Helvetica',30),fill='black')
name=tk.Entry(canvas8,font=('Arial Bold',35),fg='black',width=20,textvariable=v,bg='white')
canvas8.create_window(620,270,window=name)
buttonentry=tk.Button(playerentry,image=nextimg,borderwidth=0,highlightthickness=0,bg='SteelBlue1',activebackground='SteelBlue1',command=lambda:getentry())
buttonentrywindow=canvas8.create_window(500,380,anchor='nw',window=buttonentry)



#game code
#Creates a loop that repeats leaf motion till life becomes 0
while life!=0:           #Game continues till life becomes 0
    for i in range(7):   #Since there are 7 leaves
        left1,top1,right1,bottom1=canvas3.bbox(ch)
        left2,top2,right2,bottom2=canvas3.bbox(leaf[i])
        root.bind('<Left>',left)
        root.bind('<Right>',right)
        root.bind('<Up>',up)
        root.bind('<Down>',down)
        root.bind('<Key>',press)
        canvas3.move(leaf[i],0,y[i])
        value=i
        o=overlapping(leaf[i],ch)
        widthl,heightl=canvas3.coords(leaf[i])
        #Repeating leaf motion after reaching height of 660 
        if top2>660:                                  
            canvas3.coords(leaf[i],widthl,20)   #Changing height to 20 to repeat motion
            canvas3.move(leaf[i],0,2)    
        life=chrlife()

        if life==2:
            update_image(imgl3)
        elif life==1:
            update_image(imgl2)
        elif life==0:
            c='False'
            update_image(imgl1)
        #Checking if leaf and character overlap/collide
        if o:                    
            flash()
            time.sleep(0.2)
            '''flashdel()'''
            break
        #Checking if character completes the game before losing all lives
        elif int(right1)==1265:
            c='True'
            break
        #Checking if small version of character completes game before losing all lives
        elif int(right1)==1241 and called=='True':
            c='True'
            break
        else: 
            pass
    time.sleep(0.02)
    root.update()
    if c=='True':
        time.sleep(0.4)
        break
    elif c=='False':
        time.sleep(0.4)
        
        
        break


root.bind('<Key>',handler)
#Displaying score, life and game over  
canvas5.create_text(520,350,fill='black',font=('Cooper Black',50),text='SCORE:'+' '+ str(score))
canvas5.create_text(430,440,fill='black',font=('Cooper Black',50),text='LIFE:'+' '+ str(life))
canvas5.create_text(350,25,fill='black',font=('Cooper Black',25),text='Press <v> to view leaderboard')
canvas6.create_text(720,80,fill='black',font=('Cooper Black',50),text='CONGRATULATIONS...YOU WIN!!!')
canvas6.create_text(520,350,fill='black',font=('Cooper Black',50),text='SCORE:'+' '+ str(score))
canvas6.create_text(430,440,fill='black',font=('Cooper Black',50),text='LIFE:'+' '+ str(life))
canvas6.create_text(350,25,fill='black',font=('Cooper Black',25),text='Press <v> to view leaderboard')
#Creating keaderboard file to store score,position and name if file does not exist
#If file exist , opening it in append mode to add data
if not os.path.isfile('leaderboard3.txt'):
    file1=open('leaderboard3.txt','w')
else:
    file1=open('leaderboard3.txt','a')

#Determining position in leaderboard based on score
pos=0
if score==350:
    pos=1
elif score==330:
    pos=2
elif score==310:
    pos=3
elif score==290:
    pos=4
else:
    pos=5

#Storing leaderboard data into a dictionary and writing data from dictionary to file
d[myname]=score

#Writing data--name,score,position into file

for key in d:
    file1.write('Name:'+'  '+key+'  '+'Score:'+str(d[key])+'  '+'Position:'+str(pos)+'\n')


#Determining if player loses or wins

if life==0:
    show_frame(lost)
if life!=0:
    show_frame(win) 
root.mainloop()
