import tkinter as tk
import tkinter.messagebox
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

# APP em funcionamento


janela = tk.Tk()
janela.title("Super Mercado System")
janela.geometry("800x600")

current_frame = None
total_label = None
total = 0
codigo_barras_entry = None
nome_entry = None
valor_entry = None

image = tk.PhotoImage(file="carrinho_compras.png")
image = image.subsample(5)


def inicio():
    global current_frame, total_label, total, codigo_barras_entry

    if current_frame:
        current_frame.destroy()

    current_frame = tk.Frame(janela)
    current_frame.pack(fill=tk.BOTH, expand=True)

    pagina_inicial = tk.Label(current_frame, text="Página Inicial", font=("Helvetica", 18, "bold"))
    pagina_inicial.pack(pady=20)

    # Label e Entry para o código de barras
    codigo_barras_label = tk.Label(current_frame, text="Código de Barras:")
    codigo_barras_label.pack()
    codigo_barras_entry = tk.Entry(current_frame)
    codigo_barras_entry.pack()

    # Label para aparecer NOME e VALOR do produto quando clicar em "Buscar Produto"
    nome_valor_produto = tk.Label(current_frame, text="")
    nome_valor_produto.place(x=250, y=250)

    # Botão para buscar o produto
    buscar_button = tk.Button(current_frame, text="Buscar Produto",
                              font=("HEveltica", 12, 'bold'),
                              foreground='white', background='limegreen',
                              command=buscar_produto)
    # Alocando a tecla ENTER no botão Buscar Produto
    janela.bind("<Return>", lambda event: buscar_produto())
    buscar_button.pack(pady=12)

    # Botão para o cadastro dos itens
    cadastro_itens_button = tk.Button(current_frame,
                                      text="Cadastrar um novo item",
                                      command=cadastro_itens)
    cadastro_itens_button.place(x=650, y=0)

    # Botão para realizar o pagamento
    # Carregar a imagem
    pagamento_button = tk.Button(current_frame, text="Realizar o pagamento",
                                 font=("Helvetica", 13, 'bold'),
                                 image=image,
                                 compound="right",
                                 background='limegreen',
                                 foreground='white',
                                 command=pagamento)
    pagamento_button.place(x=500, y=350)


    # Label para exibir o total
    if total_label:
        total_label.destroy()
    total_label = tk.Label(current_frame, text=f"R$ {total:.2f}", font=("Helvetica", 25, 'bold'), foreground='green')
    total_label.place(x=530, y=220)


def cadastro_itens():
    global current_frame, codigo_barras_entry, nome_entry, valor_entry

    if current_frame:
        current_frame.destroy()

    current_frame = tk.Frame(janela)
    current_frame.pack(fill=tk.BOTH, expand=True)

    label = tk.Label(current_frame, text="Cadastro de Itens", font=("Helvetica", 30))
    label.pack(pady=20)

    # Label e Entry para o código de barras
    codigo_barras_label = tk.Label(current_frame, text="Código de Barras:")
    codigo_barras_label.pack()
    codigo_barras_entry = tk.Entry(current_frame)
    codigo_barras_entry.pack()

    # Label e Entry para o nome do produto
    nome_label = tk.Label(current_frame, text="Nome do Produto:")
    nome_label.pack()
    nome_entry = tk.Entry(current_frame)
    nome_entry.pack()

    # Label e Entry para o valor do produto
    valor_label = tk.Label(current_frame, text="Valor do Produto:")
    valor_label.pack()
    valor_entry = tk.Entry(current_frame)
    valor_entry.pack()

    # Botão de envio
    submit_button = tk.Button(current_frame, text="Enviar", command=armazenar_dados)
    submit_button.pack(pady=10)

    button_home = tk.Button(current_frame, text="Página Inicial", font=("Italic", 20), bg="lightskyblue",
                            command=inicio)
    button_home.pack(pady=10)

    # Alocando o ESC no botão "Página Inicial"
    janela.bind('<Escape>', lambda event: inicio())


def armazenar_dados():
    global codigo_barras_entry, nome_entry, valor_entry

    codigo_barras = codigo_barras_entry.get()
    nome_produto = nome_entry.get()
    valor_produto = valor_entry.get().replace(',', '.')  # Substituir vírgula por ponto

    # Armazenar os dados no arquivo
    # O "a" é utilizado para acrescentar algo no .txt
    with open("produtos.txt", "a") as file:
        file.write(
            f"Código de Barras: {codigo_barras}, Nome do Produto: {nome_produto}, Valor do Produto: {valor_produto}\n")

    # Limpar os campos de entrada após o envio
    codigo_barras_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    valor_entry.delete(0, tk.END)


def buscar_produto():
    global total, codigo_barras_entry

    codigo_barras = codigo_barras_entry.get()

    # Limpar o campo de entrada
    codigo_barras_entry.delete(0, tk.END)

    # Buscar o produto pelo código de barras
    produto_encontrado = False
    with open("produtos.txt", "r") as arquivo:
        for line in arquivo:
            if f"Código de Barras: {codigo_barras}" in line:
                # Exibir o nome e o valor do produto na página inicial
                produto_info = line.split(", ")
                valor_produto = float(produto_info[2].split(": ")[1].replace(',', '.'))  # Substituir vírgula por ponto
                total += valor_produto
                produto_encontrado = True

    # Atualizar o label de total
    total_label.config(text=f"R$ {total:.2f}")

    if not produto_encontrado:
        tk.messagebox.showwarning("ERROR", "Produto não encontrado.")


def pagamento():
    global total

    total = 0
    total_label.config(text=f'R$ {total:.2f}')


if __name__ == "__main__":
    inicio()
    janela.mainloop()
