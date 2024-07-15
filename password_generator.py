import random
import string
import tkinter as tk


def generate_strong_password(length=16):
    if length < 12:
        raise ValueError("Password length should be at least 12 characters for better security.")

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password has at least one character from each set
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]

    # Fill the rest of the password length with random choices from all sets
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to avoid any patterns and convert it to a string
    random.shuffle(password)

    return ''.join(password)


def on_generate_button_click():
    password = generate_strong_password(16)
    password_label.config(text=f"Your generated password is:\n{password}")


def on_clear_button_click():
    password_label.config(text='')


# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x200")  # Adjusted dimensions to match the provided image
root.configure(bg='#f0f0f0')

# Commented out the icon image part
# Load and create an icon image (you need to have an image file named 'key_icon.png' in the same directory)
# icon_image = tk.PhotoImage(file="key_icon.png")
# icon_label = tk.Label(root, image=icon_image, bg='#f0f0f0')
# icon_label.pack(pady=10)

# Create and place the information label
info_label = tk.Label(root, text='To use the Password Generation Tool, click the button below.',
                      font=('Helvetica', 12), bg='#f0f0f0', fg='black')
info_label.pack(pady=10)

# Create and place the "Generate Password" button with minimal border width
generate_button = tk.Button(root, text="Generate Password", command=on_generate_button_click,
                            font=('Helvetica', 14, 'bold'), bg='#e0e0e0', fg='black', relief='raised',
                            activebackground='#d0d0d0', padx=20, pady=5, borderwidth=0)
generate_button.pack(pady=10)

# Create and place the "Clear Password" button with minimal border width
clear_button = tk.Button(root, text="Clear Password", command=on_clear_button_click,
                         font=('Helvetica', 14, 'bold'), bg='#e0e0e0', fg='black', relief='raised',
                         activebackground='#d0d0d0', padx=20, pady=5, borderwidth=0)
clear_button.pack(pady=10)

# Create a label to display the generated password
password_label = tk.Label(root, text='', font=('Helvetica', 12), bg='#f0f0f0', fg='black')
password_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
