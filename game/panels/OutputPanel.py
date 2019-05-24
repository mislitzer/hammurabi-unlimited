import tkinter as tk

class OutputPanel():
    def __init__(self, root):
        self.root = root
        self.panel = tk.Frame(self.root)
        self.panel.pack(side=tk.TOP, pady=40)
        self.additional_output_elements = []

        self.year = tk.Label(self.panel)
        self.year.pack()

        self.population = tk.Label(self.panel)
        self.population.pack()

        self.acres = tk.Label(self.panel)
        self.acres.pack()

        self.store = tk.Label(self.panel)
        self.store.pack()

        self.trade_value = tk.Label(self.panel)
        self.trade_value.pack()

    def clear_additional_labels(self):
        for add_output in self.additional_output_elements:
            add_output.destroy()

        self.additional_output_elements.clear()

    def add_additional_label(self, output):
        element = tk.Label(self.panel, text=output, font='Helvetica 14 bold')
        element.pack()
        self.additional_output_elements.append(element)