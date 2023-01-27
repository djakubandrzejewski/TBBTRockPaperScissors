from random import choice
from tkinter import Tk, Label, Button
available_choices = ["paper", "rock", "scissors", "lizard", "spock"]
def play(player, cpu):
    win_with = {"paper": "rock", "rock": "scissors", "scissors": "paper", "scissors": "lizard","lizard":"spock","spock":"rock","rock":"lizard", "paper":"spock","spock":"scissors","lizard": "spock"}
    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False


def play_cmd(player):
    global text_label
    cpu = choice(available_choices)
    is_user_winner = play(player, cpu)
    if is_user_winner is None:
        text_label.config(text="Tie! Try again!", fg="blue")
        print(cpu)
    elif is_user_winner:
        text_label.config(text="You win... Let's play again", fg="green")
        print(cpu)
    else:
        text_label.config(text="I win, I win!", fg="red")
        print(cpu)
root = Tk()
root.title("Rock, Paper, Scissors, Lizard, Spock")
root.geometry("250x200")
text_label = Label(root, font=40, text="Let's play paper, rock, scissors!")
text_label.pack()
Button(
    root, text="Papier", font=40, width=10, command=lambda: play_cmd("paper") 
).pack()
Button(
    root, text="Kamien", font=40, width=10, command=lambda: play_cmd("rock")
).pack()
Button(
    root, text="Nozyce", font=40, width=10, command=lambda: play_cmd("scissors")
).pack()
Button(
    root, text="Jaszczurka", font=40, width=10, command=lambda: play_cmd("lizard")
).pack()

Button(
    root, text="Spock", font=40, width=10, command=lambda: play_cmd("spock")
).pack()

root.mainloop()