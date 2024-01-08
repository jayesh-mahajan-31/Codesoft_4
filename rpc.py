import tkinter as tk
from tkinter import messagebox
import random

class Game:
    def __init__(self, window):
        self.window = window
        self.window.title("Stone Paper Scissor")

        self.window.geometry("600x400")

        self.user_score = 0
        self.computer_score = 0

        self.lbl = tk.Label(self.window, text="Choose Your Hand:", font=("Helvetica", 14))
        self.lbl.pack(pady=10)

        self.frame = tk.Frame(self.window)
        self.frame.pack()

        self.btn1 = tk.Button(self.frame, text="Stone", font=("Helvetica", 12), command=lambda: self.game_play('Stone'))
        self.btn1.grid(row=0, column=0, padx=5, pady=5)

        self.btn2 = tk.Button(self.frame, text="Paper", font=("Helvetica", 12), command=lambda: self.game_play('Paper'))
        self.btn2.grid(row=0, column=1, padx=5, pady=5)

        self.btn3 = tk.Button(self.frame, text="Scissor", font=("Helvetica", 12), command=lambda: self.game_play('Scissor'))
        self.btn3.grid(row=0, column=2, padx=5, pady=5)

        self.lbl_score = tk.Label(self.window, text="Score:", font=("Helvetica", 14))
        self.lbl_score.pack(pady=10)

        self.lbl_user_score = tk.Label(self.window, text="User: " + str(self.user_score), font=("Helvetica", 14))
        self.lbl_user_score.pack(pady=10)

        self.lbl_computer_score = tk.Label(self.window, text="Computer: " + str(self.computer_score), font=("Helvetica", 14))
        self.lbl_computer_score.pack(pady=10)

        self.reset_button = tk.Button(self.window, text="Reset Scores", font=("Helvetica", 12), command=self.reset_scores)
        self.reset_button.pack(pady=10)

    def game_play(self, player):
        hands = ['Stone', 'Paper', 'Scissor']
        computer = random.choice(hands)

        if player == computer:
            result = "It's a tie! You both chose " + player
        elif player == 'Stone':
            if computer == 'Paper':
                result = "Computer wins! Paper beats Stone."
                self.computer_score += 1
            else:
                result = "You win! Stone beats Scissor."
                self.user_score += 1
        elif player == 'Paper':
            if computer == 'Scissor':
                result = "Computer wins! Scissor beats Paper."
                self.computer_score += 1
            else:
                result = "You win! Paper beats Stone."
                self.user_score += 1
        else:
            if computer == 'Stone':
                result = "Computer wins! Stone beats Scissor."
                self.computer_score += 1
            else:
                result = "You win! Scissor beats Paper."
                self.user_score += 1

        self.lbl_user_score.config(text="User: " + str(self.user_score))
        self.lbl_computer_score.config(text="Computer: " + str(self.computer_score))

        messagebox.showinfo("Result", result)

    def reset_scores(self):
        self.user_score = 0
        self.computer_score = 0
        self.lbl_user_score.config(text="User: " + str(self.user_score))
        self.lbl_computer_score.config(text="Computer: " + str(self.computer_score))
        messagebox.showinfo("Scores Reset", "Scores have been reset to zero.")

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
