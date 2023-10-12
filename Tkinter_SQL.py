import tkinter.messagebox
from tkinter import *
import pyodbc

# Integração com Banco de Dados
dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                 "Server=localhost;"
                 "Database=TkinterCRUD.db")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()


def btn_clicked0(): #procurar insumo
    # pegar a informação do campo nome_insumo (entry1)
    nome_insumo = entry1.get()

    # buscar essa informação do insumo no banco de dados
    comando = f"""SELECT * from Insumos
                WHERE nome_insumo = '{nome_insumo}';
                """
    cursor.execute(comando)
    # print(cursor.fetchall()) #[(1, 'garrafa', '31/12/2050', 1, 9375.0)]
    entry0.delete("1.0","end") #limpa a caixa de texto

    # colocar na caixa de texto (entry0) as informações do insumo no banco de dados
    for linha in cursor.fetchall():
        texto = f"Item: {linha.nome_insumo}\nQuantidade: {linha.quantidade}\nLote:{linha.lote}\nValidade:{linha.data_validade}" #aqui conseguimos referenciar os nomes das colunas por eles vieram do cursor
        entry0.insert("1.0", texto)

    entry1.delete("0", "end")  # limpa o campo
    print("Procurar Insumo")

def btn_clicked1(): #deletar insumo
    # pegar a informação do campo nome_insumo (entry1)
    nome_insumo = entry1.get()

    # buscar e deletar a informação do insumo no banco de dados
    comando = f"""DELETE from Insumos
                WHERE nome_insumo = '{nome_insumo}';
                """
    cursor.execute(comando)
    cursor.commit()

    # exibir uma mensagem que deletou o insumo no entry 0
    tkinter.messagebox.showinfo(title='Aviso uso excluído', message=f'{nome_insumo} foi excluído do Banco de Dados!')
    entry1.delete("0", "end") #limpa o campo
    print("Deletar Insumo")

def btn_clicked2(): #registrar uso insumo (consumir um insumo)
    # pegar a informação do campo nome_insumo (entry1)
    nome_insumo = entry1.get()

    # pegar a informação do campo quantidade (entry4)
    qtde_usada = entry4.get()

    # buscar o insumo pelo nome_insumo no banco de dados
    # diminuir a quantidade do insumo de acordo com a quantidade consumida
    comando = f"""UPDATE Insumos
            SET quantidade = quantidade - {qtde_usada}
            WHERE nome_insumo = '{nome_insumo}';
            """
    cursor.execute(comando)
    cursor.commit()

    # exibir uma mensagem dizendo quantas unidades ainda restam
    tkinter.messagebox.showinfo(title='Aviso uso insumo', message=f'{qtde_usada} unidades de {nome_insumo} foram usadas!')
    print("Usar Insumo")

def btn_clicked3(): #adicionar insumo
    # pegar todos os campos
    nome_insumo = entry1.get()
    data_validade = entry2.get()
    lote = entry3.get()
    quantidade = entry4.get()

    # adicionar no banco de dados aquele insumo
    comando = f"""INSERT INTO Insumos (nome_insumo, data_validade, lote, quantidade)
        VALUES
            ('{nome_insumo}', '{data_validade}', '{lote}', '{quantidade}')"""
    cursor.execute(comando)
    cursor.commit()
    tkinter.messagebox.showinfo(title='Aviso adicionar produto', message='Produto adicionado com sucesso!')

    # limpando os campos
    entry1.delete("0","end")
    entry2.delete("0","end")
    entry3.delete("0","end")
    entry4.delete("0","end")
    print("Adicionar Insumo")


# print(entry1.get()) #nome_insumo
# print(entry2.get()) #data_validade
# print(entry3.get()) #lote
# print(entry4.get()) #quantidade


window = Tk()

window.geometry("711x646")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 646,
    width = 711,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = fr"Tkinter_imgs\background.png")
background = canvas.create_image(
    355.5, 323.0,
    image=background_img)

img0 = PhotoImage(file = fr"Tkinter_imgs\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked0,
    relief = "flat")

b0.place(
    x = 479, y = 195,
    width = 178,
    height = 38)

img1 = PhotoImage(file = fr"Tkinter_imgs\img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b1.place(
    x = 247, y = 197,
    width = 178,
    height = 36)

img2 = PhotoImage(file = fr"Tkinter_imgs\img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b2.place(
    x = 479, y = 123,
    width = 178,
    height = 35)

img3 = PhotoImage(file = fr"Tkinter_imgs\img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked3,
    relief = "flat")

b3.place(
    x = 247, y = 125,
    width = 178,
    height = 34)

entry0_img = PhotoImage(file = fr"Tkinter_imgs\img_textBox0.png")
entry0_bg = canvas.create_image(
    455.0, 560.0,
    image = entry0_img)

entry0 = Text(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 250, y = 502,
    width = 410,
    height = 114)

entry1_img = PhotoImage(file = fr"Tkinter_imgs\img_textBox1.png")
entry1_bg = canvas.create_image(
    517.0, 294.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 377, y = 278,
    width = 280,
    height = 31)

entry2_img = PhotoImage(file = fr"Tkinter_imgs\img_textBox2.png")
entry2_bg = canvas.create_image(
    517.0, 340.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 377, y = 324,
    width = 280,
    height = 31)

entry3_img = PhotoImage(file = fr"Tkinter_imgs\img_textBox3.png")
entry3_bg = canvas.create_image(
    517.0, 388.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 377, y = 372,
    width = 280,
    height = 31)

entry4_img = PhotoImage(file = fr"Tkinter_imgs\img_textBox4.png")
entry4_bg = canvas.create_image(
    517.0, 436.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry4.place(
    x = 377, y = 420,
    width = 280,
    height = 31)

window.resizable(False, False)
window.mainloop()