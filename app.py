import os

# 1. Hardcoded credentials - Security Hotspot
def connect_to_db():
    username = "admin"  # Hardcoded credentials
    password = "password123"  # Hardcoded password
    print(f"Connecting to database with username: {username} and password: {password}")
    # Placeholder for database connection logic

# 2. SQL Injection vulnerability
def unsafe_query(user_input):
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    print(f"Executing query: {query}")
    # Imagine this query is executed on the database without sanitization

# 3. Path traversal vulnerability
def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        print(f"File content: {data}")

# 4. Use of insecure hashing algorithm - Security Hotspot
def hash_password(password):
    import hashlib
    hashed = hashlib.md5(password.encode()).hexdigest()  # MD5 is insecure
    print(f"MD5 hash of password: {hashed}")

if __name__ == "__main__":
    connect_to_db()
    unsafe_query("'; DROP TABLE users; --")
    read_file("../../etc/passwd")
    hash_password("my_secure_password")
