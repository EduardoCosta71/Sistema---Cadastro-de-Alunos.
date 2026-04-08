#importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

#importando pillow
from PIL import ImageTk, Image

#tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

#importando o sistema de registro
from main import *


#cores====================================================================================
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

#criando a janela==========================================================================
janela = Tk()
janela.title("Sistema de Registro de Estudantes")
janela.geometry("810x535")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

#Criando Frames=============================================================================
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_table = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_table.grid(row=3, column=0, pady=1, padx=10, sticky=NSEW, columnspan=5)



#Logo========================================================================================
app_logo = Image.open('Escola.jpeg')
app_logo = app_logo.resize((50, 50))
app_logo = ImageTk.PhotoImage(app_logo)
app_logo = Label(frame_logo, image=app_logo, text="Sistema de Registro de Estudantes", width=850, compound=LEFT, anchor=NW, font="Verdana 15", bg=co7, fg=co1)
app_logo.place(x=5, y=0)

#Abrindo imagem==============================================================================
imagem = Image.open('Escola.jpeg')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
l_imagem.place(x=390, y=10)


#Criando funcoes para o CRUD==================================================================
#Adicionar estudante
def add_student():
    global imagem, imagem_string, l_imagem

    #obter os dados dos campos de entrada
    nome = e_nome.get()
    email = e_email.get()
    fone = e_fone.get()
    sexo = c_sexo.get()
    data_nascimento = d_data_nascimento.get()
    endereco = e_endereco.get()
    curso = e_curso.get()
    picture = imagem_string

    lista = [nome, email, fone, sexo, data_nascimento, endereco, curso, picture]

    #Verificando se os campos obrigatórios estão preenchidos
    for i in lista:
        if i == "":
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
    
    #Adicionando o estudante ao sistema
    sistema.register_student(lista)
    

    #limpar os campos de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_fone.delete(0, END)
    c_sexo.delete(0, END)
    d_data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    e_curso.delete(0, END)

#mostrar a imagem do estudante
    imagem = Image.open('Escola.jpeg')
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    
    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)



    #mostrar valores tabela
    table_studets()

#Função procurar estudante ID ============================================================
def procurar_aluno():
    global imagem, imagem_string, l_imagem

    #obter o ID do campo de entrada
    id_aluno = int(e_procurar.get())

    #Procurar o estudante no sistema
    estudante = sistema.search_students(id_aluno)

    #Limpando os campos de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_fone.delete(0, END)
    c_sexo.delete(0, END)
    d_data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    e_curso.delete(0, END)

    #mostrar os dados do estudante nos campos de entrada
    e_nome.insert(END, estudante[1])
    e_email.insert(END, estudante[2])
    e_fone.insert(END, estudante[3])
    c_sexo.insert(END, estudante[4])
    d_data_nascimento.insert(END, estudante[5])
    e_endereco.insert(END, estudante[6])
    e_curso.insert(END, estudante[7])

    #mostrar a imagem do estudante
    imagem = estudante[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)


#Função para atualizar estudante ID ============================================================
def atualizar_aluno():
    global imagem, imagem_string, l_imagem

    #obter o ID do campo de entrada
    id_aluno = int(e_procurar.get())

    #obter os dados dos campos de entrada
    nome = e_nome.get()
    email = e_email.get()
    fone = e_fone.get()
    sexo = c_sexo.get()
    data_nascimento = d_data_nascimento.get()
    endereco = e_endereco.get()
    curso = e_curso.get()
    picture = imagem_string

    lista = [nome, email, fone, sexo, data_nascimento, endereco, curso, picture, id_aluno]

    #Verificando se os campos obrigatórios estão preenchidos
    for i in lista:
        if i == "":
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
    
    #Atualizando o estudante no sistema
    sistema.update_student(lista)

    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_fone.delete(0, END)
    c_sexo.delete(0, END)
    d_data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    e_curso.delete(0, END)

    #mostrar a imagem do estudante
    imagem = Image.open("Escola.jpeg")
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    #mostrar valores tabela
    table_studets()


#Função para deletar estudante ID ============================================================
def deletar_aluno():
    global imagem, imagem_string, l_imagem

    #obter o ID do campo de entrada
    id_aluno = int(e_procurar.get())

    #Deletar o estudante no sistema
    sistema.delete_student(id_aluno)

    e_nome.delete(0,END)
    e_email.delete(0,END)
    e_fone.delete(0,END)
    c_sexo.delete(0,END)
    d_data_nascimento.delete(0,END)
    e_endereco.delete(0,END)
    e_curso.delete(0,END)

    e_procurar.delete(0, END)

    #mostrar a imagem do estudante
    imagem = Image.open('Escola.jpeg')
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    #mostrar valores tabela
    table_studets()



#Botões Entrada\frame_details===============================================================
l_nome = Label(frame_details, text="Nome completo", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_details, width=30, justify='left', relief=SOLID)
e_nome.place(x=7, y=40)

l_email = Label(frame_details, text="Email", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=30, justify='left', relief=SOLID)
e_email.place(x=7, y=100)

l_fone = Label(frame_details, text="Telefone", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_fone.place(x=4, y=130)
e_fone = Entry(frame_details, width=15, justify='left', relief=SOLID)
e_fone.place(x=7, y=160)

l_sexo = Label(frame_details, text="Sexo", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_sexo.place(x=127, y=130)
c_sexo = ttk.Combobox(frame_details, width=7, font=("Ivy 8 bold"), justify='center')
c_sexo['values'] = ("Masculino", "Feminino", "Outro")
c_sexo.place(x=130, y=160)

l_data_nascimento = Label(frame_details, text="Data de Nascimento", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_data_nascimento.place(x=220, y=10)
d_data_nascimento = DateEntry(frame_details, width=18, justify='center', background='red', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
d_data_nascimento.place(x=224, y=40)

l_endereco = Label(frame_details, text="Endereço", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_endereco.place(x=220, y=70)  
e_endereco = Entry(frame_details, width=15, justify='left', relief=SOLID)
e_endereco.place(x=224, y=100)

#Opcao de cursos para o estudante==================================================================
cursos = ["Engenharia de Software", "Ciência da Computação", "Sistemas de Informação", "Análise e Desenvolvimento de Sistemas", "Redes de Computadores", "Segurança da Informação", "Inteligência Artificial", "Banco de Dados", "Desenvolvimento Web", "Desenvolvimento Mobile"]   

l_curso = Label(frame_details, text="Cursos", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_curso.place(x=220, y=130)
e_curso = ttk.Combobox(frame_details, width=18, font=("Ivy 8 bold"), justify='center')
e_curso['values'] = (cursos)
e_curso.place(x=224, y=160)

#Função para selecionar a imagem==============================================================================
def selecionar_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    b_selecionar_imagem['text'] = 'Trocar Imagem'.upper()

#botao para selecionar a imagem
b_selecionar_imagem = Button(frame_details, command=selecionar_imagem, text="Selecionar Imagem".upper(), compound=CENTER, anchor=CENTER, width=20, font=("Ivy 7 bold"), bg=co3, fg=co0, relief=RAISED)
b_selecionar_imagem.place(x=390, y=160)



#Tabela alunos================================================================================
def table_studets():

    #Creating a treeview with dual scrollbars
    list_header = ['ID', 'Nome', 'Email', 'Fone', 'Sexo', 'Data de Nascimento', 'Endereço', 'Curso'] 
    
    #Ver Estudantes
    df_list = sistema.view_students()

    tree_aluno = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")

    #Vertical
    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree_aluno.yview)
    #horizontal
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_table.grid_rowconfigure(0, weight=12)
    
    hd=["nw", "nw", "nw", "center", "center", "center", "center", "center"]
    h=[40, 150, 150, 70, 70, 70, 120, 100, 100]
    n=0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        #adjusting the column's width to the header string
        tree_aluno.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)




#Procurar aluno================================================================================
frame_procurar = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar Aluno [Entra ID]", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='center', relief=SOLID, font=("Ivy 10"))
e_procurar.grid(row=1, column=0, pady=10, padx=10, sticky=NSEW)

btn_procurar = Button(frame_procurar, command=procurar_aluno, text="Procurar", anchor=CENTER, width=9, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co1, fg=co4)
btn_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

#Botoes de ação, Adicionar, Editar, Excluir=======================================================
frame_btn = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_btn.grid(row=2, column=0, pady=10, padx=10, sticky=NSEW)

btn_adicionar = Button(frame_btn, command=add_student, relief=GROOVE, text="Adicionar", width=24, compound=LEFT, overrelief=RIDGE, font=("Ivy 11 bold"), bg=co1, fg=co0)
btn_adicionar.grid(row=1, column=1, pady=5, padx=10, sticky=NSEW)

btn_editar = Button(frame_btn, command=atualizar_aluno, relief=GROOVE, text="Atualizar", width=24, compound=LEFT, overrelief=RIDGE, font=("Ivy 11 bold"), bg=co1, fg=co0)
btn_editar.grid(row=2, column=1, pady=5, padx=10, sticky=NSEW)

btn_excluir = Button(frame_btn, command=deletar_aluno, relief=GROOVE, text="Deletar", width=24, compound=LEFT , overrelief=RIDGE, font=("Ivy 11 bold"), bg=co1, fg=co0)
btn_excluir.grid(row=3, column=1, pady=5, padx=10, sticky=NSEW)

#linha separadora
l_linha = Label(frame_botoes, relief=GROOVE, text="", width=1, height=123, anchor=NW, font='Ivy 10', bg=co1, fg=co0)
l_linha.place(x=265, y=15)

#chamar tabela
table_studets()


janela.mainloop()
