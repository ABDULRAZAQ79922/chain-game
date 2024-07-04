import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Chain Game")
root.geometry("400x400")

sequence = [1, 2, 3, 4, 5]
current_index = 0

def check_button(number):
    global current_index
    if number == sequence[current_index]:
        current_index += 1
        buttons[number-1].config(state=tk.DISABLED, bg="green")
        if current_index == len(sequence):
            messagebox.showinfo("Congratulations!", "You completed the chain!")
            reset_game()
    else:
        messagebox.showwarning("Wrong!", "Wrong button! Try again.")
        reset_game()

def reset_game():
    global current_index
    current_index = 0
    for btn in buttons:
        btn.config(state=tk.NORMAL, bg="SystemButtonFace")

buttons = []
for i in range(1, 6):
    btn = tk.Button(root, text=f"Button {i}", font=("Helvetica", 14), command=lambda i=i: check_button(i))
    btn.pack(pady=10)
    buttons.append(btn)

root.mainloop()
