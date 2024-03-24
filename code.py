
# Import necessary modules
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from cryptography.fernet import Fernet

# Function to handle text encryption
def encrypt_text():
    try:
        # Generate a Fernet key
        fernet_key = Fernet.generate_key()
        print(fernet_key)
        text = input_text.get("1.0", "end-1c")  # Get the input text from the Text widget
        cipher_suite = Fernet(fernet_key)  # Create a Fernet cipher suite
        encrypted_text = cipher_suite.encrypt(text.encode())  # Encrypt the text
        save_to_file(encrypted_text, 'encrypted_text.txt')  # Save the encrypted text to a file
        key_entry.delete(0, 'end')  # Clear the key entry field
        key_entry.insert(0, fernet_key.decode())  # Display the generated key
        output_text.delete("1.0", "end")  # Clear the output text field
        output_text.insert("1.0", "Text encrypted successfully.")  # Display a success message
    except Exception as e:
        output_text.delete("1.0", "end")  # Clear the output text field
        output_text.insert("1.0", f"Encryption error: {str(e)}")  # Display an error message if encryption fails

# Function to handle text decryption
def decrypt_text():
    secret_key = key_entry.get()  # Get the Fernet key from the entry field
    try:
        cipher_suite = Fernet(secret_key.encode())  # Create a Fernet cipher suite with the provided key
        encrypted_text = load_from_file('encrypted_text.txt')  # Load the encrypted text from a file
        decrypted_text = cipher_suite.decrypt(encrypted_text)  # Decrypt the text

        decrypted_output.delete("1.0", "end")  # Clear the decrypted text field
        decrypted_output.insert("1.0", decrypted_text.decode())  # Display the decrypted text
    except Exception as e:
        output_text.delete("1.0", "end")  # Clear the output text field
        output_text.insert("1.0", f"Decryption error: {str(e)}")  # Display an error message if decryption fails

# Function to save data to a file
def save_to_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)  # Write the data to the specified file

# Function to load data from a file
def load_from_file(filename):
    with open(filename, 'rb') as file:
        return file.read()  # Read and return the data from the specified file

# Create the main themed Tkinter window
window = ThemedTk()  # Create the main window with a theme
window.set_theme("radiance")  # Set the window theme
window.title("Secure Text Sharing")  # Set the window title

style = ttk.Style()  # Create a style for ttk widgets
style.configure("TLabel", foreground="black")  # Configure label text color
style.configure("TButton", foreground="black")  # Configure button text color

# Create and configure various GUI elements (labels, text widgets, buttons)
input_label = ttk.Label(window, text="Enter Text:")  # Create a label for the input text
input_label.pack()  # Display the input label in the window
input_text = tk.Text(window, height=5, width=40)  # Create a Text widget for entering text
input_text.pack()  # Display the input text widget in the window

key_label = ttk.Label(window, text="Generated Secret Key:")  # Create a label for displaying the generated key
key_label.pack()  # Display the key label in the window
key_entry = ttk.Entry(window)  # Create an entry field for displaying the key
key_entry.pack()  # Display the key entry field in the window

encrypt_button = ttk.Button(window, text="Encrypt", command=encrypt_text)  # Create an "Encrypt" button
decrypt_button = ttk.Button(window, text="Decrypt", command=decrypt_text)  # Create a "Decrypt" button
encrypt_button.pack()  # Display the "Encrypt" button in the window
decrypt_button.pack()  # Display the "Decrypt" button in the window

output_label = ttk.Label(window, text="Output:")  # Create a label for displaying output messages
output_label.pack()  # Display the output label in the window
output_text = tk.Text(window, height=5, width=40)  # Create a Text widget for displaying output messages
output_text.pack()  # Display the output text widget in the window

decrypted_label = ttk.Label(window, text="Decrypted Text:")  # Create a label for displaying decrypted text
decrypted_label.pack()  # Display the decrypted text label in the window
decrypted_output = tk.Text(window, height=5, width=40)  # Create a Text widget for displaying decrypted text
decrypted_output.pack()  #

#  Display the decrypted text widget in the window

window.mainloop()  # Start the Tkinter main loop for the main window
