import sqlite3
import hashlib
import getpass
import sys

DB = "users.db"

def connect_db():
    conn = sqlite3.connect(DB)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        is_logged_in INTEGER NOT NULL DEFAULT 0
    )""")
    conn.commit()
    return conn

def hash_password(pwd: str) -> str:
    return hashlib.sha256(pwd.encode()).hexdigest()

def register(conn):
    user = input("Enter new username: ").strip()
    if not user:
        print("❌ Username can't be empty.")
        return
    cur = conn.execute("SELECT 1 FROM users WHERE username = ?", (user,))
    if cur.fetchone():
        print("❌ Username already taken.")
        return

    p1 = getpass.getpass("Enter password: ")
    p2 = getpass.getpass("Confirm password: ")
    if p1 != p2:
        print("❌ Passwords do not match.")
        return

    hp = hash_password(p1)
    conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, hp))
    conn.commit()
    print("✅ Registration successful.")

def login(conn):
    user = input("Username: ").strip()
    row = conn.execute(
        "SELECT password, is_logged_in FROM users WHERE username = ?", (user,)
    ).fetchone()
    if not row:
        print("❌ User not found.")
        return
    stored_hash, logged = row
    if logged:
        print("⚠  Already logged in elsewhere.")
        return

    pwd = getpass.getpass("Password: ")
    if hash_password(pwd) != stored_hash:
        print("❌ Incorrect password.")
        return

    conn.execute("UPDATE users SET is_logged_in = 1 WHERE username = ?", (user,))
    conn.commit()
    print(f"✅ '{user}' logged in successfully.")

def logout(conn):
    user = input("Username to logout: ").strip()
    row = conn.execute(
        "SELECT is_logged_in FROM users WHERE username = ?", (user,)
    ).fetchone()
    if not row:
        print("❌ User not found.")
        return
    if not row[0]:
        print("⚠  User is not logged in.")
        return

    conn.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (user,))
    conn.commit()
    print(f"✅ '{user}' logged out successfully.")

def change_password(conn):
    user = input("Username: ").strip()
    row = conn.execute(
        "SELECT password, is_logged_in FROM users WHERE username = ?", (user,)
    ).fetchone()
    if not row:
        print("❌ User not found.")
        return
    stored_hash, logged = row
    if not logged:
        print("⚠  User must be logged in to change password.")
        return

    current = getpass.getpass("Current password: ")
    if hash_password(current) != stored_hash:
        print("❌ Current password is incorrect.")
        return

    new1 = getpass.getpass("New password: ")
    new2 = getpass.getpass("Confirm new password: ")
    if new1 != new2:
        print("❌ New passwords do not match.")
        return

    new_h = hash_password(new1)
    conn.execute("UPDATE users SET password = ? WHERE username = ?", (new_h, user))
    conn.commit()
    print("✅ Password updated successfully.")

def main():
    conn = connect_db()
    menu = {
        "1": ("Register", register),
        "2": ("Login", login),
        "3": ("Logout", logout),
        "4": ("Change Password", change_password),
        "5": ("Exit", None)
    }

    while True:
        print("\n===== User Management =====")
        for key, (name, _) in menu.items():
            print(f"{key}. {name}")
        choice = input("Choose an action: ").strip()
        if choice not in menu:
            print("❌ Invalid option.")
            continue
        if choice == "5":
            print("👋 Goodbye!")
            conn.close()
            sys.exit()
        _, fn = menu[choice]
        fn(conn)

if __name__ == "_main_":
    main()