import random
import customtkinter
import challenges

def rand():
    num = random.randint(0, 303)
    print(challenges.projects[num])


customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="random challanges")
label.pack(pady=12, padx=10)

randomize = customtkinter.CTkButton(master=frame, text="Randomize", command=rand)
randomize.pack(pady = 12, padx = 10)

challenge = customtkinter.CTkLabel(master=frame, width=300, height=50, text=str(challenges.projects[random.randint(0, 303)]), bg_color="lightGreen", text_color="black", wraplength=200)
challenge.pack()
challenge.update()

root.mainloop()