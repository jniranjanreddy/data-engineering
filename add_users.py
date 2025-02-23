import json
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(host="localhost", user="devops", password="password", database="mydb")
cursor = conn.cursor()

# Create table (if not exists)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
""")

# Load JSON file
with open('data.json') as f:
    data = json.load(f)

# Insert data
for record in data:
    cursor.execute("INSERT INTO users (id, name, age) VALUES (%s, %s, %s)", 
                   (record['id'], record['name'], record['age']))

# Commit and close
conn.commit()
conn.close()


