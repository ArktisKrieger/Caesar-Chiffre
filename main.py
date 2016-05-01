# -*- coding: utf-8 -*-
# Python 3.2 
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import * # use system control theme
from tkinter import messagebox
from method import *
import fileinput

root=Tk()
root.title("ИБ. Лабораторная работа №3")
root.iconbitmap('myicon.ico')


pos='+'+str(int(root.winfo_screenwidth()/3))+'+'+str(int(root.winfo_screenheight()/4))

root.geometry('600x400'+pos)
root.minsize(600,400)
root.maxsize(600,400)

bpanel=Frame(root,borderwidth=10)
bpanel.pack(side=BOTTOM)
rbpanel=Frame(root,borderwidth=10)
rbpanel.pack(side=BOTTOM)
kpanel=Frame(root,borderwidth=10)
kpanel.pack(side=BOTTOM)




label1=Label(root, text='Cообщение')
label1.pack(side=TOP)

mpanel=Frame(root,borderwidth=5)
mpanel.pack(side=TOP)

#label1=Label(root,text=' Шифрованное сообщение')
#label1.pack(side=TOP)

#cmpanel=Frame(root,borderwidth=15)
#cmpanel.pack(side=TOP)






sb1 = Scrollbar(mpanel)
text1=Text(mpanel,font='Arial 12',wrap=WORD,height=15,width=55)
text1.insert(END,"Съешь же ещё этих мягких французских булок, да выпей чаю.")
text1.pack(side=LEFT)
sb1.config(command=text1.yview)
text1.config(yscrollcommand=sb1.set)
sb1.pack(side=RIGHT,fill=Y)



#sb2 = Scrollbar(cmpanel)
#em=StringVar() # зашифрованное сообщение
#text2=Text(cmpanel,font='Arial 12',wrap=WORD, height=5,width=55)
#text2.pack(side=LEFT)
#sb2.config(command=text2.yview)
#text2.config(yscrollcommand=sb2.set)
#sb2.pack(side=RIGHT,fill=Y)


label3=Label(kpanel,text='Ключ: ')
label3.pack(side=LEFT)
skey=StringVar()
skey.set("3")
edit1=Entry(kpanel,textvariable=skey)
edit1.pack(side=LEFT)



cryptm=IntVar()
cryptm.set(1)
rbutton1=Radiobutton(rbpanel,text='Шифр Цезаря',variable=cryptm,value=1)
rbutton2=Radiobutton(rbpanel,text='Шифр Замены',variable=cryptm,value=2)
rbutton1.pack(side=LEFT)
rbutton2.pack(side=LEFT)



def button2_clicked():
    s=text1.get(0.0, "end")
  #  print(s)
  #  print(skey.get())
    if len(skey.get())>0:
        if cryptm.get()==1:
            if skey.get().isdigit()==TRUE:
                text1.delete("1.0", END)
                ikey=int(skey.get())%abp
                text1.insert('end',cezar_encode(s,ikey,ab))
        else:
            if len(skey.get())==len(ab):
                text1.delete("1.0", END)
                text1.insert('end',exchange_encode(s,skey.get(),ab))
            else:
                messagebox.showerror('шифрование заменой','число символов перемешанного алфавита не соостветсвует числу символов исходного алфавита')
    pass



def button1_clicked():
    messagebox.showinfo('ИНФОРМАЦИОННАЯ БЕЗОПАСНОСТЬ',"Лабораторная работа №3"+
                                '\n'+"выполнил: Новиков А.В гр.448, каф АСУ, 2011 г.")
    pass

def button3_clicked():# очистить
    text1.delete("1.0","end")
    pass

def button4_clicked():#сохранить
     sf = asksaveasfilename()
     if len(sf)>0:
         msg = text1.get(1.0,END)
         f = open(sf,"w")
         f.write(msg)
         f.close()
     pass

def button5_clicked():#открыть
    op = askopenfilename()
    if len(op)>0:
   # text2.insert("end",op)
        for sf in fileinput.input(op):
      #  sf=sf.encode('1251')
            text1.insert("end",sf)
    pass

def button7_clicked():#сохранить
     sf = asksaveasfilename(title='сохранение ключа в файл')
     if len(sf)>0:
         f = open(sf,"w")
         f.write(skey.get())
         f.close()
     pass

def button6_clicked():#открыть
    op = askopenfilename(title='загрузка ключа из файла')
    if len(op)>0:
        print(op)
   # text2.insert("end",op)
        for sf in fileinput.input(op):
      #  sf=sf.encode('1251')
            skey.set(sf)
    pass


def button8_clicked():# расшифровка
    s=text1.get(0.0,"end")
    if len(skey.get())>0:
        if cryptm.get()==1:
            if skey.get().isdigit()==TRUE:
                ikey=int(skey.get())%abp
                text1.delete("1.0", END)
          #  if ikey>0:
          #      ikey=-ikey
          #  else:
           #     ikey=abs(ikey)
            #text1.insert('end',cezar_encode(s,ikey,ab))
                text1.insert('end',cezar_decode(s,ikey,ab))
        else:
            if len(skey.get())==len(ab):
                text1.delete("1.0", END)
                text1.insert('end',exchange_decode(s,skey.get(),ab))
            else:
                messagebox.showerror('расшифрование заменой','число символов перемешанного алфавита не соостветсвует числу символов исходного алфавита')
    pass



button2=Button(bpanel,text='Шифровать',command=button2_clicked)
button2.pack(side=LEFT)

button8=Button(bpanel,text='Расшифровать',command=button8_clicked)
button8.pack(side=LEFT)

button3=Button(bpanel,text='очистить',command=button3_clicked)
button3.pack(side=LEFT)

button4=Button(bpanel,text='сохранить',command=button4_clicked)
button4.pack(side=LEFT)

button5=Button(bpanel,text='открыть',command=button5_clicked)
button5.pack(side=LEFT)

button1=Button(bpanel,text="о программе ",command=button1_clicked)
button1.pack(side=LEFT)

button6=Button(kpanel,text='открыть',command=button6_clicked )
button6.pack(side=LEFT)

button7=Button(kpanel,text='сохранить',command =button7_clicked )
button7.pack(side=LEFT)

root.mainloop()