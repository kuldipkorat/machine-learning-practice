import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",      
    user="root",  
    password="root",  
    database="pythoncrud"  
)
cursor = conn.cursor()

# Insert data
name = input("Enter the employee's name: ")
age = int(input("Enter the employee's age: "))
department = input("Enter the employee's department: ")

insert_query = "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)"
cursor.execute(insert_query, (name, age, department))
conn.commit()
print("Data inserted successfully!")

# Read data
cursor.execute("SELECT * FROM employees")
print("Current employees:")
for row in cursor.fetchall():
    print(row)

# Update data
name = input("Enter the employee's name: ")
new_department = input(f"Enter the new department for {name}: ")

update_query = "UPDATE employees SET department = %s WHERE name = %s"
cursor.execute(update_query, (new_department, name))
conn.commit()
print(f"{name}'s department updated successfully!")

# Read updated data
cursor.execute("SELECT * FROM employees")
print("Updated employees:")
for row in cursor.fetchall():
    print(row)

# Optionally delete data
name = input("Enter the employee's name: ")
delete_choice = input(f"Do you want to delete {name} from the database? (yes/no): ")
if delete_choice.lower() == 'yes':
    delete_query = "DELETE FROM employees WHERE name = %s"
    cursor.execute(delete_query, (name,))
    conn.commit()
    print(f"{name} has been deleted from the database.")

# Read final data
cursor.execute("SELECT * FROM employees")
print("Final employees list:")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
conn.close()
