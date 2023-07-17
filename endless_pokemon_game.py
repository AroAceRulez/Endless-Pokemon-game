from tkinter import *
from PIL import ImageTk, Image
import random

root=Tk()
root.title("Endless Pokemon Game")
root.geometry("800x800")
root.configure(bg="#96dfc9")

abra= ImageTk.PhotoImage(Image.open('abra.jpg'))

bulbasour= ImageTk.PhotoImage(Image.open('bulbasour.jpg'))

img= ImageTk.PhotoImage(Image.open('button.jpg'))

img2= ImageTk.PhotoImage(Image.open('button.jpg'))

charmander= ImageTk.PhotoImage(Image.open('charmender.jpg'))

ivysour= ImageTk.PhotoImage(Image.open('iyvasour.jpg'))

kadabra= ImageTk.PhotoImage(Image.open('kadabra.jpg'))

meowth= ImageTk.PhotoImage(Image.open('meowth.jpg'))

nidoking= ImageTk.PhotoImage(Image.open('nidoking.jpg'))

paras= ImageTk.PhotoImage(Image.open('paras.jpg'))

persion= ImageTk.PhotoImage(Image.open('persion.jpg'))

pikachu= ImageTk.PhotoImage(Image.open('pikachu.jpg'))

ratata= ImageTk.PhotoImage(Image.open('ratata.jpg'))

squirtle= ImageTk.PhotoImage(Image.open('squirtle.jpg'))

p1=Label(root, text="Player 1", bg="#96dfc9", fg="black", font=("curlz mt", 13, "bold"))
p1.place(relx=0.15, rely=0.3, anchor=CENTER)

p2=Label(root, text="Player 2", bg="#96dfc9", fg="black", font=("curlz mt", 13, "bold"))
p2.place(relx=0.85, rely=0.3, anchor=CENTER)

title = Label(root,text="Endless Pokemon Game", bg="#96dfc9", fg="#2c3abe", font=("curlz mt", 24, "bold", "italic"))
title.place(relx=0.5, rely=0.15, anchor=CENTER)

p1_count=Label(root, bg="#96dfc9", fg="white", font=("curlz mt", 16, "bold"))
p1_count.place(relx=0.15, rely=0.4, anchor=CENTER)

p2_count=Label(root, bg="#96dfc9", fg="white", font=("curlz mt", 16, "bold"))
p2_count.place(relx=0.85, rely=0.4, anchor=CENTER)

random_pokemon_label = Label(root, bg = "#96dfc9", fg = "black")
random_pokemon_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

pokemon_list = [abra, bulbasour, charmander, ivysour, kadabra, meowth, nidoking, paras, persion, pikachu, ratata, squirtle]
power_list = [30, 60, 50, 100, 70, 60, 90, 40, 70, 200, 40, 50]

p1score=0
p2score=0

def player1 ():
    global p1score
    random_no=random.randint(0,12)
    random_pokemon= pokemon_list[random_no]
    random_pokemon_label["image"]=random_pokemon
    
    random_power = power_list[random_no]
    p1score = p1score + random_power
    p1_count["text"] = str(p1score)
    
    
    
btn=Button(root, image=img, command= player1, bg="black",border="0" )
btn.place(relx=0.15, rely=0.6, anchor=CENTER)

def player2 ():
    global p2score
    random_no=random.randint(0,12)
    random_pokemon= pokemon_list[random_no]
    random_pokemon_label["image"]=random_pokemon
    
    random_power = power_list[random_no]
    p2score = p2score + random_power
    p2_count["text"] = str(p2score)
    
    
    
btn2=Button(root, image=img2, command= player2, bg="black",border="0" )
btn2.place(relx=0.85, rely=0.6, anchor=CENTER)


root.mainloop()


