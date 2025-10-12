from database import get_connection, init_db

def get_user(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, streak FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    return result  # returns (id, streak) if found, or None if not

def add_user(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, streak) VALUES (?, ?)", (name, 0))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return user_id

def check_in(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET streak = streak + 1 WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Welcome to Accountability Bot!")
    username = input("What’s your name? ").strip()

    user = get_user(username)
    if user is None:
        user_id = add_user(username)
        print(f"Nice to meet you, {username}! Let’s start your first streak day 🌱")
    else:
        user_id, streak = user
        print(f"Welcome back, {username}! Your current streak is {streak} days 🔥")
        check_in(user_id)
        print(f"✅ Checked in! New streak: {streak + 1}")