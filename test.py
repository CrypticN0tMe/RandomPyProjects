import customtkinter

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def showpw():
    print("password")

def login():
    print("it works")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="login System")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="enter your user")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="enter your password", show="*")
entry2.pack(pady=12, padx=10)

showPW = customtkinter.CTkCheckBox(master=frame, text="show password", command=showpw)
showPW.pack(pady=12, padx = 10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady= 12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="rember me")
checkbox.pack(pady=12, padx=10)

root.mainloop()