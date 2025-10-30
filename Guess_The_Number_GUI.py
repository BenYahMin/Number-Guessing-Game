import tkinter as tk
import random
from tkinter import messagebox

def check_guess():
    global tries
    try:
        guess = int(entry.get())
        tries += 1
        
        if guess == picked_no:
            messagebox.showinfo("Winner!", f"Correct! The number was {picked_no}\nYou guessed it in {tries} tries!")
            window.destroy()
        elif tries >= max_tries:
            messagebox.showinfo("Game Over", f"Out of trials! The number was {picked_no}")
            window.destroy()
        elif guess < picked_no:
            result_label.config(text=f"Try {tries}: Too small!")
        else:
            result_label.config(text=f"Try {tries}: Too large!")
            
        entry.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Game setup
picked_no = random.randint(1, 100)
tries = 0
max_tries = 8

# Create window
window = tk.Tk()
window.title("Guess the Number")
window.geometry("300x200")

# Widgets
tk.Label(window, text="Guess a number (1-100):").pack(pady=10)
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=5)
entry.bind('<Return>', lambda event: check_guess())

tk.Button(window, text="Submit", command=check_guess).pack(pady=5)
result_label = tk.Label(window, text=f"You have {max_tries} tries", font=("Arial", 10))
result_label.pack(pady=10)

# Debug button
tk.Button(window, text="Reveal Number", 
          command=lambda: messagebox.showinfo("Secret", f"Number: {picked_no}")).pack()

window.mainloop()