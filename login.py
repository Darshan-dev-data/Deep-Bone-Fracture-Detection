import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import json
import os

# Get username from login.py
if len(sys.argv) > 1:
    logged_in_user = sys.argv[1]
else:
    logged_in_user = "Guest"

# File to store user data
USER_FILE = "users.json"
# Load users
def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)

# Save users
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

def login():
    username = entry_user.get()
    password = entry_pass.get()
    users = load_users()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login successful!")
        root.destroy()
        # Pass the username to mainGUI.py
        subprocess.run([sys.executable, "mainGUI.py", username])
    else:
        messagebox.showerror("Error", "Invalid username or password")


def open_register():
    reg_win = tk.Toplevel(root)
    reg_win.title("Register")
    reg_win.geometry("1200x1200")

    tk.Label(reg_win, text="New Username").pack(pady=5)
    reg_user = tk.Entry(reg_win)
    reg_user.pack()

    tk.Label(reg_win, text="New Password").pack(pady=5)
    reg_pass = tk.Entry(reg_win, show="*")
    reg_pass.pack()

    def register_user():
        new_user = reg_user.get()
        new_pass = reg_pass.get()
        users = load_users()

        if new_user in users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            users[new_user] = new_pass
            save_users(users)
            messagebox.showinfo("Success", "Registration successful!")
            reg_win.destroy()

    tk.Button(reg_win, text="Register", command=register_user).pack(pady=10)

# GUI setup
root = tk.Tk()
root.title("Login Page")
root.geometry("1200x1200")

tk.Label(root, text="Username").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack(pady=5)
tk.Button(root, text="Register", command=open_register).pack(pady=5)

root.mainloop()
