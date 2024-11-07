#===================================
# IMPORTAÇÕES
#===================================

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

#===================================
# CLASSE REFERENTE AO BANCO DE DADOS
#===================================

'''!!• Definição de Estruturas de Dados: Estruturas bem definidas para produtos, categorias e movimentações.!!'''
class Produto:
# Inicialização da classe produto com todas colunas do banco de dados.
    def __init__(self, ID, Nome, Codigo=None, Preco=0.0, QntdAtual=0, Categoria=None, SubCategoria=None, 
                 Marca=None, Localizacao=None, QntdMin=None, QntdMax=None):
        self.ID = ID
        self.Nome = Nome
        self.Codigo = Codigo
        self.Preco = Preco
        self.QntdAtual = QntdAtual
        self.Categoria = Categoria
        self.SubCategoria = SubCategoria
        self.Marca = Marca
        self.Localizacao = Localizacao
        self.QntdMin = QntdMin
        self.QntdMax = QntdMax
# Função de chamada dos parâmetros 
    def __repr__(self):
        return (f"Produto(ID={self.ID}, Nome='{self.Nome}', Codigo='{self.Codigo}', Preco={self.Preco}, "
                f"QntdAtual={self.QntdAtual}, Categoria='{self.Categoria}', SubCategoria='{self.SubCategoria}', "
                f"Marca='{self.Marca}', Localizacao='{self.Localizacao}', QntdMin={self.QntdMin}, QntdMax={self.QntdMax})")

#===================================
# FUNÇÕES PARA O BANCO DE DADOS
#===================================
'''!!• Algoritmos de Cadastro e Consulta: Funções para cadastrar e consultar dados no sistema.!!'''

# Função para buscar produtos pelo nome
def buscar_produtos():
    nome = entry_nome.get()  # Obter o nome do produto digitado
    conn = sqlite3.connect('GerenciamentodeEstoque.db')
    cursor = conn.cursor()
    
    # Executar a consulta de busca com base no nome
    cursor.execute("SELECT * FROM 'GerenciamentodeEstoque' WHERE Nome LIKE ?", ('%' + nome + '%',))
    resultados = cursor.fetchall()
    
    # Limpar a lista atual
    for item in tree.get_children():
        tree.delete(item)
    
    # Inserir os resultados na interface
    for produto in resultados:
        tree.insert('', 'end', values=produto)
    
    conn.close()

# Função para abrir a janela de cadastro
def abrir_cadastro():
    cadastro_window = tk.Toplevel(root)
    cadastro_window.title("Cadastro de Produto")
    cadastro_window.geometry("400x400")
    
    # Campos para o cadastro
    tk.Label(cadastro_window, text="Nome").grid(row=0, column=0, padx=10, pady=5)
    entry_nome_cad = tk.Entry(cadastro_window)
    entry_nome_cad.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(cadastro_window, text="Codigo").grid(row=1, column=0, padx=10, pady=5)
    entry_codigo_cad = tk.Entry(cadastro_window)
    entry_codigo_cad.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(cadastro_window, text="Preço").grid(row=2, column=0, padx=10, pady=5)
    entry_preco_cad = tk.Entry(cadastro_window)
    entry_preco_cad.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(cadastro_window, text="Quantidade Atual").grid(row=3, column=0, padx=10, pady=5)
    entry_qntd_atual_cad = tk.Entry(cadastro_window)
    entry_qntd_atual_cad.grid(row=3, column=1, padx=10, pady=5)
    
    tk.Label(cadastro_window, text="Categoria").grid(row=4, column=0, padx=10, pady=5)
    entry_categoria_cad = tk.Entry(cadastro_window)
    entry_categoria_cad.grid(row=4, column=1, padx=10, pady=5)
    
    tk.Label(cadastro_window, text="SubCategoria").grid(row=5, column=0, padx=10, pady=5)
    entry_subcategoria_cad = tk.Entry(cadastro_window)
    entry_subcategoria_cad.grid(row=5, column=1, padx=10, pady=5)
    
    tk.Label(cadastro_window, text="Marca").grid(row=6, column=0, padx=10, pady=5)
    entry_marca_cad = tk.Entry(cadastro_window)
    entry_marca_cad.grid(row=6, column=1, padx=10, pady=5)
    
    tk.Label(cadastro_window, text="Localização").grid(row=7, column=0, padx=10, pady=5)
    entry_localizacao_cad = tk.Entry(cadastro_window)
    entry_localizacao_cad.grid(row=7, column=1, padx=10, pady=5)
    
    tk.Label(cadastro_window, text="Quantidade Mínima").grid(row=8, column=0, padx=10, pady=5)
    entry_qntd_min_cad = tk.Entry(cadastro_window)
    entry_qntd_min_cad.grid(row=8, column=1, padx=10, pady=5)
    
    tk.Label(cadastro_window, text="Quantidade Máxima").grid(row=9, column=0, padx=10, pady=5)
    entry_qntd_max_cad = tk.Entry(cadastro_window)
    entry_qntd_max_cad.grid(row=9, column=1, padx=10, pady=5)
    
    # Função para salvar o produto no banco de dados
    def salvar_produto():
        conn = sqlite3.connect('GerenciamentodeEstoque.db')
        cursor = conn.cursor()
        
        # Inserir os dados no banco de dados
        cursor.execute('''INSERT INTO 'GerenciamentodeEstoque' 
                          (Nome, Codigo, Preço, QntdAtual, Categoria, SubCategoria, Marca, Localização, QntdMin, QntdMax) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                       (entry_nome_cad.get(), entry_codigo_cad.get(), entry_preco_cad.get(), entry_qntd_atual_cad.get(),
                        entry_categoria_cad.get(), entry_subcategoria_cad.get(), entry_marca_cad.get(),
                        entry_localizacao_cad.get(), entry_qntd_min_cad.get(), entry_qntd_max_cad.get()))
        
        conn.commit()
        conn.close()
        
        # Mostrar mensagem de sucesso
        messagebox.showinfo("Cadastro", "Produto cadastrado com sucesso!")
        cadastro_window.destroy()
        buscar_produtos()  # Atualizar a lista de produtos na interface principal
    
    # Botão para salvar o cadastro
    btn_salvar = tk.Button(cadastro_window, text="Salvar", command=salvar_produto)
    btn_salvar.grid(row=10, column=0, columnspan=2, pady=10)

# Função para deletar produto
def deletar_produto():
    # Obter o item selecionado na Treeview
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Atenção", "Nenhum produto selecionado para exclusão.")
        return
    
    # Obter o ID do produto selecionado
    item_values = tree.item(selected_item, 'values')
    produto_id = item_values[0]  # Primeiro valor é o ID do produto
    
    # Confirmar exclusão
    resposta = messagebox.askyesno("Confirmação", "Deseja realmente deletar o produto selecionado?")
    if resposta:
        conn = sqlite3.connect('GerenciamentodeEstoque.db')
        cursor = conn.cursor()
        
        # Executar a exclusão no banco de dados
        cursor.execute("DELETE FROM 'GerenciamentodeEstoque' WHERE ID = ?", (produto_id,))
        conn.commit()
        conn.close()
        
        # Remover o item da Treeview
        tree.delete(selected_item)
        messagebox.showinfo("Exclusão", "Produto deletado com sucesso!")

# Função para editar produto
def editar_produto():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Atenção", "Nenhum produto selecionado para edição.")
        return
    
    item_values = tree.item(selected_item, 'values')
    produto_id = item_values[0]
    
    edit_window = tk.Toplevel(root)
    edit_window.title("Editar Produto")
    edit_window.geometry("400x400")
    
    # Campos de edição, preenchidos com os dados atuais do produto
    fields = ["Nome", "Codigo", "Preço", "QntdAtual", "Categoria", "SubCategoria", "Marca", "Localização", "QntdMin", "QntdMax"]
    entries = []
    
    for i, field in enumerate(fields):
        tk.Label(edit_window, text=field).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(edit_window)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, item_values[i + 1])  # Pulamos o ID
        entries.append(entry)
    
    # Função para salvar as alterações no banco de dados
    def salvar_edicao():
        conn = sqlite3.connect('GerenciamentodeEstoque.db')
        cursor = conn.cursor()
        
        # Atualizar os dados no banco de dados
        cursor.execute('''UPDATE 'GerenciamentodeEstoque' 
                          SET Nome=?, Codigo=?, Preço=?, QntdAtual=?, Categoria=?, SubCategoria=?, Marca=?, 
                              Localização=?, QntdMin=?, QntdMax=? 
                          WHERE ID=?''', 
                       (entries[0].get(), entries[1].get(), entries[2].get(), entries[3].get(),
                        entries[4].get(), entries[5].get(), entries[6].get(), entries[7].get(),
                        entries[8].get(), entries[9].get(), produto_id))
        
        conn.commit()
        conn.close()
        
        # Atualizar a Treeview e exibir mensagem de sucesso
        buscar_produtos()
        messagebox.showinfo("Edição", "Produto atualizado com sucesso!")
        edit_window.destroy()
    
    # Botão para salvar a edição
    btn_salvar = tk.Button(edit_window, text="Salvar", command=salvar_edicao)
    btn_salvar.grid(row=len(fields), column=0, columnspan=2, pady=10)

# Função referente as movimentações
def registrar_movimentacao():
    movimento_window = tk.Toplevel(root)
    movimento_window.title("Movimentação de Produto")
    movimento_window.geometry("400x400")

    def verificar_id():
        idmov = entry_id_cad.get()
        conn = sqlite3.connect('GerenciamentodeEstoque.db')
        cursor = conn.cursor()
        
        # Realiza a consulta ao banco de dados
        cursor.execute("SELECT * FROM 'GerenciamentodeEstoque' WHERE Id = ?", (idmov,))
        resultado = cursor.fetchone()
        conn.close()
        
        # Atualiza o texto do label com o nome do produto
        if resultado:
            label_produto.config(text=f"{resultado[1]}")  # Nome do produto
        else:
            label_produto.config(text="Produto não encontrado.")

    def realizar_movimentacao(tipo):
        idmov = entry_id_cad.get()
        quantidade_movimento = int(entry_quantidade.get())
        
        conn = sqlite3.connect('GerenciamentodeEstoque.db')
        cursor = conn.cursor()
        
        # Verificar se o produto existe e obter a quantidade atual
        cursor.execute("SELECT * FROM 'GerenciamentodeEstoque' WHERE Id = ?", (idmov,))
        resultado = cursor.fetchone()
        
        if resultado is None:
            conn.close()
            messagebox.showerror("Erro", "Produto não encontrado!")
            return

        quantidade_atual = resultado[4]  # Supondo que a coluna de quantidade seja a quinta coluna (índice 4)
        
        # Lógica de movimentação: "saída" diminui, "entrada" aumenta a quantidade
        if tipo == 'saída':
            if quantidade_atual >= quantidade_movimento:
                nova_quantidade = quantidade_atual - quantidade_movimento
            else:
                messagebox.showerror("Erro", "Quantidade insuficiente em estoque!")
                conn.close()
                return
        elif tipo == 'entrada':
            nova_quantidade = quantidade_atual + quantidade_movimento
        
        # Atualizar a quantidade na tabela GerenciamentodeEstoque
        cursor.execute("UPDATE GerenciamentodeEstoque SET QntdAtual = ? WHERE Id = ?", (nova_quantidade, idmov))
        
        # Registrar a movimentação na tabela Movimentacoes
        cursor.execute("INSERT INTO movimentacoes (IdProduto, Quantidade, TipodeTransacao, Data) VALUES (?, ?, ?, ?)", 
                       (idmov, quantidade_movimento, tipo, datetime.now()))
        
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Sucesso", f"{'Venda' if tipo == 'saída' else 'Adição'} realizada com sucesso!")

    # Interface da janela de movimentação
    tk.Label(movimento_window, text="Id do Produto").grid(row=0, column=0, padx=10, pady=5)
    entry_id_cad = tk.Entry(movimento_window)
    entry_id_cad.grid(row=0, column=1, padx=10, pady=5)

    # Botão para checar o ID do produto
    btn_checar = tk.Button(movimento_window, text="Checar", command=verificar_id)
    btn_checar.grid(row=0, column=2, columnspan=2, pady=10)
    
    # Label para mostrar o resultado da verificação
    label_produto = tk.Label(movimento_window, text="")
    label_produto.grid(row=1, column=0, columnspan=3)

    # Campo para quantidade a ser movimentada
    tk.Label(movimento_window, text="Quantidade a ser movimentada:").grid(row=2, column=0, padx=10, pady=5)
    entry_quantidade = tk.Entry(movimento_window)
    entry_quantidade.grid(row=2, column=1, padx=10, pady=5)

    # Botões para realizar a movimentação
    btn_vender = tk.Button(movimento_window, text="Venda", command=lambda: realizar_movimentacao('saída'))
    btn_vender.grid(row=3, column=0, padx=10, pady=5)

    btn_adicionar = tk.Button(movimento_window, text="Adicionar", command=lambda: realizar_movimentacao('entrada'))
    btn_adicionar.grid(row=3, column=1, padx=10, pady=5)

# Função para gerar relatórios
def gerar_relatorio():
    conn = sqlite3.connect('GerenciamentodeEstoque.db')
    cursor = conn.cursor()
    
    # Consultar todas as linhas da tabela GerenciamentodeEstoque
    print("Tabela: GerenciamentodeEstoque")
    cursor.execute("SELECT * FROM GerenciamentodeEstoque")
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)
    
    print("\nTabela: Movimentacoes")
    # Consultar todas as linhas da tabela Movimentacoes
    cursor.execute("SELECT * FROM movimentacoes")
    movimentacoes = cursor.fetchall()
    for movimentacao in movimentacoes:
        print(movimentacao)

    # Fechar a conexão com o banco de dados
    conn.close()

#===================================
#INTERFACE COM TKINTER
#===================================

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Gerenciamento de Estoque")
root.geometry("800x400")

# Campo de entrada para o nome do produto
label_nome = tk.Label(root, text="Nome do Produto:")
label_nome.pack(pady=10)
entry_nome = tk.Entry(root, width=50)
entry_nome.pack()

# Frame dos Botões
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

#Botões
btn_buscar = tk.Button(button_frame, text="Buscar", command=buscar_produtos)
btn_buscar.grid(row=0, column=0, padx=5)

btn_cadastrar = tk.Button(button_frame, text="Adicionar Produto", command=abrir_cadastro)
btn_cadastrar.grid(row=0, column=1, padx=5)

btn_editar = tk.Button(button_frame, text="Editar", command=editar_produto)
btn_editar.grid(row=0, column=2, padx=5)

btn_deletar = tk.Button(button_frame, text="Deletar", command=deletar_produto)
btn_deletar.grid(row=0, column=3, padx=5)

btn_vendas = tk.Button(button_frame, text="Vender", command=registrar_movimentacao)
btn_vendas.grid(row=0, column=4, padx=5)

btn_relatorio = tk.Button(button_frame, text="Relatório",command=gerar_relatorio)
btn_relatorio.grid(row=0, column=5, padx=5)
#===================================
#TABELA TREE-VIEW PARA VISUALIZAR BANCO DE DADOS
#===================================

# Frame para Tabela
tree_frame = tk.Frame(root)
tree_frame.pack(expand=True, fill='both')
# Configuração da tabela para exibir os produtos
columns = ('ID', 'Nome', 'Codigo', 'Preço', 'QntdAtual', 'Categoria', 'SubCategoria', 'Marca', 'Localização', 'QntdMin', 'QntdMax')
tree = ttk.Treeview(root, columns=columns, show='headings', height=15)
tree.pack(expand=True, fill='both', pady=10)
scroll_x = ttk.Scrollbar(tree_frame, orient='horizontal', command=tree.xview)
tree.configure(xscrollcommand=scroll_x.set)
scroll_x.pack(side='bottom', fill='x')

for col in columns:
    tree.heading(col, text=col)


root.mainloop()