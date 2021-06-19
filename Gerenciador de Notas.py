import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import *
import sqlite3

root = Tk()
root.title("Genrenciador de Notas")
width = 800
height = 400
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
#root.iconbitmap("Nova America/Noite/icons/crud.ico")
root.config(bg="#6666ff")

# --------- VARIAVEIS ----------

nome = StringVar()
materia = StringVar()
AV1 = StringVar()
AV2 = StringVar()
AV3 = StringVar()
AVD = StringVar()
AVDS = StringVar()
Media = 0
updateWindow = None
id = None
newWindow = None

# ------------ METODOS ----------

def database():
    conn = sqlite3.connect("estacio.db")
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS 'alunos' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT,materia TEXT ,AV1 decimal(10,2), AV2 decimal(10,2), AV3 decimal(10,2), AVD decimal(10,2), AVDS decimal(10,2),Media decimal(10,2)) """
    cursor.execute(query)
    cursor.execute('SELECT * FROM alunos ORDER BY nome')
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def submitData():
    
    if nome.get() == "" or AV1.get() == "" or AV2.get() == "" or materia.get() == "":
        resultado = msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
    elif AVD.get() != '':
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("estacio.db")
        cursor = conn.cursor()
        Media = ((float(AV1.get())+float(AV2.get())+float(AVD.get()))/3.0)
        query = """ INSERT INTO 'alunos' (nome, materia, AV1, AV2, AVD, Media) VALUES (?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (str(nome.get()),str(materia.get()) ,float(AV1.get()), 
                        float(AV2.get()), float(AVD.get()),float(Media)))
        conn.commit()
        cursor.execute('SELECT * FROM alunos ORDER BY nome')
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        AV1.set("")
        AV2.set("")
        materia.set("")
        AVD.set("")
        
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("estacio.db")
        cursor = conn.cursor()
        Media = ((float(AV1.get())+float(AV2.get()))/2.0)
        query = """ INSERT INTO 'alunos' (nome, materia, AV1, AV2, Media) VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query, (str(nome.get()),str(materia.get()), float(AV1.get()), 
                        float(AV2.get()),float(Media)))
        conn.commit()
        cursor.execute('SELECT * FROM alunos ORDER BY nome')
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        AV1.set("")
        AV2.set("")
        materia.set("")
        AVD.set("")
        

def updateData():
    if AVD.get != "" and AVDS != "":
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("estacio.db")
        cursor = conn.cursor()
        query = """ UPDATE 'alunos' SET nome = ?, materia = ?, AV1 = ?, AV2 = ?, AV3 = ?, AVD = ?, AVDS = ? WHERE id = ?"""
        cursor.execute(query, (str(nome.get()), str(materia.get()), float(AV1.get()),
                            float(AV2.get()), float(AV3.get()), float(AVD.get()), float(AVDS.get()), int(id)))
        conn.commit()
        cursor.execute('SELECT * FROM alunos ORDER BY nome')
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        materia.set("")
        AV1.set("")
        AV2.set("")
        AV3.set("")
        AVD.set("")
        AVDS.set("")
        updateWindow.destroy()
    elif AVD.get != '' and AVDS.get() == '':
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("estacio.db")
        cursor = conn.cursor()
        query = """ UPDATE 'alunos' SET nome = ?, materia = ?, AV1 = ?, AV2 = ?, AV3 = ?, AVD = ? WHERE id = ?"""
        cursor.execute(query, (str(nome.get()), str(materia.get()), float(AV1.get()),
                            float(AV2.get()), float(AV3.get()), float(AVD.get()), int(id)))
        conn.commit()
        cursor.execute('SELECT * FROM alunos ORDER BY nome')
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        materia.set("")
        AV1.set("")
        AV2.set("")
        AV3.set("")
        AVD.set("")
        updateWindow.destroy()
    elif AVD.get() == '' and AVDS.get() != '':
        resultado = msb.showwarning("", "Por favor, digite os campos de maneira correta.", icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("estacio.db")
        cursor = conn.cursor()
        query = """ UPDATE 'alunos' SET nome = ?, materia = ?, AV1 = ?, AV2 = ?, AV3 = ? WHERE id = ?"""
        cursor.execute(query, (str(nome.get()), str(materia.get()), float(AV1.get()),
                            float(AV2.get()), float(AV3.get()), int(id)))
        conn.commit()
        cursor.execute('SELECT * FROM alunos ORDER BY nome')
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        materia.set("")
        AV1.set("")
        AV2.set("")
        AV3.set("")
        updateWindow.destroy()

def onSelect(event):
    global id, updateWindow
    selectItem = tree.focus()
    conteudo = (tree.item(selectItem))
    selectedItem = conteudo["values"]
    id = selectedItem[0]
    nome.set("")
    materia.set("")
    AV1.set("")
    AV2.set("")
    AV3.set("")
    AVD.set("")
    AVDS.set("")
    nome.set(selectedItem[1])
    materia.set(selectedItem[2])
    AV1.set(selectedItem[3])
    AV2.set(selectedItem[4])
    AV3.set(selectedItem[5])
    AVD.set(selectedItem[6])
    AVDS.set(selectedItem[7])

    #--------- CRIANDO JANELA UPDATE ---------
    updateWindow = Toplevel()
    updateWindow.title("ATUALIZANDO NOTAS FINAIS")
    width = 480
    height = 300
    sc_width = updateWindow.winfo_screenwidth()
    sc_height = updateWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    updateWindow.resizable(0, 0)

    # --------- FRAME DO ATUALIZAR ----------
    formTitle = Frame(updateWindow)
    formTitle.pack(side=TOP)
    formContact = Frame(updateWindow)
    formContact.pack(side = TOP, pady = 10)
    # --------- LABEL DO ATUALIZAR ----------
    lbl_title = Label(formTitle, text="Atualizando Notas", font=('arial', 18), bg='blue', width=300)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContact, text="Nome", font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_materia = Label(formContact, text="Materia", font=('arial', 12))
    lbl_materia.grid(row=1, sticky=W)
    lbl_AV1 = Label(formContact, text="AV1", font=('arial', 12))
    lbl_AV1.grid(row=2, sticky=W)
    lbl_AV2 = Label(formContact, text="AV2", font=('arial', 12))
    lbl_AV2.grid(row=3, sticky=W)
    lbl_AV3 = Label(formContact, text="AV3", font=('arial', 12))
    lbl_AV3.grid(row=4, sticky=W)
    lbl_AVD = Label(formContact, text="AVD", font=('arial', 12))
    lbl_AVD.grid(row=5, sticky=W)
    lbl_AVDS = Label(formContact, text="AVDS", font=('arial', 12))
    lbl_AVDS.grid(row=6, sticky=W)

    # --------- ENTRY DO ATUALIZAR ----------
    nomeEntry = Entry(formContact, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    materiaEntry = Entry(formContact, textvariable=materia, font=('arial', 12))
    materiaEntry.grid(row=1, column=1)
    AV1Entry = Entry(formContact, textvariable=AV1, font=('arial', 12))
    AV1Entry.grid(row=2, column=1)
    AV2Entry = Entry(formContact, textvariable=AV2, font=('arial', 12))
    AV2Entry.grid(row=3, column=1)
    AV3Entry = Entry(formContact, textvariable=AV3, font=('arial', 12))
    AV3Entry.grid(row=4, column=1)
    AVDEntry = Entry(formContact, textvariable=AVD, font=('arial', 12))
    AVDEntry.grid(row=5, column=1)
    AVDSEntry = Entry(formContact, textvariable=AVDS, font=('arial', 12))
    AVDSEntry.grid(row=6, column=1)
    
    # --------- BUTTON DO ATUALIZAR ---------
    bttn_update = Button(formContact, text="Atualizar", width=50, command=updateData)
    bttn_update.grid(row=7, columnspan=2, pady=10)

def deletarData():
    if not tree.selection():
        resultado = msb.showwarning("", "Por favor, selecione um item na lista.", icon="warning")
    else:
        resultado = msb.askquestion("", "Tem certeza que deseja deletar o aluno?")
        if resultado == 'yes':
            selectItem = tree.focus()
            conteudo = (tree.item(selectItem))
            selectedItem = conteudo['values']
            tree.delete(selectItem)
            conn = sqlite3.connect("estacio.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM alunos WHERE id = %d" % selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()

def inserirData():
    global newWindow
    nome.set("")
    materia.set("")
    AV1.set("")
    AV2.set("")
    AVD.set("")

    #--------- CRIANDO JANELA INCLUDE ---------
    newWindow = Toplevel()
    newWindow.title("INSERINDO NOTAS")
    width = 480
    heigth = 200
    sc_width = newWindow.winfo_screenwidth()
    sc_height = newWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    newWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    newWindow.resizable(0, 0)

    # --------- FRAME DO INCLUDE ----------
    formTitle = Frame(newWindow)
    formTitle.pack(side=TOP)
    formContact = Frame(newWindow)
    formContact.pack(side=TOP, pady=10)
    # --------- LABEL DO INCLUDE ----------
    lbl_title = Label(formTitle, text="Inserindo Notas",
                      font=('arial', 18), bg='blue', width=300)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContact, text="Nome", font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_materia = Label(formContact, text="Materia", font=('arial', 12))
    lbl_materia.grid(row=1, sticky=W)
    lbl_AV1 = Label(formContact, text="AV1", font=('arial', 12))
    lbl_AV1.grid(row=2, sticky=W)
    lbl_AV2 = Label(formContact, text="AV2", font=('arial', 12))
    lbl_AV2.grid(row=3, sticky=W)
    lbl_AVD = Label(formContact, text="AVD", font=('arial', 12))
    lbl_AVD.grid(row=4, sticky=W)

    # --------- ENTRY DO INCLUDE ----------
    nomeEntry = Entry(formContact, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    materiaEntry = Entry(formContact, textvariable=materia, font=('arial', 12))
    materiaEntry.grid(row=1, column=1)
    AV1Entry = Entry(formContact, textvariable=AV1, font=('arial', 12))
    AV1Entry.grid(row=2, column=1)
    AV2Entry = Entry(formContact, textvariable=AV2, font=('arial', 12))
    AV2Entry.grid(row=3, column=1)
    AVDEntry = Entry(formContact, textvariable=AVD, font=('arial', 12))
    AVDEntry.grid(row=4, column=1)

    # --------- BUTTON DO INCLUDE ---------
    bttn_inserir = Button(formContact, text="Inserir",
                        width=50, command=submitData)
    bttn_inserir.grid(row=6, columnspan=2, pady=10)

def sobreApp():
    pass

# --------- FRAMES TELA PRINCIPAL -------------
top = Frame(root, width=500, bd=1,relief=SOLID)
top.pack(side=TOP)
mid = Frame(root, width=500, bg="#6666ff")
mid.pack(side=TOP)
midLeft = Frame(mid, width=100)
midLeft.pack(side=LEFT)
midLeftPadding = Frame(mid, width=350, bg="#6666ff")
midLeftPadding.pack(side=LEFT)
midRight = Frame(mid, width=100)
midRight.pack(side=RIGHT)
bottom = Frame(root, width=200)
bottom.pack(side=BOTTOM)
tableMargim = Frame(root, width=500)
tableMargim.pack(side=TOP)


# --------- LABELS TELA PRINCIPAL -------------
lbl_title = Label(top, text="SISTEMA DE GERENCIAMENTO DE NOTAS Academicas", font=('arial', 18), width=500)
lbl_title.pack(fill=X)

lbl_alt = Label(bottom, text="Para alterar clique duas vezes no aluno desejado.", font=('arial', 12), width=200)
lbl_alt.pack(fill=X)

# --------- BUTTONS TELA PRINCIPAL -------------
bttn_add = Button(midLeft, text="Inserir", bg="OliveDrab1", command=inserirData)
bttn_add.pack()
bttn_del = Button(midRight, text="Deletar",
                 bg="orange red", command=deletarData)
bttn_del.pack(side=RIGHT)

# --------- TREEVIEW TELA PRINCIPAL -------------

scrollbarX = Scrollbar(tableMargim, orient=HORIZONTAL)
scrollbarY = Scrollbar(tableMargim, orient=VERTICAL)

tree = ttk.Treeview(tableMargim, columns=("ID", "Nome", "Materia", "AV1", "AV2", "AV3", "AVD", "AVDS", "Media"), height=400, 
                    selectmode="extended", yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)
scrollbarY.config(command=tree.yview)
scrollbarY.pack(side=RIGHT, fill=Y)
scrollbarX.config(command=tree.xview)
scrollbarX.pack(side=BOTTOM, fill=X)
tree.heading("ID", text="ID", anchor=W)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("Materia", text="Materia", anchor=W)
tree.heading("AV1", text="AV1", anchor=W)
tree.heading("AV2", text="AV2", anchor=W)
tree.heading("AV3", text="AV3", anchor=W)
tree.heading("AVD", text="AVD", anchor=W)
tree.heading("AVDS", text="AVDS", anchor=W)
tree.heading("Media", text="Media", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=40)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=90)
tree.column('#6', stretch=NO, minwidth=0, width=90)
tree.column('#7', stretch=NO, minwidth=0, width=90)
tree.column('#8', stretch=NO, minwidth=0, width=90)
tree.pack()
tree.bind('<Double-Button-1>', onSelect)

# ----------------- CRIANDO MENU -----------------
menu_bar = Menu(root)
root.config(menu=menu_bar)

# construir o menu
fileMenu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label="Menu", menu=fileMenu)
fileMenu.add_command(label="Criar Novo", command=inserirData)
fileMenu.add_separator()
fileMenu.add_command(label="Sair", command=root.destroy)

# construindo outro
menuSobre = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label="Sobre", menu=menuSobre)
menuSobre.add_command(label="Info", command=sobreApp)


#----------INICIANDO -------------
if __name__ == '__main__':
    database()
    root.mainloop()
