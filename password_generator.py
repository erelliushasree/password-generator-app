import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())  # Get password length
    charset = ""

    # Check which types of characters to include
    if uppercase_var.get():
        charset += string.ascii_uppercase
    if lowercase_var.get():
        charset += string.ascii_lowercase
    if numbers_var.get():
        charset += string.digits
    if special_var.get():
        charset += string.punctuation

    # If no character type is selected, show a warning
    if not charset:
        messagebox.showwarning("Warning", "Please select at least one character type!")
        return

    # Generate the password by choosing random characters from the pool
    password = ''.join(random.choice(charset) for _ in range(length))
    password_entry.delete(0, tk.END)  # Clear the entry widget
    password_entry.insert(0, password)  # Insert the generated password

# Function to copy password to clipboard
def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Set up the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x400")
window.resizable(False, False)

# Password length label and entry
length_label = tk.Label(window, text="Password Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(window)
length_entry.pack(pady=5)
length_entry.insert(0, "12")

# Checkboxes for character types
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(window, text="Include Uppercase", variable=uppercase_var).pack()
tk.Checkbutton(window, text="Include Lowercase", variable=lowercase_var).pack()
tk.Checkbutton(window, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(window, text="Include Special Characters", variable=special_var).pack()

# Generate password button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Entry for displaying the generated password
password_entry = tk.Entry(window, width=30, font=("Arial", 14))
password_entry.pack(pady=10)

# Copy button
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Run the Tkinter loop
window.mainloop()
