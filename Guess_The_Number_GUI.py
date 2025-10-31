import tkinter as tk
import random
from tkinter import messagebox

def start_new_game():
    global picked_no, tries
    picked_no = random.randint(1, 100)
    tries = 0
    result_label.config(text=f"You have {max_tries} tries")
    entry.delete(0, tk.END)
    entry.focus()

def check_guess():
    global tries
    try:
        guess = int(entry.get())
        tries += 1
        
        if guess == picked_no:
            messagebox.showinfo("Winner!", f"Correct! The number was {picked_no}\nYou guessed it in {tries} tries!")
            start_new_game()
        elif tries >= max_tries:
            messagebox.showinfo("Game Over", f"Out of trials! The number was {picked_no}")
            start_new_game()
        elif guess < picked_no:
            result_label.config(text=f"Try {tries}: Too small!")
        else:
            result_label.config(text=f"Try {tries}: Too large!")
            
        entry.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def quit_game():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        window.destroy()

# Game setup
max_tries = 8
picked_no = random.randint(1, 100)
tries = 0

# Create window
window = tk.Tk()
window.title("Guess the Number")
window.geometry("350x250")

# Widgets
tk.Label(window, text="Guess a number (1-100):", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=5)
entry.bind('<Return>', lambda event: check_guess())
entry.focus()

# Buttons frame
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Submit Guess", command=check_guess, bg="lightblue").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="New Game", command=start_new_game, bg="lightgreen").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Quit", command=quit_game, bg="lightcoral").pack(side=tk.LEFT, padx=5)

result_label = tk.Label(window, text=f"You have {max_tries} tries", font=("Arial", 10))
result_label.pack(pady=10)

# Debug button (optional)
tk.Button(window, text="Reveal Number", 
          command=lambda: messagebox.showinfo("Secret", f"Number: {picked_no}")).pack()

window.mainloop()
