from tkinter import *
from random import *
import regressionModel as R
import tkinter.messagebox
def team1():
    tan=Tk()

    ab=Label(tan,text="A\nK\nK\nS",font="Helvetica 18")
    ab.grid(row=1,column=0)
    khali1=Label(tan,text="         ",font="Helvetica 24")
    khali2=Label(tan,text="         ",font="Helvetica 24")
    khali3=Label(tan,text="         ",font="Helvetica 24")
    khali4=Label(tan,text="         ",font="Helvetica 18")
    khali5=Label(tan,text="         ",font="Helvetica 18")
    khali6=Label(tan,text="         ",font="Helvetica 18")
    khali1.grid(row=0,column=1)
    khali2.grid(row=0,column=3)
    khali3.grid(row=0,column=5)
    khali4.grid(row=1,column=1)
    khali5.grid(row=1,column=3)
    khali6.grid(row=1,column=5)

    roll=Label(tan,text="4\n4\n4\n4",font="Helvetica 18")
    roll.grid(row=1,column=2)
    phone=Label(tan,text="9\n9\n8\n8",font="Helvetica 18")
    phone.grid(row=1,column=4)
    email=Label(tan,text="a@gmail.com\nk@gmail.com\nk@gmail.com\ns@gmail.com",font="Helvetica 18")
    email.grid(row=1,column=6)
    tan.mainloop()
def llist1():
    llisting=Tk()
    def goback():
        llisting.destroy()
    image3= PhotoImage(file='back.png')
    l1=Label(llisting,text="Code",font="Helvetica 20 bold")
    l1.grid(row=0,column=0)
    l2=Label(llisting,text="        ",font="Helvetica 20 bold")
    l2.grid(row=0,column=1)
    l3=Label(llisting,text="Locality",font="Helvetica 20 bold")
    l3.grid(row=0,column=2)
    l4=Label(llisting,text="0.\n1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.\n10.\n11.\n12.\n13.\n14.",font="helvetica 16")
    l4.grid(row=1,column=0)
    l5=Label(llisting,text="        ",font="Helvetica 16 bold")
    l5.grid(row=1,column=1)
    l6=Label(llisting,text="Arroyo Grande\nAtascadero\nBuelton\nCambria\nGrover Beach\nLompoc\nLos Osos\nMorro Bay\nNipomo\nPaso Robles\nPimo Beach\nSan Luis Obispo\nSan Miguel\nSanta Maria-Orcutt\nTemptation",font="helvetia 16")
    l6.grid(row=1,column=2)


    but=Button(llisting,text="Back",font="Helvetica12",justify="left",command=goback)
    but.grid(row=2,column=0)
    llisting.mainloop()
def part():
    party=Tk()
    def llist():
        llist1()
    Locality=Button(party,text="Locality table",command=llist)
    Locality.grid(row=8,column=4)
    khali=Label(party,text="      \n ")
    khali.grid(row=1,rowspan=2,column=3)
    def Close():
        party.destroy()
    def Back():
        party.destroy()
        maina()
    def win1():
        party.destroy()
        efgh()
    def win2():
        party.destroy()
        ijkl()
    khali2=Label(party,text="    ")
    khali2.grid(row=6,column=0)
    khali3=Label(party,text="               ")
    khali3.grid(row=4,column=0)
    khali3=Label(party,text="           ")
    khali3.grid(row=3,column=6)
    image1 =  PhotoImage(file='pic1.png')
    # laimage1=Label(party,image=image1)
    image2=PhotoImage(file='estimation.png')
    image3=PhotoImage(file='back.png')
    image4=PhotoImage(file='close.png')

    # laimage2=Label(party,image=image2)
    # laimage1.grid(row =1,rowspan=2,column=0,columnspan=2)
    # laimage2.grid(row=1,rowspan=2,column=4,columnspan=6)
    button1=Button(party,image=image1,command=win1)
    button1.grid(row=3,column=1,pady=5)
    # labelkhali=Label(party,text="         ")
    # labelkhali.grid(row=3,column=3)
    button2=Button(party,image=image2,command=win2)
    button2.grid(row=3,column=5,pady=5)

    label1=Label(party,text=" Loan Estimation",font="Helvetica 16 bold")
    label1.grid(row=2,column=1)
    label2=Label(party,text=" Land Evaluation",font="Helvetica 16 bold")
    label2.grid(row=2,column=5)
    button3=Button(party,image=image3,justify="left",command=Back)
    button4=Button(party,image=image4,justify="right",command=Close)
    button3.grid(row=5,column=1)
    button4.grid(row=5,column=5)

    contact=Label(party,text="Contact us @")
    contact2=Label(party,text="k@mail.com")
    contact.grid(row=7,column=1)
    contact2.grid(row=7,column=5)
    party.mainloop()
def ijkl():
    abcd=Tk()
    abcd.wm_title("  LAND EVALUATION")
    welcome=Label(abcd,text="Enter the housing details\n",font="Helvetica 22 ")
    welcome.grid(row=0,column=0,columnspan=4)
    la1=Label(abcd,text="Locality",font="Helvetica 16 bold")
    la1.grid(row=1,column=0)
    var = StringVar()
    var.set(0)
    option = OptionMenu(abcd, var,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14 )
    option.grid(row=1,column=1,columnspan=4)

    l5=Label(abcd,text="No of Rooms",font="Helvetica 16 bold")
    l5.grid(row=2,column=0)
    l6=Label(abcd,text="Bath",font="Helvetica 16 bold")
    l6.grid(row=3,column=0)
    l7=Label(abcd,text='Area',font="Helvetica 16 bold")
    l7.grid(row=4,column=0)
    cc=StringVar()
    nr=StringVar()
    bat=StringVar()
    are=StringVar()
    def testVal(inStr,i,acttyp):
        ind=int(i)
        if acttyp == '1': #insert
            if not inStr[ind].isdigit():
                return False
        return True
    def testVal1(inStr,i,acttyp):
        ind=int(i)
        if acttyp == '1': #insert
            if not inStr[ind].isalpha():
                return True
        return False
    image1=PhotoImage(file="back.png")
    image2=PhotoImage(file="home1.png")
    image3=PhotoImage(file="submit.png")
    e3=Entry(abcd,textvariable=cc,validate="key",width=25,selectbackground="red")
    e3['validatecommand'] = (e3.register(testVal),'%P','%i','%d')
    e3.grid(row=2,column=1,columnspan=4,pady=4,padx=4)
    e4=Entry(abcd,textvariable=nr,validate="key",width=25)
    e4['validatecommand'] = (e3.register(testVal),'%P','%i','%d')
    e4.grid(row=3,column=1,columnspan=4,pady=4,padx=4)
    e5=Entry(abcd,textvariable=bat,width=25,validate="key")
    e5['validatecommand'] = (e3.register(testVal),'%P','%i','%d')
    e5.grid(row=4,column=1,pady=4,padx=4,columnspan=4)


    l12=Button(abcd,text="Predict")
    l12.grid(row=6,column=0)
    def choice():
        a=var.get()
        b=e3.get()
        c=e4.get()
        d=e5.get()
        a=int(a)
        b=int(b)
        c=int(c)
        d=int(d)
        if b>10 or b<1 or c>10 or c<1 or d>10000 or d<1000:
            tkinter.messagebox.showinfo("wrong input","Check your room and bath value")
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
        else:
            t1.delete("1.0",END)
            t1.insert(END,R.regression(a,b,c,d))


    l12=Button(abcd,text="Predict",command=choice)
    l12.grid(row=6,column=0)

    t1=Text(abcd,width=7,height=2)
    t1.grid(row=6,column=1,columnspan=4)
    #
    # b4=Button(abcd,image=image3,justify="center")
    # b4.grid(row=8,column=1)
    def goo():
        abcd.destroy()
        maina()
    def abcde():
        abcd.destroy()
        part()
    khalii=Label(abcd,text="")
    khalii.grid(row=7,column=0)
    b7=Button(abcd,image=image2,command=goo)
    b7.grid(row=9,column=3)
    # khali8=Label(abcd,text="")
    # khali8.grid(row=9,column=0)
    b8=Button(abcd,image=image1,command=abcde)
    b8.grid(row=9,column=0)
    abcd.mainloop()
def efgh():


    atta=Tk()
    def choice():
        a=e7.get()
        a=int(a)
        b=int(e8.get())
        c=int(e9.get())
        d=int(e10.get())
        e=var.get()
        if a<3:
            tkinter.messagebox.showinfo("LOw Score","Can't get loan too low credit")
            e7.delete(0,END)
        elif a>10:
            tkinter.messagebox.showinfo("High Score","Check your input very high input")
            e7.delete(0,END)
        elif b>10 or b<1 or c>10 or c<1 or d<1000 or d>10000:
            tkinter.messagebox.showinfo("wrong input","Check your room and bath value")
            e8.delete(0,END)
            e9.delete(0,END)
            e10.delete(0,END)

        else:
            credit_score=a
            prediction=R.regression(e,b,c,d)
            simple_interest = ((-3*credit_score + 33) - (21/29)*(prediction/100000) + 24 + (21/29))/2
            t1.delete("1.0",END)
            t1.insert(END,simple_interest)

    atta.wm_title("  LOAN Estimation")
    ente=Label(atta,text="Enter data for Loan estimation",font="Helvetica 24 ")
    ente.grid(row=0,column=0,columnspan=3)
    khali=Label(atta,text="")
    khali.grid(row=1,column=0)
    la1=Label(atta,text="Locality",font="Helvetica 16 bold")
    la1.grid(row=2,column=0)
    image1=PhotoImage(file="back.png")
    image2=PhotoImage(file="calculate.png")
    image3=PhotoImage(file="submit.png")
    var = StringVar()
    var.set(0)
    def testVal(inStr,i,acttyp):
        ind=int(i)
        if acttyp == '1': #insert
            if not inStr[ind].isdigit():
                return False
        return True
    def testVal1(inStr,i,acttyp):
        ind=int(i)
        if acttyp == '1': #insert
            if not inStr[ind].isalpha():
                return True
        return False
    option = OptionMenu(atta, var,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14 )
    option.grid(row=2,column=1,columnspan=4)
    l8=Label(atta,text="Credit Score",pady=1,padx=2,font="Helvetica 16 bold")
    l8.grid(row=3,column=0)
    l9=Label(atta,text="No of Rooms",pady=1,padx=2,font="Helvetica 16 bold")
    l9.grid(row=4,column=0)
    l10=Label(atta,text="Bath",pady=1,padx=2,font="Helvetica 16 bold")
    l10.grid(row=5,column=0)
    l11=Label(atta,text='Area',pady=1,padx=2,font="Helvetica 16 bold")
    l11.grid(row=6,column=0)
    cc=StringVar()
    nr=StringVar()
    bat=StringVar()
    are=StringVar()
    e7=Entry(atta,textvariable=cc,validate="key",width=25)
    e7['validatecommand'] = (e7.register(testVal),'%P','%i','%d')
    e7.grid(row=3,column=1,columnspan=4,pady=1,padx=2)
    e8=Entry(atta,textvariable=nr,validate="key",width=25)
    e8['validatecommand'] = (e8.register(testVal),'%P','%i','%d')
    e8.grid(row=4,column=1,columnspan=4,pady=1,padx=2)
    e9=Entry(atta,textvariable=bat,validate="key",width=25)
    e9['validatecommand'] = (e9.register(testVal),'%P','%i','%d')
    e9.grid(row=5,column=1,columnspan=4,pady=1,padx=2)
    e10=Entry(atta,textvariable=are,validate="key",width=25)
    e10['validatecommand'] = (e10.register(testVal),'%P','%i','%d')
    e10.grid(row=6,column=1,columnspan=4,pady=1,padx=2)

    l12=Label(atta,text="SI",font="Helvetica 16 bold")
    l12.grid(row=8,column=0)
    b5=Button(atta,image=image2,command=choice)
    b5.grid(row=9,column=2,ipadx=4,ipady=4,padx=4,pady=4)
    t1=Text(atta,width=10,height=1)
    t1.grid(row=8,column=2,ipadx=4,ipady=4,padx=4,pady=4)
    def goback():
        atta.destroy()
        part()
    b6=Button(atta,image=image1,command=goback)
    b6.grid(row=9,column=0)
    atta.mainloop()
def final():
    abcd=Tk()
    abcd.wm_title("  Credit")
    welcome=Label(abcd,text="Enter the housing details\n",font="Helvetica 22 ")
    welcome.grid(row=0,column=0,columnspan=4)
    la1=Label(abcd,text="Locality",font="Helvetica 16 bold")
    la1.grid(row=1,column=0)
    var = StringVar()
    var.set("Arroyo Grande")
    option = OptionMenu(abcd, var,"Arroyo Grande","Atascadero","Buelton","Cambria","Grover Beach","Lompoc","Los Osos","Morro Bay","Nipomo","Paso Robles","Pimo Beach","San Luis Obispo","San Miguel","Santa Maria-Orcutt","Temptation" )
    option.grid(row=1,column=1,columnspan=4)
    l4=Label(abcd,text="Cost",font="Helvetica 16 bold")
    l4.grid(row=5,column=0)
    l5=Label(abcd,text="No of Rooms",font="Helvetica 16 bold")
    l5.grid(row=2,column=0)
    l6=Label(abcd,text="Bath",font="Helvetica 16 bold")
    l6.grid(row=3,column=0)
    l7=Label(abcd,text='Area',font="Helvetica 16 bold")
    l7.grid(row=4,column=0)
    cc=StringVar()
    nr=StringVar()
    bat=StringVar()
    are=StringVar()
    def testVal(inStr,i,acttyp):
        ind=int(i)
        if acttyp == '1': #insert
            if not inStr[ind].isdigit():
                return False
        return True
    def testVal1(inStr,i,acttyp):
        ind=int(i)
        if acttyp == '1': #insert
            if not inStr[ind].isalpha():
                return True
        return False
    image1=PhotoImage(file="back.png")
    image2=PhotoImage(file="home1.png")
    image3=PhotoImage(file="submit.png")
    e3=Entry(abcd,textvariable=cc,validate="key",width=25,selectbackground="red")
    e3['validatecommand'] = (e3.register(testVal),'%P','%i','%d')
    e3.grid(row=2,column=1,columnspan=4,pady=4,padx=4)
    e4=Entry(abcd,textvariable=nr,validate="key",width=25)
    e4['validatecommand'] = (e3.register(testVal),'%P','%i','%d')
    e4.grid(row=3,column=1,columnspan=4,pady=4,padx=4)
    e5=Entry(abcd,textvariable=bat,width=25,validate="key")
    e5['validatecommand'] = (e3.register(testVal),'%P','%i','%d')
    e5.grid(row=4,column=1,pady=4,padx=4,columnspan=4)
    e6=Entry(abcd,textvariable=are,width=25)
    e6.grid(row=5,column=1,pady=4,padx=4,columnspan=4)

    def close():
        a=e3.get()
        b=e4.get()
        c=e5.get()
        d=e6.get()
        e=var.get()

        b=int(b)
        c=int(c)
        d=int(d)
        a=int(a)
        if a>10 or b>10 or c>10000 or d>3000000 or d<40000 or a<1 or b<1 or c<1000 :
            tkinter.messagebox.showinfo("wrong input","Check your input value")
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e6.delete(0,END)
        else:
            b=str(b)
            c=str(c)
            d=str(d)
            a=str(a)
            f=open("RealEstateCSV.csv","a+")
            f.write(e)
            f.write(",")
            f.write(a)
            f.write(",")
            f.write(b)
            f.write(",")
            f.write(c)
            f.write(",")
            f.write(d)
            f.write("\n")
            f.close()
            a=float(e3.get())
            b=float(e4.get())
            c=float(e5.get())
            d=float(e6.get())
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e6.delete(0,END)

    b4=Button(abcd,image=image3,command=close,justify="center")
    b4.grid(row=7,column=1)
    def goo():
        abcd.destroy()
        maina()
    def abcde():
        abcd.destroy()
        create_yes()
    khalii=Label(abcd,text="")
    khalii.grid(row=6,column=0)
    b7=Button(abcd,image=image2,command=goo)
    b7.grid(row=9,column=3)
    khali8=Label(abcd,text="")
    khali8.grid(row=8,column=0)
    b8=Button(abcd,image=image1,command=abcde)
    b8.grid(row=9,column=0)
    abcd.mainloop()
def create_yes():
    username=["K","Ke","So","Am"]
    password=["a","z=x+iy123","123","chain"]
    root=Tk()
    root.wm_title("login")
    login=Label(root,text="          Enter your credentials:         ",padx=2,pady=1,font="Times 24",justify="center")
    login.grid(row=0,column=0,columnspan=5)
    l2=Label(root,text="       User ID",font="times 14 bold",pady=1)
    l2.grid(row=2,column=0)
    la2=Label(root,text=" ")
    khali=Label(root,text=":",font="Times 18 ")
    khali.grid(row=2,column=1)
    khali=Label(root,text=":",font="Times 18")
    khali.grid(row=4,column=1)
    la2.grid(row=1,column=0,columnspan=3)
    l3=Label(root,text="  Password",pady=1,font="times 14 bold",)
    l3.grid(row=4,column=0)
    user_var=StringVar()
    pass_var=StringVar()
    image=PhotoImage(file="back.png")
    image2=PhotoImage(file="submit.png")
    e1=Entry(root,textvariable=user_var,width=25)
    e1.grid(row=2,column=2,columnspan=3,padx=5,pady=10)
    la2=Label(root,text=" ")
    la2.grid(row=3,column=0,columnspan=3)
    khali3=Label(root,text="    ")
    khali3.grid(row=2,column=5,columnspan=6)
    e2=Entry(root,textvariable=pass_var,show='*',width=25)
    e2.grid(row=4,column=2,columnspan=3,padx=5,pady=10)
    # la1=Label(root,text=" ")
    # la1.grid(row=4,column=0,columnspan=3)

    def trylogin():
        count=0
        user=e1.get()
        passy=e2.get()
        for i in range(4):
            if username[i]==user and password[i]==passy:
                print("Correct")
                root.destroy()
                final()
            else:
                count+=1
        if count==4:
                tkinter.messagebox.showinfo("wrong password","try again!!!")
                print("Wrong")
                e1.delete(0,END)
                e2.delete(0,END)


    def back():
        root.destroy()
        maina()
    labp=Label(root,text="(User ID and Passoword are case sensitive!!)\n")
    labp.grid(row=5,column=0,columnspan=2)
    b3=Button(root,image=image2,command=trylogin)
    b3.grid(row=6,column=4)
    b5=Button(root,image=image,command=back)
    b5.grid(row=6,column=0)
    contact=Label(root,text="For any query:\nReach us @\n k@gmail.com")
    contact.grid(row=7,column=4)

    root.mainloop()
def maina():
    window=Tk()
    frame=Frame(window)
    frame.grid()
    frame=Frame(window,width=200,height=500)

    window.wm_title("Welcome")
    def abc():
        window.destroy()
        create_yes()

    l1=Label(window,text="Welcome to\n PELP",font="Times 32",justify="center",pady=4)
    l1.grid(row=0,column=0,columnspan=4)

    l2=Label(window,text="Property Evaluation and Loan Prediction",font="Helvetica 20",justify="center",padx=4,pady=4)
    l2.grid(row=2,column=0,columnspan=4)
    l4=Label(window,text=" ",font="Times 20",justify="center")
    l4.grid(row=6,column=0,columnspan=4)
    l5=Label(window,text=" ",font="Times 20",justify="center")
    l5.grid(row=3,column=0,columnspan=4)
    image1 =  PhotoImage(file='user.png')
    l=Label(window,image=image1)
    l.grid(row=4,column=2,columnspan=3)
    image2 =  PhotoImage(file='registrar.png')
    l2=Label(window,image=image2)
    l2.grid(row=4,column=0,columnspan=1)
    b1=Button(window,text="Admin",width=20,font ="Times 14",height=2,command=abc)
    b1.grid(row=5,column=0,pady=4,padx=4)
    def close2():
        window.destroy()
        part()
    def team():
        team1()
    image=PhotoImage(file="close.png")
    l3=Label(window,text="or ",font="calibri 20",justify="center")
    l3.grid(row=5,column=1)
    b2=Button(window,text="User",width=20,height=2,font ="Times 14",command=close2)
    b2.grid(row=5,column=3,pady=4,padx=4)
    def abcm():
        window.destroy()
    b8=Button(window,image=image,command=abcm)
    b8.grid(row=7,column=1,padx=4,pady=4)
    b9=Button(window,text="Developer Team",font="Helvetica 10",comman=team)
    b9.grid(row=7,column=3)
    contact=Label(window,text="\nContact us:\n+91-8",font="times 10 bold",anchor=W,justify=LEFT)
    contact.grid(row=6,column=0)
    contact2=Label(window,text="\nEmail:\n K7@gmail.com",font="times 10 bold",anchor=W,justify=LEFT)
    contact2.grid(row=6,column=3)

    window.mainloop()
maina()
