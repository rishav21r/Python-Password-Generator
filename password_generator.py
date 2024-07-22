#!/opt/anaconda3/bin/python
import random
import string
import customtkinter as ctk

def generate_strong_password(length=16):
    if length < 12:
        raise ValueError("Password length should be at least 12 characters for better security.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]

    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

def on_generate_button_click():
    password = generate_strong_password(16)
    password_label.configure(text=f"{password}")

def on_clear_button_click():
    password_label.configure(text='')

# Set the appearance mode and color theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Create the main application window
root = ctk.CTk()
root.title("Password Generator")
root.geometry("400x200")

# Create and place the information label
info_label = ctk.CTkLabel(root, text='To use the Password Generation Tool, click the button below.',
                          font=('Georgia', 12))
info_label.pack(pady=10)

# Create and place the "Generate Password" button
generate_button = ctk.CTkButton(root, text="Generate Password", command=on_generate_button_click,
                                font=('Georgia', 14))
generate_button.pack(pady=10)

# Create and place the "Clear Password" button
clear_button = ctk.CTkButton(root, text="Clear Password", command=on_clear_button_click,
                             font=('Georgia', 14))
clear_button.pack(pady=10)

# Create a label to display the generated password
password_label = ctk.CTkLabel(root, text='', font=('Georgia', 12))
password_label.pack(pady=10)

# Start the customtkinter event loop
root.mainloop()