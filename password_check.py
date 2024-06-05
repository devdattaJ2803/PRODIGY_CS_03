import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain lowercase letters.")
    
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain uppercase letters.")
    
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain digits.")
    
    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for char in password):
        strength += 1
    else:
        feedback.append("Password should contain special characters.")

    return strength, feedback

def evaluate_password():
    password = password_entry.get()
    strength, feedback = check_password_strength(password)

    if strength == 5:
        result_label.config(text="Password Strength: Strong", fg="green")
    elif 3 <= strength < 5:
        result_label.config(text="Password Strength: Medium", fg="orange")
    else:
        result_label.config(text="Password Strength: Weak", fg="red")

    feedback_text.delete(1.0, tk.END)
    if feedback:
        feedback_text.insert(tk.END, "\n".join(feedback))
    else:
        feedback_text.insert(tk.END, "Your password is strong!")

# Create the main window
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x300")

# Create and place the widgets
tk.Label(root, text="Enter your password:", font=("Helvetica", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*", font=("Helvetica", 12), width=30)
password_entry.pack(pady=5)

tk.Button(root, text="Check Password", command=evaluate_password, font=("Helvetica", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=5)

feedback_text = tk.Text(root, height=5, width=50, wrap="word", font=("Helvetica", 10))
feedback_text.pack(pady=5)

# Run the main event loop
root.mainloop()
