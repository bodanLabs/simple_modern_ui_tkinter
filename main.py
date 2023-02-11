import tkinter
from lib.write_to_file import write
import customtkinter

root = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")

root.title("User-Login")
root.geometry('500x300')

def save_user_data():
    username=user_txt.get()
    password=pass_txt.get()
    write("data.txt",f'{username} -> {password}\n')


user_l = customtkinter.CTkLabel(root, text="Username",font=('Arial',15))
user_l.pack()

user_txt = customtkinter.CTkEntry(master=root,placeholder_text="username")
user_txt.pack(padx=10,pady=10)

pass_l = customtkinter.CTkLabel(root, text="Password",font=('Arial',15))
pass_l.pack()

pass_txt = customtkinter.CTkEntry(master=root,placeholder_text="password",show="*")
pass_txt.pack(padx=10,pady=10)


button = customtkinter.CTkButton(master=root,text="Log-in",font=('Arial',20),command=save_user_data)
button.pack(pady=10)


slider = customtkinter.CTkSlider(master=root, from_=0, to=100)
slider.pack(pady=10)

root.mainloop()