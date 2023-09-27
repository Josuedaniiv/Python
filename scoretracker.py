import tkinter as tk
from tkinter import ttk

class TennisScoreboard:
    def __init__(self):
        self.score_player1 = 0
        self.score_player2 = 0
        self.sets = []
        self.current_set = 1

        self.window = tk.Tk()
        self.window.title("Tennis Scoreboard")

        self.label_player1 = ttk.Label(self.window, text="Player 1: 0", font=("Arial", 16))
        self.label_player1.grid(row=1, column=0, padx=10, pady=10)

        self.label_player2 = ttk.Label(self.window, text="Player 2: 0", font=("Arial", 16))
        self.label_player2.grid(row=2, column=0, padx=10, pady=10)

        self.frame_sets = ttk.Frame(self.window)
        self.frame_sets.grid(row=1, column=1, rowspan=8, padx=10, pady=10)

        button_increase_player1 = tk.Button(self.window, text="+", command=self.increase_player1, font=("Arial", 16), width=5, bg="#00CC66")
        button_increase_player1.grid(row=3, column=0, padx=10, pady=10)

        button_decrease_player1 = tk.Button(self.window, text="-", command=self.decrease_player1, font=("Arial", 16), width=5, bg="#FF0000")
        button_decrease_player1.grid(row=4, column=0, padx=10, pady=10)

        button_increase_player2 = tk.Button(self.window, text="+", command=self.increase_player2, font=("Arial", 16), width=5, bg="#00CC66")
        button_increase_player2.grid(row=3, column=1, padx=10, pady=10)

        button_decrease_player2 = tk.Button(self.window, text="-", command=self.decrease_player2, font=("Arial", 16), width=5, bg="#FF0000")
        button_decrease_player2.grid(row=4, column=1, padx=10, pady=10)

        button_add_set = tk.Button(self.window, text="Agregar Set", command=self.add_set, font=("Arial", 16), width=15, bg="#3366FF")
        button_add_set.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        button_start_break = tk.Button(self.window, text="Iniciar Break", command=self.start_break, font=("Arial", 16), width=15, bg="#FFCC00")
        button_start_break.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        button_finish_break = tk.Button(self.window, text="Finalizar Break", command=self.finish_break, font=("Arial", 16), width=15, bg="#FFCC00")
        button_finish_break.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        button_reset_scores = tk.Button(self.window, text="Reiniciar Puntajes", command=self.reset_scores, font=("Arial", 16), width=15, bg="#FFCC00")
        button_reset_scores.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        self.display_scores()
        self.display_sets()

    def update_score(self, player, increment):
        if player == 1:
            self.score_player1 += increment
        elif player == 2:
            self.score_player2 += increment

        if self.score_player1 == 40 or self.score_player2 == 40:
            self.start_break()

        self.display_scores()

    def start_break(self):
        print("¡Se ha iniciado un break de 3 minutos!")

    def finish_break(self):
        print("¡El break ha finalizado!")

    def reset_scores(self):
        self.score_player1 = 0
        self.score_player2 = 0
        self.sets = []
        self.current_set = 1

        self.display_scores()
        self.display_sets()

    def display_scores(self):
        self.label_player1.config(text="Player 1: " + str(self.score_player1))
        self.label_player2.config(text="Player 2: " + str(self.score_player2))

    def add_set(self):
        self.sets.append((self.score_player1, self.score_player2))
        self.display_sets()

    def display_sets(self):
        for child in self.frame_sets.winfo_children():
            child.destroy()

        for i, (set_score1, set_score2) in enumerate(self.sets):
            set_label = ttk.Label(self.frame_sets, text="Set {}: {} - {}".format(i+1, set_score1, set_score2))
set_label.grid(row=i, column=0, padx=5, pady=5)

    def increase_player1(self):
        self.update_score(1, 1)

    def decrease_player1(self):
        self.update_score(1, -1)

    def increase_player2(self):
        self.update_score(2, 1)

    def decrease_player2(self):
        self.update_score(2, -1)

    def run(self):
        self.window.mainloop()

scoreboard = TennisScoreboard()
scoreboard.run()