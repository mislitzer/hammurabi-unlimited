import tkinter as tk

class OutputPanel():
    def __init__(self, root):
        self.root = root
        self.panel = tk.Frame(self.root)
        self.panel.pack(side=tk.TOP)

        self.year = tk.Label(self.root)
        self.year.pack()

        self.population = tk.Label(self.root)
        self.population.pack()
        self.acres = tk.Label(self.root)
        self.acres.pack()
        self.store = tk.Label(self.root)
        self.store.pack()
        self.trade_value = tk.Label(self.root)
        self.trade_value.pack