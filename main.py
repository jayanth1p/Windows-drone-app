
from tkinter import *

from gryoaccel import *

root=Tk()

root.title("Tech Tron")
root.geometry("880x480")

phologo=PhotoImage(file='img1.png')
# logobit=PhotoImage(file='img.bmp')

root.iconphoto(False,phologo)
l1=Label(root,text="Tech Tron project" )


fra1=Frame(root,bg="#222222",highlightbackground="#222222",highlightthickness=2)

lafra1=Label(fra1,bg="#222222",fg="white",text="TronTech Labs Drone flight Control System",font=("Arial",15))

fra2=Frame(root,bg="#3D3D3D",highlightbackground="#3D3D3D",highlightthickness=2)

but2fra2=Button(fra2,text="Take Off", fg="white", bg="green",font=("Arial",10),width=20,height=2 )
butfra2=Button(fra2,text="KILL", fg="white", bg="red",font=("Arial",10),width=20,height=2, )


laicfra2=Label(fra2,image=phologo,border=0)
fra3=Frame(fra2,bg="#3D3D3D")
gyro(fra3)
acc(fra3)


fra1.place(relx=0.24,rely=0 ,relheight=1,relwidth=0.76)
fra2.place(relx=0,rely=0,relheight=1,relwidth=0.24)


lafra1.pack(padx=100,pady=15,)

laicfra2.pack(pady=20)

fra3.pack()

butfra2.pack(side='bottom',pady=15)

but2fra2.pack(side='bottom',pady=30)

l1.place(relx=0.4 ,rely=0.4,relheight=0.2,relwidth=0.2)

root.mainloop()