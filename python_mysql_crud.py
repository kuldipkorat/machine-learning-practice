import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pythoncrud"
)
cursor = conn.cursor()

def check_roll_no_exists(roll_no):
    cursor.execute("SELECT COUNT(*) FROM students WHERE roll_no = %s", (roll_no,))
    return cursor.fetchone()[0] > 0

# Insert data
def insert_data():
    roll_no = int(input("Enter the student's roll number: "))
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    city = input("Enter the student's city: ")

    if check_roll_no_exists(roll_no):
        print("Error: A student with this roll number already exists.")
    else:
        insert_query = "INSERT INTO students (roll_no, name, age, city) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (roll_no, name, age, city))
        conn.commit()
        print("Data inserted successfully!")

# Read data
def read_data():
    cursor.execute("SELECT * FROM students")
    print("Current students:")
    for row in cursor.fetchall():
        print(row)

# Update data
def update_data():
    roll_no = int(input("Enter the student's roll number: "))
    
    if not check_roll_no_exists(roll_no):
        print("Error: No student found with this roll number.")
    else:
        new_city = input(f"Enter the new city for roll number {roll_no}: ")
        update_query = "UPDATE students SET city = %s WHERE roll_no = %s"
        cursor.execute(update_query, (new_city, roll_no))
        conn.commit()
        print("Student details updated successfully!")

# Delete data
def delete_data():
    roll_no = int(input("Enter the student's roll number: "))

    if not check_roll_no_exists(roll_no):
        print("Error: No student found with this roll number.")
    else:
        delete_choice = input(f"Do you want to delete the student with roll number {roll_no}? (yes/no): ")
        if delete_choice.lower() == 'yes':
            delete_query = "DELETE FROM students WHERE roll_no = %s"
            cursor.execute(delete_query, (roll_no,))
            conn.commit()
            print("Student has been deleted from the database.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Insert Data")
    print("2. Read Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        insert_data()
    elif choice == '2':
        read_data()
    elif choice == '3':
        update_data()
    elif choice == '4':
        delete_data()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

# Close connection
cursor.close()
conn.close()
