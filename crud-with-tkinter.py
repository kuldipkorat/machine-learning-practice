import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost", 
    user="root",  
    password="root",  
    database="pythoncrud"  
)
cursor = conn.cursor()

# Function to insert data into the database
def insert_data():
    name = entry_name.get()
    age = entry_age.get()
    department = entry_department.get()
    
    if name and age and department:
        insert_query = "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (name, age, department))
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully")
        load_data()
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields")

# Function to load data into the table
def load_data():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in tree.get_children():
        tree.delete(row)
    for row in rows:
        tree.insert("", tk.END, values=row)

# Function to delete selected data
def delete_data():
    selected_item = tree.selection()[0]
    delete_query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(delete_query, (tree.item(selected_item)['values'][0],))
    conn.commit()
    tree.delete(selected_item)
    messagebox.showinfo("Success", "Data deleted successfully")

# Function to update selected data
def update_data():
    selected_item = tree.selection()[0]
    id = tree.item(selected_item)['values'][0]
    name = entry_name.get()
    age = entry_age.get()
    department = entry_department.get()
    
    if name and age and department:
        update_query = "UPDATE employees SET name = %s, age = %s, department = %s WHERE id = %s"
        cursor.execute(update_query, (name, age, department, id))
        conn.commit()
        load_data()
        messagebox.showinfo("Success", "Data updated successfully")
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields")

# Function to populate input fields when selecting a row
def on_row_select(event):
    selected_item = tree.selection()[0]
    selected_data = tree.item(selected_item)['values']
    entry_name.delete(0, tk.END)
    entry_name.insert(0, selected_data[1])
    entry_age.delete(0, tk.END)
    entry_age.insert(0, selected_data[2])
    entry_department.delete(0, tk.END)
    entry_department.insert(0, selected_data[3])

# GUI Setup
root = tk.Tk()
root.title("CRUD App")

# Input Fields
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=10)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Department").grid(row=2, column=0, padx=10, pady=10)
entry_department = tk.Entry(root)
entry_department.grid(row=2, column=1, padx=10, pady=10)

# Buttons
tk.Button(root, text="Insert", command=insert_data).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Update", command=update_data).grid(row=3, column=1, padx=10, pady=10)
tk.Button(root, text="Delete", command=delete_data).grid(row=3, column=2, padx=10, pady=10)

# Treeview Table
columns = ("ID", "Name", "Age", "Department")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Bind the selection event
tree.bind('<<TreeviewSelect>>', on_row_select)

# Load data into the table
load_data()

root.mainloop()

# Close the connection when the app is closed
conn.close()
