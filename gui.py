import tkinter as tk
from calculator import calculate
from history import save_history, load_history

class CalculatorApp:
    def __init__(self, root):
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(8):
            root.grid_rowconfigure(i, weight=1)
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.entry = tk.Entry(root, font=("Arial", 20), width=20)
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row, col = 1, 0
        for btn in buttons:
            tk.Button(root, text=btn, width=8, height=2,
                      command=lambda b=btn: self.click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        tk.Button(root, text="History", command=self.show_history).grid(row=row, column=0, columnspan=2)
        tk.Button(root, text="Clear", command=self.clear).grid(row=row, column=2, columnspan=2)

        self.history_box = tk.Listbox(root, width=45, height=6)
        self.history_box.grid(row=row + 1, column=0, columnspan=4, pady=10)

    def click(self, btn):
        if btn == '=':
            expr = self.entry.get()
            result = calculate(expr)
            save_history(expr, result)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        else:
            self.entry.insert(tk.END, btn)

    def clear(self):
        self.entry.delete(0, tk.END)

    def show_history(self):
        self.history_box.delete(0, tk.END)
        for item in load_history():
            self.history_box.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()