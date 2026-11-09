import tkinter as tk
from tkinter import ttk, messagebox
from encryptie import encrypt_text, decrypt_text
from cryptography.exceptions import InvalidTag

root = tk.Tk()
root.title("Text Encryptor")
root.geometry("600x600")

title_label = ttk.Label(root, text="Encryptie", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

input_label = ttk.Label(root, text="Voer je tekst in:")
input_label.pack()

input_text = tk.Text(root, height=5, width=60)
input_text.pack(pady=10)

password_label = ttk.Label(root, text="Wachtwoord:")
password_label.pack()

password_entry = ttk.Entry(root, show="*", width=40)
password_entry.pack(pady=10)

def encrypt():
    text = input_text.get("1.0", tk.END).strip()
    password = password_entry.get()

    if not text or not password:
        messagebox.showwarning("Waarschuwing", "Vul tekst en een wachtwoord in.")
        return

    encrypted = encrypt_text(text, password)

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, encrypted)


def decrypt():
    text = input_text.get("1.0", tk.END).strip()
    password = password_entry.get()

    if not text or not password:
        messagebox.showwarning("Waarschuwing", "Vul tekst en een wachtwoord in.")
        return

    try:
        decrypted = decrypt_text(text, password)

        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, decrypted)

    except (ValueError, UnicodeError, InvalidTag):
        messagebox.showerror(
            "Fout",
            "Ontsleutelen mislukt. Controleer je wachtwoord en versleutelde tekst."
        )


encrypt_button = ttk.Button(root, text="Versleutelen", command=encrypt)
encrypt_button.pack(pady=5)

decrypt_button = ttk.Button(root, text="Ontsleutelen", command=decrypt)
decrypt_button.pack(pady=5)

result_label = ttk.Label(root, text="Resultaat:")
result_label.pack(pady=10)

result_text = tk.Text(root, height=5, width=60)
result_text.pack(pady=10)

root.mainloop()