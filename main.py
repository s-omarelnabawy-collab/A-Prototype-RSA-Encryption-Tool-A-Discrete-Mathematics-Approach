import tkinter as tk
from tkinter import ttk, messagebox
import rsa as rsa


def handle_encrypt():
    try:
        p_input = entry_p.get()
        q_input = entry_q.get()
        p = int(p_input)
        q = int(q_input)

        msg = entry_msg.get()

        n = p * q
        phi = (p - 1) * (q - 1)

        e = 65537
        candidates = [65537, 3, 5, 7, 11, 13, 17]

        for c in candidates:
            common_factor = rsa.gcd(c, phi)
            if common_factor == 1:
                e = c
                break

        d = rsa.mod_inverse(e, phi)
        cipher = rsa.encrypt(msg, e, n)

        result_text.delete(1.0, tk.END)

        display_content = f"Ciphertext: {cipher}\n\nPrivate Key (d): {d}\nModulus (n): {n}"
        result_text.insert(tk.END, display_content)

    except Exception as error:
        messagebox.showerror("Error", f"Invalid Input: {error}")


def handle_decrypt():
    try:
        cipher_input = entry_cipher.get()
        cipher_list = eval(cipher_input)

        d_input = entry_d.get()
        n_input = entry_n.get()

        d_val = int(d_input)
        n_val = int(n_input)

        plain_result = rsa.decrypt(cipher_list, d_val, n_val)

        messagebox.showinfo("Decrypted Message", f"Original Message: {plain_result}")
    except Exception as error:
        messagebox.showerror("Error", "Check your inputs (Ciphertext must be a list)")


root = tk.Tk()
root.title("RSA Encryption Suite - Discrete Math Project")
root.geometry("500x500")

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

encrypt_frame = ttk.Frame(notebook)
notebook.add(encrypt_frame, text="Encryption")

label_title_enc = tk.Label(encrypt_frame, text="Key Generation & Encryption", font=('Arial', 12, 'bold'))
label_title_enc.pack(pady=10)

label_p = tk.Label(encrypt_frame, text="Enter Prime P:")
label_p.pack()
entry_p = tk.Entry(encrypt_frame, width=30)
entry_p.pack(pady=5)

label_q = tk.Label(encrypt_frame, text="Enter Prime Q:")
label_q.pack()
entry_q = tk.Entry(encrypt_frame, width=30)
entry_q.pack(pady=5)

label_m = tk.Label(encrypt_frame, text="Message to Encrypt:")
label_m.pack()
entry_msg = tk.Entry(encrypt_frame, width=30)
entry_msg.pack(pady=5)

btn_encrypt = tk.Button(encrypt_frame, text="Generate & Encrypt", command=handle_encrypt, bg="#2ecc71", fg="white", width=20)
btn_encrypt.pack(pady=10)

result_text = tk.Text(encrypt_frame, height=8, width=45)
result_text.pack(pady=5)

decrypt_frame = ttk.Frame(notebook)
notebook.add(decrypt_frame, text="Decryption")

label_title_dec = tk.Label(decrypt_frame, text="Decrypt Ciphertext", font=('Arial', 12, 'bold'))
label_title_dec.pack(pady=10)

label_c = tk.Label(decrypt_frame, text="Enter Ciphertext (e.g. [12, 45]):")
label_c.pack()
entry_cipher = tk.Entry(decrypt_frame, width=40)
entry_cipher.pack(pady=5)

label_d = tk.Label(decrypt_frame, text="Enter Private Key (d):")
label_d.pack()
entry_d = tk.Entry(decrypt_frame, width=40)
entry_d.pack(pady=5)

label_n = tk.Label(decrypt_frame, text="Enter Modulus (n):")
label_n.pack()
entry_n = tk.Entry(decrypt_frame, width=40)
entry_n.pack(pady=5)

btn_decrypt = tk.Button(decrypt_frame, text="Decrypt Message", command=handle_decrypt, bg="#3498db", fg="white", width=20)
btn_decrypt.pack(pady=20)

root.mainloop()