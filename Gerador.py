from tkinter import *
import random

#passstr.set(senhas)

tela= Tk()
tela.title('Gerador de senhas')
tela.geometry('400x230')
tela.minsize(400,230)
tela.maxsize(400,230)
passstr=StringVar()
tela.configure(background='#454545')

def gerador():
    caract='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*[/?°'
    for c in range(1): 
        senhas=''
        for g in range(12): 
            senhas+=random.choice(caract)
        passstr.set(senhas)
        
texto=Label(tela, text='Gerador de senhas', background='#454545', fg='White', font=('Arial', 20, 'bold'))
texto.pack()
textob= Label(tela, text='Senha:',background='#454545', fg='White', font=('Arial', 15, 'bold'))
textob.pack(padx=2)
teti= Entry(tela, textvariable=passstr,width=30, font=('Arial', 13, 'bold'),justify=CENTER).pack(padx=2)
num1= Button(tela,text='Gerar', bg='White',font=('Arial',15,'bold'), relief=SOLID,command=gerador).pack(pady=20)


tela.mainloop()
