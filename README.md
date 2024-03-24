<h1> SECURE TRANSFER SYSTEM USING FERNET KEY </h1>


<h3> working of the code </h3>
* Create the Themed Tkinter Window: The main window is created using ThemedTk() from the ttkthemes module. This window is the main GUI container where all the widgets will be placed.

* Set Window Theme and Title: The theme of the window is set using window.set_theme("radiance"), and the title is set using window.title("Secure Text Sharing").

* Create and Configure GUI Elements: Various GUI elements like labels, text widgets, and buttons are created using ttk.Label, tk.Text, ttk.Entry, and ttk.Button. These elements are configured with specific properties like text, height, width, and command (for buttons).

* Pack GUI Elements: Each GUI element is packed using the pack() method, which makes them visible inside the window. Packing determines the placement and size of each element within the window.

* Define Callback Functions: Callback functions encrypt_text() and decrypt_text() are defined to handle the encryption and decryption processes when the corresponding buttons are clicked.

* Start the Main Loop: window.mainloop() starts the Tkinter event loop, which listens for events like button clicks, mouse movements, etc. This loop continues running until the window is closed by the user.

<h2>FERNET KEY </h2>

A Fernet key is a symmetric encryption key used in the Fernet symmetric encryption scheme. It's generated using a cryptographic algorithm and typically consists of 32 bytes (256 bits) of random data. The key is crucial for both encrypting and decrypting data securely.

To obtain a Fernet key, you can use the Fernet.generate_key() method provided by the cryptography library in Python. This method generates a random key each time it's called, ensuring strong encryption.

The Fernet key works on the principle of symmetric encryption, where the same key is used for both encryption and decryption. This means that anyone with the key can encrypt and decrypt data.

During encryption, the plaintext is combined with the Fernet key using a cryptographic algorithm, producing ciphertext that appears random and unintelligible without the key.

During decryption, the ciphertext is combined with the Fernet key using the same cryptographic algorithm in reverse, resulting in the original plaintext being recovered.

### photo
<img src = "Screenshot 2024-03-24 135531.png" width = "600px" >
