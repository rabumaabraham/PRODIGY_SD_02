import tkinter as tk
import random
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        self.root.config(bg="#f4f4f4")

        # Generate random number (1-10) and initialize attempts
        self.random_number = random.randint(1, 10)
        self.attempts = 0

        # Header
        header = tk.Label(
            root,
            text="Guess the Number",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=10
        )
        header.pack(fill=tk.X)

        # Instructions
        instructions = tk.Label(
            root,
            text="I'm thinking of a number between 1 and 10.\nCan you guess it?",
            font=("Arial", 12),
            bg="#f4f4f4",
            fg="#333",
            pady=20,
        )
        instructions.pack()

        # Input Section
        self.entry_guess = tk.Entry(root, font=("Arial", 14), justify="center", width=10)
        self.entry_guess.pack(pady=10)

        # Submit Button
        submit_button = tk.Button(
            root,
            text="Submit Guess",
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            relief=tk.RAISED,
            command=self.check_guess,
        )
        submit_button.pack(pady=10)

        # Feedback Label
        self.feedback = tk.Label(
            root,
            text="",
            font=("Arial", 14),
            bg="#f4f4f4",
            fg="#e74c3c",
        )
        self.feedback.pack(pady=10)

        # Footer
        footer = tk.Label(
            root,
            text="Developed by Rabuma",
            font=("Arial", 10, "italic"),
            bg="#2c3e50",
            fg="white",
            pady=10
        )
        footer.pack(fill=tk.X)

    def check_guess(self):
        # Retrieve the user's guess
        guess = self.entry_guess.get()

        # Validate input
        if not guess.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid number!")
            return

        guess = int(guess)
        self.attempts += 1

        # Check the guess
        if guess < self.random_number:
            self.feedback.config(text="Too low! Try again.", fg="#e74c3c")
        elif guess > self.random_number:
            self.feedback.config(text="Too high! Try again.", fg="#e74c3c")
        else:
            messagebox.showinfo(
                "Congratulations!",
                f"You guessed it right! The number was {self.random_number}.\nAttempts: {self.attempts}",
            )
            self.reset_game()

    def reset_game(self):
        # Reset the game after a win
        self.random_number = random.randint(1, 10)
        self.attempts = 0
        self.entry_guess.delete(0, tk.END)
        self.feedback.config(text="")


# Create the GUI application
root = tk.Tk()
game = GuessingGame(root)
root.mainloop()
