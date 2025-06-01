import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv
from datetime import datetime

DB_NAME = "expenses.db"

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.create_db()
        self.create_widgets()
        self.load_expenses()

    def create_db(self):
        """Create SQLite database and expenses table if not exists"""
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT
            )
        ''')
        self.conn.commit()

    def create_widgets(self):
        """Setup all UI elements"""

        # Top frame for input form
        frame = ttk.Frame(self.root)
        frame.pack(pady=10, padx=10, fill='x')

        ttk.Label(frame, text="Amount:").grid(row=0, column=0, sticky='w')
        self.amount_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.amount_var, width=15).grid(row=0, column=1, sticky='w')

        ttk.Label(frame, text="Category:").grid(row=0, column=2, sticky='w', padx=(10,0))
        self.category_var = tk.StringVar()
        ttk.Combobox(frame, textvariable=self.category_var, values=[
            "Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"
        ], state="readonly", width=17).grid(row=0, column=3, sticky='w')

        ttk.Label(frame, text="Date (YYYY-MM-DD):").grid(row=0, column=4, sticky='w', padx=(10,0))
        self.date_var = tk.StringVar(value=datetime.today().strftime("%Y-%m-%d"))
        ttk.Entry(frame, textvariable=self.date_var, width=15).grid(row=0, column=5, sticky='w')

        ttk.Label(frame, text="Description:").grid(row=1, column=0, sticky='w', pady=(5,0))
        self.desc_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.desc_var, width=65).grid(row=1, column=1, columnspan=5, sticky='w', pady=(5,0))

        # Buttons
        ttk.Button(frame, text="Add Expense", command=self.add_expense).grid(row=2, column=0, pady=10)
        ttk.Button(frame, text="Update Selected", command=self.update_expense).grid(row=2, column=1, pady=10)
        ttk.Button(frame, text="Delete Selected", command=self.delete_expense).grid(row=2, column=2, pady=10)
        ttk.Button(frame, text="Export to CSV", command=self.export_csv).grid(row=2, column=3, pady=10)

        # Expense list table
        columns = ("ID", "Amount", "Category", "Date", "Description")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col)
            # Adjust column widths
            if col == "Description":
                self.tree.column(col, width=200)
            elif col == "ID":
                self.tree.column(col, width=40)
            else:
                self.tree.column(col, width=100)
        self.tree.pack(padx=10, fill='x')
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Label for total expenses
        self.total_label = ttk.Label(self.root, text="Total Expenses: $0.00", font=("Helvetica", 14, "bold"))
        self.total_label.pack(pady=10)

    def load_expenses(self):
        """Load expenses from DB into the Treeview"""
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
        rows = self.cursor.fetchall()
        total = 0
        for r in rows:
            self.tree.insert("", "end", values=r)
            total += r[1]

        self.total_label.config(text=f"Total Expenses: ${total:.2f}")

    def add_expense(self):
        """Add new expense to DB"""
        try:
            amount = float(self.amount_var.get())
            if amount <= 0:
                raise ValueError("Amount must be positive.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number for amount.")
            return

        category = self.category_var.get()
        if not category:
            messagebox.showerror("Invalid Input", "Please select a category.")
            return

        date = self.date_var.get()
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Input", "Date must be in YYYY-MM-DD format.")
            return

        description = self.desc_var.get()

        self.cursor.execute("INSERT INTO expenses (amount, category, date, description) VALUES (?, ?, ?, ?)",
                            (amount, category, date, description))
        self.conn.commit()
        self.load_expenses()
        self.clear_form()

    def update_expense(self):
        """Update selected expense"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an expense to update.")
            return

        item = self.tree.item(selected[0])
        expense_id = item["values"][0]

        try:
            amount = float(self.amount_var.get())
            if amount <= 0:
                raise ValueError("Amount must be positive.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number for amount.")
            return

        category = self.category_var.get()
        if not category:
            messagebox.showerror("Invalid Input", "Please select a category.")
            return

        date = self.date_var.get()
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Input", "Date must be in YYYY-MM-DD format.")
            return

        description = self.desc_var.get()

        self.cursor.execute(
            "UPDATE expenses SET amount=?, category=?, date=?, description=? WHERE id=?",
            (amount, category, date, description, expense_id))
        self.conn.commit()
        self.load_expenses()
        self.clear_form()

    def delete_expense(self):
        """Delete selected expense"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an expense to delete.")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected expense?")
        if not confirm:
            return

        item = self.tree.item(selected[0])
        expense_id = item["values"][0]

        self.cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
        self.conn.commit()
        self.load_expenses()
        self.clear_form()

    def clear_form(self):
        """Clear input fields"""
        self.amount_var.set("")
        self.category_var.set("")
        self.date_var.set(datetime.today().strftime("%Y-%m-%d"))
        self.desc_var.set("")
        self.tree.selection_remove(self.tree.selection())

    def on_tree_select(self, event):
        """Load selected expense into form for editing"""
        selected = self.tree.selection()
        if not selected:
            return
        item = self.tree.item(selected[0])
        _, amount, category, date, description = item["values"]

        self.amount_var.set(str(amount))
        self.category_var.set(category)
        self.date_var.set(date)
        self.desc_var.set(description)

    def export_csv(self):
        """Export all expenses to CSV file"""
        self.cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
        rows = self.cursor.fetchall()
        if not rows:
            messagebox.showinfo("No Data", "No expenses to export.")
            return

        default_filename = f"expenses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            initialfile=default_filename,
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )

        if not file_path:
            return  # user cancelled

        try:
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Amount", "Category", "Date", "Description"])
                writer.writerows(rows)
            messagebox.showinfo("Export Success", f"Expenses exported to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Export Failed", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
