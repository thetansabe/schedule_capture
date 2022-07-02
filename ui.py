import tkinter as tk
from tkinter import StringVar, ttk, messagebox
import os
from unittest import skip

from main import mainFunction

#default file path
curr_directory = os.path.abspath(os.getcwd())

###Intial UI
root = tk.Tk()
root.title('Screenshot schedule')
root.geometry("500x300")

###Create UI
#inputs
username = StringVar()
label1 = tk.Label(root, text='Username: ').grid(row=0, column=0)
input1 = tk.Entry(root, width=30, bg='white', fg='black', textvariable= username).grid(row=0, column=1)

password = StringVar()
label2 = tk.Label(root, text='Password: ').grid(row=1, column=0)
input2 = tk.Entry(root, width=30, bg='white', fg='black', textvariable= password).grid(row=1, column=1)

date = StringVar()
label3 = tk.Label(root, text='Date (dd/mm/yyyy): ').grid(row=2, column=0)
input3 = tk.Entry(root, width=30, bg='white', fg='black', textvariable= date).grid(row=2, column=1)

#select tag
label4 = tk.Label(root, text='Choose semester: ').grid(row=3, column=0)

n = tk.StringVar()
semesters = ttk.Combobox(root, width = 27, textvariable = n)
semesters['values'] = (
                    'HK HE 22/23', 
                    'Du Thinh 2 22/23', 
                    'HK2 22/23',
                    'Du Thinh 1 22/23', 
                    'HK1 22/23',
                    'HK HE 21/22')

semesters.grid(row=3, column=1)
semesters.current(len(semesters['values']) - 1) 

#
file_name = StringVar()
label5 = tk.Label(root, text='PNG name: ').grid(row=4, column=0)
input5 = tk.Entry(root, width=30, bg='white', fg='black', textvariable= file_name).grid(row=4, column=1)

##
semester_dict = {
    'HK HE 22/23': '118',
    'Du Thinh 2 22/23': '120',
    'HK2 22/23': '117',
    'Du Thinh 1 22/23': '119',
    'HK1 22/23': '116',
    'HK HE 21/22' : '113'
}

#file path browse
def start():
    #get data
    name_ = username.get()
    pass_ = password.get()
    date_ = date.get()
    semes = n.get()
    save_ = curr_directory + '\\' + file_name.get() + '.png'
    print(semes)
    semes_code = semester_dict.get(semes)

    print(name_)
    print(pass_)
    print(date_)
    print(semes_code)
    print(save_)

    #save cookie
    cookie = open("cookie.txt", "w")
    cookie.writelines([name_,'\n', pass_,'\n', date_, '\n',semes_code,'\n', file_name.get(),'\n'])
    cookie.close()

    #execute main function
    try:
        done = mainFunction(name_,pass_,semes_code,date_, save_)
        if done : messagebox.showinfo('Thanh cong', 'Anh thoi khoa bieu duoc luu trong thu muc chua file .exe')
        
    except Exception as inst:
        messagebox.showerror('Failed', inst.args)

    root.destroy()



def getCookie():
    cookie = open("cookie.txt", "r")
    datas = cookie.readlines()
    cookie.close()
    
    username.set(datas[0].rstrip()) 
    password.set(datas[1].rstrip())
    date.set(datas[2].rstrip())

    new_semes_code = datas[3].rstrip()
    file_name.set(datas[4].rstrip()) 

    for key, val in semester_dict.items():
        if(val == new_semes_code):
            n.set(key)


cache_btn = tk.Button(root, text="Cookie", padx= 20, pady=10, command=getCookie).grid(row=6, column=0)
start_btn = tk.Button(root, text="Start", padx= 20, pady=10, command=start).grid(row=6, column=1)

#running
root.mainloop()