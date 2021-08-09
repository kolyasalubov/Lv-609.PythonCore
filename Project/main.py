from re import search, match
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from time import sleep

class User(object):
    
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.__password = password
   
    def check_pass(self):
        """
        Lenth must be 8 - 32
        At least 1 letter between [a-z] and 1 letter between [A-Z]
        At least 1 character from [$#@]
        At least 1 number between [0-9]
        """
        if len(self.__password) < 8 or len(self.__password) > 32:
            return 'Lenth must be 8 - 32'
        elif not search('[a-z]', self.__password):
            return 'At least 1 letter between [a-z] and 1 letter between [A-Z]'
        elif not search('[A-Z]', self.__password):
            return 'At least 1 letter between [a-z] and 1 letter between [A-Z]'
        elif not search('[#$@]', self.__password):
            return 'At least 1 character from [$#@]'
        elif not search('[0-9]', self.__password):
            return 'At least 1 number between [0-9]'
        else:
            return True

names_list = []
count = 1

def counter(base: str):
    global count 
    f = open(base, 'r')
    for i in f.readlines():
        count += 1
    return count

def start():
    
    username = ent_name.get()
    # global names_list  
    # names_list.append(username)
    password = ent_pass.get()
    print(f'User input --> {username}: {password}')

    while True:
        users = User(username, password)
        # for name in names_list:
        #     if username == name:
        #         del names_list[-1]
        #         ent_name.delete(0, tk.END)
        #         tk.messagebox.showinfo(message= 'This name has already engaged')
        #         break
        if username == '' or password == '':
            print('Error')
            tk.messagebox.showinfo(message= 'Error: Nothing was input!')
            break
        elif users.check_pass() !=  True:
            print('Error')
            ent_pass.delete(0, tk.END) 
            tk.messagebox.showinfo(message= users.check_pass())
            break
        else:
            counter('users.txt')
            with open('users.txt', 'a') as users:
                users.write(f'{count}. {username} ---> {password}   {datetime.now()}\n')
            print('Autorized')
            window.destroy()
            break

window = tk.Tk()
window.title('SingIn')
window.geometry('600x110')

def rule():
    lbl_rules = tk.Label(master= frm_right, text= User.check_pass.__doc__).place(x= 265, y= 1)

lbl_name = tk.Label(master=window, text= 'Username')
ent_name = tk.Entry(master=window, width= 32)
lbl_name.place(x = 5, y = 5)
ent_name.place(x= 70, y= 5)
lbl_name.configure(font=("Courier", 9, "italic"))

lbl_pass = tk.Label(master=window, text='Password')
ent_pass = tk.Entry(master=window, width= 32)
lbl_pass.place(x= 5, y= 30)
ent_pass.place(x= 70, y = 30)
lbl_pass.configure(font=("Courier", 9, "italic"))

lbl_info = tk.Label(text='Click Rules to see information').place(x= 350, y = 38)

btn_singin = tk.Button(text='Confirm', command= start, width= 7, height= 1)
btn_singin.place(x = 205, y = 70)

btn_rules = tk.Button(text='Rules', command= rule, width= 7, height= 1).place(x = 140, y= 70)
frm_right = tk.Frame(relief= tk.GROOVE, borderwidth= 3, bg= 'blue').pack(side= tk.RIGHT)

window.mainloop()
