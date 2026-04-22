import tkinter as tk

from CTkListbox import CTkListbox

from calculator import calculate
from history import save_history, load_history
import customtkinter as ctk

class CalculatorApp:
    def __init__(self, root):

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(8):
            root.grid_rowconfigure(i, weight=1)
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("500x600")
        self.entry = ctk.CTkEntry(
            root,
            font=("Arial", 24),
            width=400,
            height=80,
            corner_radius=10,
            justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row, col = 1, 0
        for btn in buttons:
            if btn == '=':
                color = "#FF9500"  # оранжевый
                hover = "#FFB143"
            elif btn in '+-*/':
                color = "#505050"  # тёмно-серый оператор
                hover = "#686868"
            else:
                color = "#333333"  # цифры
                hover = "#4A4A4A"

            ctk.CTkButton(
                root,
                text=btn,
                width=100,
                height=60,
                corner_radius=8,
                fg_color=color,
                hover_color=hover,
                font=("Arial", 18),
                command=lambda b=btn: self.click(b)
            ).grid(row=row, column=col, padx=4, pady=4)
            col += 1
            if col > 3:
                col = 0
                row += 1

        ctk.CTkButton(
            root,
            text="History",
            command=self.show_history,
            corner_radius=8
        ).grid(row=row, column=0, columnspan=2, padx=4, pady=4)

        ctk.CTkButton(
            root,
            text="Clear",
            command=self.clear,
            fg_color="#D32F2F",
            hover_color="#E53935",
            corner_radius=8
        ).grid(row=row, column=2, columnspan=2, padx=4, pady=4)

        self.history_box = CTkListbox(
            root,
            width=400,
            height=80,
            corner_radius=12,
            border_width=2,
            fg_color="#1e1e1e",
            text_color="white",
            hover_color="#2a2a2a"
        )


        self.history_box.grid(row=row + 1, column=0, columnspan=4, pady=10, padx=10)
        self.history_box.bind("<<ListboxSelect>>", self.on_select)

    def click(self, btn):
        if btn == '=':
            expr = self.entry.get()
            result = calculate(expr)
            save_history(expr, result)

            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))

            self.show_history()  # 👈 добавь это
        else:
            self.entry.insert(tk.END, btn)

    def clear(self):
        self.entry.delete(0, tk.END)

    def show_history(self):
        self.history_box.delete(0, "end")
        for item in load_history():
            self.history_box.insert(tk.END, item)

    def on_select(self, event):
        selected = self.history_box.get()
        if selected:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, selected.split('=')[0].strip())



if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    app = CalculatorApp(root)
    root.mainloop()