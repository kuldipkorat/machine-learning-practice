import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",      # Your MySQL server host (e.g., "localhost")
    user="root",  # Your MySQL username
    password="root",  # Your MySQL password
    database="pythoncrud"  # Name of the database yo
)
cursor = conn.cursor()


# Insert data
insert_query = "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)"
cursor.execute(insert_query, ("John Doe", 28, "Engineering"))
conn.commit()

# Read data
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)

# Update data
update_query = "UPDATE employees SET department = %s WHERE name = %s"
cursor.execute(update_query, ("Human Resources", "John Doe"))
conn.commit()

cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)

# Delete data
# delete_query = "DELETE FROM employees WHERE name = %s"
# cursor.execute(delete_query, ("John Doe",))
# conn.commit()

# cursor.execute("SELECT * FROM employees")
# for row in cursor.fetchall():
#     print(row)
    
# Close connection
cursor.close()
conn.close()
