from database import get_connection, init_db

def add_user(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, streak) VALUES (?, ?)", (name, 0))
    conn.commit()
    conn.close()

def check_in(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET streak = streak + 1 WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Welcome to Accountability Bot!")
    username = input("What’s your name? ")
    add_user(username)
    print(f"Nice to meet you, {username}! Let's beat procrastination!")