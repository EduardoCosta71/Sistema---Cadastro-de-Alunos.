# Sistema---Cadastro-de-Alunos.
Sistema de Cadastro de Alunos, construido em python para aprimorar meu conhecimento.

Para construir este sistema utilizei a linguagem PYTHON, para guardar os dados obtidos
foi utilizado o Banco de dados Sqlite3.

Básicamente este sistema é um registro simples de alunos para preencher campos Nome, email,
telefone, sexo, data de nascimento, endereço, curso e o estudante pode colocar uma foto sua
no perfil dele.

O banco de dados utilizado foi o SQLite3, criei ele no proprio visua studio as tabelas.

Foi criada algumas funções do tipo = Registrar Aluno, Ver o aluno(seria para consultar as info dele), Pesquisar o aluno pelo (ID), Atualizar as Info do aluno e Excluir o aluno do banco de dados.

===========================

Para rodar este sistema é bem simples, basta fazer a instalação do banco sqlit3 e importar algumas bibliotecas abaixo:

Importar no "main.py"
import sqlite3
from tkinter import messagebox

Importar no "tela.py"
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
