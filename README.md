# Expense-tracker-
Developed a simple expense tracker using python and its frameworks 
# Personal Expense Tracker

A simple yet effective desktop application built with Python and Tkinter to help you manage your personal expenses. Track your spending, categorize expenses, and stay on top of your finances with an easy-to-use interface.

![Screenshot of Expense Tracker (Optional: Add a screenshot of your application here if you have one)]
*(Optional: If you add a screenshot, name it e.g., `expense_tracker_screenshot.png` and place it in your repository. Then you can use the markdown `![Screenshot Name](expense_tracker_screenshot.png)`)*

## 🌟 Features

* **Add Expenses:** Easily record new expenses with amount, category, date, and a description.
* **View Expenses:** Displays all recorded expenses in a clear, sortable table (sorted by date by default).
* **Update Expenses:** Select an expense from the table to load its details into the form for easy modification.
* **Delete Expenses:** Remove unwanted or incorrect expense entries with a confirmation step.
* **Input Validation:** Ensures data integrity with checks for valid amounts, category selection, and date formats.
* **Pre-defined Categories:** Includes common expense categories (Food, Transport, Shopping, Bills, Entertainment, Other) via a dropdown menu.
* **Automatic Date Population:** Defaults the date field to the current day for quicker entry.
* **Total Expenses Display:** Shows a running total of all recorded expenses.
* **Export to CSV:** Export all your expense data to a CSV file for backup or further analysis in spreadsheet software.
* **User-Friendly Interface:** Clean and intuitive GUI built with Tkinter's themed widgets (`ttk`).

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **GUI Framework:** Tkinter (`ttk` for themed widgets)
* **Database:** SQLite 3 (for local data storage)
* **Standard Libraries:**
    * `csv` (for CSV export functionality)
    * `datetime` (for date handling)
    * `messagebox` (from Tkinter for alerts and confirmations)
    * `filedialog` (from Tkinter for save file dialog)

## 🚀 Setup and Usage

1.  **Prerequisites:**
    * Python 3 installed on your system. (Tkinter and SQLite3 are usually included with standard Python installations).

2.  **Clone the repository (Optional, if you're sharing it):**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

3.  **Run the application:**
    Execute the main Python script (e.g., `expense_tracker.py` or whatever you've named your main file):
    ```bash
    python your_main_script_name.py
    ```
    A `expenses.db` file will be automatically created in the same directory to store your expense data.

## 💡 How to Use

1.  **Adding an Expense:**
    * Fill in the "Amount", select a "Category", verify the "Date", and add a "Description".
    * Click the "Add Expense" button.
2.  **Updating an Expense:**
    * Click on an expense row in the table. The details will populate the input fields.
    * Modify the details as needed.
    * Click the "Update Selected" button.
3.  **Deleting an Expense:**
    * Click on an expense row in the table.
    * Click the "Delete Selected" button. A confirmation prompt will appear.
4.  **Exporting Data:**
    * Click the "Export to CSV" button.
    * Choose a location and filename for your CSV file.

## 🌱 Future Enhancements (Ideas)

* [ ] Filtering expenses by category or date range.
* [ ] Sorting data by different columns (Amount, Category) directly in the Treeview.
* [ ] Visualizations/Charts (e.g., a pie chart of expenses by category).
* [ ] More robust date picker widget.
* [ ] User-defined categories.
* [ ] Basic reporting features (e.g., monthly summaries).

## 🙏 Acknowledgements

* This project serves as a practical application of Python, Tkinter, and SQLite for managing personal finances.

---

*(Optional: Add a License section if you wish, e.g., MIT License)*
