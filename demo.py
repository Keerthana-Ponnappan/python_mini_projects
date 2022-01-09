from tkinter import *
from tkinter import simpledialog
import random
wd = Tk()
wd.geometry('900x2000')
wd.title("GUI CREATOR")
x = 0
y = 0

def l_c():#label is clicked
    global x,y
    num = random.randint(1, 100)
    var = 'L' + str(num)
    labl.configure(text=var)
    fd =open('fname','a')
    l_name = simpledialog.askstring("Input", "Enter your label name?",parent=wd)
    bg = simpledialog.askstring("Input", "Enter your background color as hexadecimal #FFFFFF ?",parent=wd)
    fd.write("\n"+var+" = Label(wd,text = '"+l_name+"',width = 5 , bg = '"+str(bg)+"')\n")
    fd.write(var+".place(x = "+str(x)+",y= "+str(y)+")")
    y += 40
    fd.close()
    fd = open('fname','r')
    tex.delete("1.0", "end")
    tex.insert("end",fd.read())
    fd.close()

def b_c():#button is clicked
    global x,y,fname
    num = random.randint(1, 100)
    var = 'B' + str(num)
    labl.configure(text=var)
    fd =open('fname','a')
    b_name = simpledialog.askstring("Input", "Enter your button name?",parent=wd)
    bg = simpledialog.askstring("Input", "Enter your background color as hexadecimal #FFFFFF ?",parent=wd)
    fd.write("\n"+var+" = Button(wd,text = '"+b_name+"',width = 5 ,bg = '"+str(bg)+"')\n")
    fd.write(var+".place(x = "+str(x)+",y= "+str(y)+")")
    y += 40
    fd.close()
    fd = open('fname','r')
    tex.delete("1.0", "end")
    tex.insert("end",fd.read())
    fd.close()
def e_c():#entry is clicked
    global x,y,fname
    num = random.randint(1, 100)
    var = 'E' + str(num)
    labl.configure(text=var)
    fd =open('fname','a')
    e_name = simpledialog.askstring("Input", "Enter your textvariable name?",parent=wd)
    bg = simpledialog.askstring("Input", "Enter your background color as hexadecimal #FFFFFF ?",parent=wd)
    fd.write("\n"+var+" = Entry(wd,textvariable = '"+e_name+"',width = 5 ,bg = '"+str(bg)+"')\n")
    fd.write(var+".place(x = "+str(x)+",y= "+str(y)+")")
    y += 40
    fd.close()
    fd = open('fname','r')
    tex.delete("1.0", "end")
    tex.insert("end",fd.read())
    fd.close()

def rb_c():#radiobutton is clicked
    global x, y, fname
    num = random.randint(1, 6)
    var = 'RB' + str(num)
    labl.configure(text=var)
    fd = open('fname', 'a')
    fd.write("\nvar = IntVar()\n")
    rb_no = simpledialog.askinteger("Input", "Enter your no of radio button (max 5 can be added) ?", parent=wd,minvalue=0, maxvalue=5)
    bg = simpledialog.askstring("Input", "Enter your background color as hexadecimal #FFFFFF ?", parent=wd)
    for i in range(0, rb_no):
        rb_name = simpledialog.askstring("Input", "Enter your button name?", parent=wd)
        fd.write("\n" + var + " = Radiobutton(wd,text = '" + rb_name + "',variable = var,width = 5 ,bg = '" + str(bg) + "',value=" + str(i) + ")\n")
        fd.write(var + ".place(x = " + str(x) + ",y= " + str(y) + ")")
        y += 40
    fd.close()
    fd = open('fname', 'r')
    tex.delete("1.0", "end")
    tex.insert("end", fd.read())
    fd.close()

def cb_c():#checkbutton is clicked
    global x, y, fname
    num = random.randint(1, 6)
    var = 'CB' + str(num)
    labl.configure(text=var)
    fd = open('fname', 'a')
    rb_no = simpledialog.askinteger("Input", "Enter your no of check button (max 5 can be added) ?", parent=wd,minvalue=0, maxvalue=5)
    bg = simpledialog.askstring("Input", "Enter your background color as hexadecimal #FFFFFF ?", parent=wd)
    for i in range(0, int(rb_no)):
        rb_name = simpledialog.askstring("Input", "Enter your button name?", parent=wd)
        rb_var_name = simpledialog.askstring("Input", "Enter your button variable name?", parent=wd)
        fd.write("\n"+rb_var_name+"= IntVar()")
        fd.write("\n" + var + " = Checkbutton(wd,text = '" + rb_name + "',variable = "+rb_var_name+",width = 5 ,bg = '" + str(bg) + "',onvalue=1 ,offvalue= 0)\n")
        fd.write(var + ".place(x = " + str(x) + ",y= " + str(y) + ")\n")
        y += 40
    fd.close()
    fd = open('fname', 'r')
    tex.delete("1.0", "end")
    tex.insert("end", fd.read())
    fd.close()

def m_c():#message is clicked
    global x,y,fname
    num = random.randint(1, 100)
    var = 'M' + str(num)
    labl.configure(text=var)
    fd =open('fname','a')
    msg = simpledialog.askstring("Input", "Enter your  Message?",parent=wd)
    bg = simpledialog.askstring("Input", "Enter your background color as hexadecimal #FFFFFF ?",parent=wd)
    fd.write("\n"+var+" = Message(wd,text = '"+msg+"',width = 60 , bg = '"+str(bg)+"')\n")
    fd.write(var+".place(x = "+str(x)+",y= "+str(y)+")")
    y += 40
    fd.close()
    fd = open('fname','r')
    tex.delete("1.0", "end")
    tex.insert("end",fd.read())
    fd.close()




def in_loop():#loop is clicked
    fd = open('fname', 'a')
    fd.write("\n\nwd.mainloop()")
    fd.close()
    fd = open('fname', 'r')
    tex.delete("1.0", "end")
    tex.insert(INSERT, fd.read())
    fd.close()

def check():
    if  s1.get() == 'y':#s1 is variable of 'save' button
        fd = open('fname','w')
        tex1.insert(INSERT,tex.get('1.0','end'))#insert content of tex to tex1
        fd.write(tex1.get("0.0","end"))##tex1 content will be added  to the file
        tex.delete("0.0","end")#tex contents are deleted after saving tex1 content to file
        fd.close()


fd =open('fname','w')
fd.write("from tkinter import* \nwd = Tk() \nwd.geometry('700x300') \n")
s1 = StringVar()
tex = Text(wd, width = 50, height = 30, bg = 'red')
tex.place(x= 10 ,y =10)

msg = Message(wd,text="Add all widgets and then click mainloop() to get complete  code",width= 70)
msg.place(x= 700,y= 600)

lab= Label(wd,text = "enter 'y' to save the changes")
lab.place(x= 100 ,y =500)
t1 = Entry(wd,width= 15,textvariable = s1)
t1.place(x= 200 ,y =500)
sm = Button(wd,text = 'save',command = check)
sm.place(x= 300 ,y =500)

tex1 = Text(wd,width= 50,height=30,bg = 'yellow')
tex1.place(x= 400 ,y =10)

labl = Label(wd , width=7 ,height=3,bg = 'cyan')
labl.place(x=10 ,y =500)



bt = Button(wd , text = 'Label', width=10,height=3,command = l_c)
bt.place(x= 10 ,y =600)

bt = Button(wd ,text = 'Button',  width=10,height=3,command = b_c)
bt.place(x= 100 ,y =600)

bt = Button(wd , text = 'Entry', width=10,height=3, command=e_c)
bt.place(x= 200 ,y =600)

bt = Button(wd , text = 'Radio Button',  width=10,height=3,command=rb_c)
bt.place(x= 300 ,y =600)

bt = Button(wd  ,text = 'Check Button', width=10,height=3, command=cb_c)
bt.place(x= 400 ,y =600)

bt = Button(wd  ,text = 'message', width=10,height=3, command=m_c)
bt.place(x= 500 ,y =600)

bt = Button(wd , text = 'main_loop', width=10,height=3, command=in_loop)
bt.place(x= 600 ,y =600)
fd.close()

wd.mainloop()

