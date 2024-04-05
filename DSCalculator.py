import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

def calculate_daily_spending():
    total_money = float(entry_total_money.get())
    duration = int(entry_duration.get())
    daily_spending = total_money / duration

    planned_expenses = 0
    if include_planned_expenses.get() == 1:
        selected_period = combo_period.get()
        expense_amount = float(entry_expense.get())

        if selected_period == "Daily":
            planned_expenses += expense_amount * duration
        elif selected_period == "Weekly":
            planned_expenses += expense_amount * (duration // 7)
        elif selected_period == "Monthly":
            planned_expenses += expense_amount

    total_spending = daily_spending + (planned_expenses / duration) if include_planned_expenses.get() == 1 else daily_spending

    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, f"To have enough money for {duration} days, you need to spend {total_spending:.2f} per day.\n")
    
    if include_planned_expenses.get() == 1:
        result_text.insert(tk.END, f"Including planned expenses: {planned_expenses:.2f}")

root = tk.Tk()
root.title("Calculate Daily Spending")
root.geometry("400x500")  
root.resizable(False, False)

label_font = ('Arial', 12)
button_font = ('Arial', 12)
button_bg = '#4CAF50'
button_fg = 'white'
entry_bg = '#f0f0f0'

label_total_money = tk.Label(root, text="Total money:", font=label_font)
label_total_money.pack()

entry_total_money = tk.Entry(root, bg=entry_bg)
entry_total_money.pack()

label_duration = tk.Label(root, text="Duration (in days):", font=label_font)
label_duration.pack()

entry_duration = tk.Entry(root, bg=entry_bg)
entry_duration.pack()

label_period = tk.Label(root, text="Expense Periodicity:", font=label_font)
label_period.pack()

period_options = ["Daily", "Weekly", "Monthly"]
combo_period = ttk.Combobox(root, values=period_options)
combo_period.pack()

label_expense = tk.Label(root, text="Expense Amount:", font=label_font)
label_expense.pack()

entry_expense = tk.Entry(root, bg=entry_bg)
entry_expense.pack()

include_planned_expenses = tk.IntVar()
include_planned_expenses.set(0)  

planned_expenses_checkbox = tk.Checkbutton(root, text="Include Planned Expenses", variable=include_planned_expenses)
planned_expenses_checkbox.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_daily_spending, font=button_font, bg=button_bg, fg=button_fg)
calculate_button.pack(pady=10)  

result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, font=label_font)
result_text.pack()

root.mainloop()