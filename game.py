import tkinter as tk
from tkinter import messagebox
import random


def check_guess():
    try:
        guess = int(entry.get())
        if guess == secret_number:
            messagebox.showinfo("Result", "You Won!")
            root.destroy()
        else:
            messagebox.showwarning("Result", "Wrong! Try again.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


root = tk.Tk()
root.title("Keele Game Assignment")
root.geometry("300x200")

secret_number = random.randint(1, 10)

tk.Label(root, text="Guess a number between 1 and 10", pady=20).pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Submit Guess", command=check_guess, pady=10).pack()

root.mainloop()
