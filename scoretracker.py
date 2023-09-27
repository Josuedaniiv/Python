import tkinter as tk
from tkinter import ttk

score_player1 = 0
score_player2 = 0
sets = []
current_set = 1

def update_score(player, increment):
    global score_player1, score_player2

    if player == 1:
        score_player1 += increment
    elif player == 2:
        score_player2 += increment

    if score_player1 == 40 or score_player2 == 40:
        start_break()

    display_scores()

def start_break():
    print("¡Se ha iniciado un break de 3 minutos!")

def finish_break():
    print("¡El break ha finalizado!")

def reset_scores():
    global score_player1, score_player2, sets, current_set

    score_player1 = 0
    score_player2 = 0
    sets = []
    current_set = 1

    display_scores()
    display_sets()

def display_scores():
    label_player1.config(text=player1_name.get() + ": " + str(score_player1))
    label_player2.config(text=player2_name.get() + ": " + str(score_player2))

def add_set():
    sets.append((score_player1, score_player2))
    display_sets()

def display_sets():
    for child in frame_sets.winfo_children():
        child.destroy()

    for i, (set_score1, set_score2) in enumerate(sets):
        set_label = ttk.Label(frame_sets, text="Set {}: {} - {}".format(i+1, set_score1, set_score2))
        set_label.grid(row=i, column=0, padx=5, pady=5)

def increase_player1():
    update_score(1, 1)

def decrease_player1():
    update_score(1, -1)

def increase_player2():
    update_score(2, 1)

def decrease_player2():
    update_score(2, -1)

window = tk.Tk()

button_increase_player1 = tk.Button(window, text="+", command=increase_player1, font=("Arial", 16), width=5, bg="#00CC66")
button_increase_player1.grid(row=3, column=0, padx=10, pady=10)

button_decrease_player1 = tk.Button(window, text="-", command=decrease_player1, font=("Arial", 16), width=5, bg="#FF0000")
button_decrease_player1.grid(row=4, column=0, padx=10, pady=10)

button_increase_player2 = tk.Button(window, text="+", command=increase_player2, font=("Arial", 16), width=5, bg="#00CC66")
button_increase_player2.grid(row=3, column=1, padx=10, pady=10)

button_decrease_player2 = tk.Button(window, text="-", command=decrease_player2, font=("Arial", 16), width=5, bg="#FF0000")
button_decrease_player2.grid(row=4, column=1, padx=10, pady=10)

button_add_set = tk.Button(window, text="Agregar Set", command=add_set, font=("Arial", 16), width=15, bg="#3366FF")
button_add_set.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

button_start_break = tk.Button(window, text="Iniciar Break", command=start_break, font=("Arial", 16), width=15, bg="#FFCC00")
button_start_break.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

button_finish_break = tk.Button(window, text="Finalizar Break", command=finish_break, font=("Arial", 16), width=15, bg="#FFCC00")
button_finish_break.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

button_reset_scores = tk.Button(window, text="Reiniciar Puntajes", command=reset_scores, font=("Arial", 16), width=15, bg="#FFCC00")
button_reset_scores.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

label_player1 = ttk.Label(window, text="Player 1: 0", font=("Arial", 16))
label_player1.grid(row=1, column=0, padx=10, pady=10)

label_player2 = ttk.Label(window, text="Player 2: 0", font=("Arial", 16))
label_player2.grid(row=2, column=0, padx=10, pady=10)

frame_sets = ttk.Frame(window)
frame_sets.grid(row=1, column=1, rowspan=8, padx=10, pady=10)

window.mainloop()
