a=int(input("please Enter First number"))
import tkinter as tk
import random

# Global variables
secret_number = random.randint(1, 100)   # Computer ka random number (1-100)
attempts = 0
max_attempts = 3
guessed_numbers = []

def check_guess():
    global attempts, secret_number
    
    try:
        user_guess = int(entry.get())
    except ValueError:
        result_label.config(text="⚠️ Please enter a valid number!", fg="red")
        return
    
    attempts += 1
    guessed_numbers.append(user_guess)

    if user_guess == secret_number:
        result_label.config(text=f"🎉 You Win! Correct Number {secret_number}", fg="green")
        guess_button.config(state="disabled")
    elif attempts < max_attempts:
        if user_guess < secret_number:
            result_label.config(text=f"❌ Too Low! Tries left: {max_attempts - attempts}", fg="red")
        else:
            result_label.config(text=f"❌ Too High! Tries left: {max_attempts - attempts}", fg="red")
    else:
        result_label.config(text=f"☠️ Game Over! Number was {secret_number}", fg="black")
        guess_button.config(state="disabled")

    info_label.config(text=f"No. of guesses: {attempts}\nGuessed numbers: {guessed_numbers}")

def restart_game():
    global secret_number, attempts, guessed_numbers
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_numbers = []
    result_label.config(text="Guess a number between 1 and 100", fg="blue")
    info_label.config(text="")
    entry.delete(0, tk.END)
    guess_button.config(state="normal")

# GUI setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("450x350")
root.config(bg="#dfe6e9")

frame = tk.Frame(root, bg="white", bd=3, relief="solid")
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)

title_label = tk.Label(frame, text="🔢 Guess the Number (1-100)", font=("Arial", 14, "bold"), bg="white", fg="navy")
title_label.pack(pady=10)

entry = tk.Entry(frame, font=("Arial", 14), justify="center", width=10, bd=2, relief="solid")
entry.pack(pady=10)

guess_button = tk.Button(frame, text="GUESS", font=("Arial", 12, "bold"), bg="#6c5ce7", fg="white", command=check_guess)
guess_button.pack(pady=5)

restart_button = tk.Button(frame, text="Restart Game", font=("Arial", 12, "bold"), bg="#00cec9", fg="white", command=restart_game)
restart_button.pack(pady=5)

result_label = tk.Label(frame, text="Guess a number between 1 and 100", font=("Arial", 12, "bold"), fg="blue", bg="white")
result_label.pack(pady=10)

info_label = tk.Label(frame, text="", font=("Arial", 11), bg="white", fg="black")
info_label.pack(pady=5)

root.mainloop()
