import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Helvetica", 20), bd=15, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for i in range(4):
    for j in range(4):
        button = tk.Button(root, text=buttons[i][j], font=("Arial", 20), padx=30, pady=30)
        button.grid(row=i+1, column=j)
        button.bind("<Button-1>", on_button_click)

root.mainloop()
