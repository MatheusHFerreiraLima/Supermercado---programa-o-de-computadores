import tkinter as tk
from tkinter import messagebox

# Tela de login

login = tk.Tk()
login.geometry("500x300")
login.title('Tela de Login')


def clique():
    email_digitado = email.get()
    senha_digitada = senha.get()

    if email_digitado == "supermercado@email.com" and senha_digitada == "sucesso":
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        login.destroy()
    else:
        messagebox.showerror("Erro", "Credenciais inválidas. Tente novamente.")


def limpar_email(event):
    if email.get() == "E-mail":
        email.delete(0, tk.END)
        email.config(fg='black')


def limpar_senha(event):
    if senha.get() == "Senha":
        senha.delete(0, tk.END)
        senha.config(fg='black')
        senha.config(show="*")


def preencher_email(event):
    if not email.get():
        email.insert(0, "E-mail")
        email.config(fg='grey')


def preencher_senha(event):
    if not senha.get():
        senha.insert(0, "Senha")
        senha.config(fg='grey')
        senha.config(show="")


texto = tk.Label(login, text="Fazer login", font=("heveltica", 18, "bold"))

email = tk.Entry(login, width=30, fg='grey')
email.insert(0, "E-mail")
email.bind("<FocusIn>", limpar_email)
email.bind("<FocusOut>", preencher_email)

senha = tk.Entry(login, width=30, fg='grey', show="")
senha.insert(0, "Senha")
senha.bind("<FocusIn>", limpar_senha)
senha.bind("<FocusOut>", preencher_senha)

botao = tk.Button(login, text="Login", command=clique, font=("Heveltica", 13, "bold"), background="royalblue",
                  foreground="white")

texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=5)
senha.pack(padx=10, pady=5)
botao.pack(padx=10, pady=10)

login.mainloop()
