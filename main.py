import sqlite3
from tkinter import messagebox

#Conexão com o banco de dados e criação da tabela de estudantes=========================================
class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('students.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                fone TEXT NOT NULL,
                sexo TEXT NOT NULL,
                data_nascimento TEXT NOT NULL,
                endereco TEXT NULL,
                curso TEXT NOT NULL,
                picture TEXT NOT NULL
            )
        ''')
        self.conn.commit()

 #Registro De Estudante===================================================================
    def register_student(self, students):
            try:
                self.cursor.execute("INSERT INTO students (name, email, fone, sexo, data_nascimento, endereco, curso, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                     (students))
                self.conn.commit()
                messagebox.showinfo("Success", "Student registered successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

#Consulta de estudantes====================================================================
    def view_students(self):
        self.cursor.execute("SELECT * FROM students")
        dados = self.cursor.fetchall()

        return dados
        
#Consulta de estudantes por ID==============================================================
    def search_students(self, id):
        self.cursor.execute("SELECT * FROM students WHERE id=?", (id,))
        dados = self.cursor.fetchone()
      
        return dados
    
    def update_student(self, nova_valores):
        try:
            query = "UPDATE students SET name=?, email=?, fone=?, sexo=?, data_nascimento=?, endereco=?, curso=?, picture=? WHERE id=?"
            self.cursor.execute(query, nova_valores)
            self.conn.commit()
            messagebox.showinfo("Success", f"Student updated successfully!{nova_valores[8]} is actualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

#Exclusão de estudantes======================================================================
    def delete_student(self, id):
        try:
            self.cursor.execute("DELETE FROM students WHERE id=?", (id,))
            self.conn.commit()
            messagebox.showinfo("Success", f"Student with ID {id} deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

#Instancia do sistema de registro
sistema = SistemaDeRegistro()

#informações
#estudante = ("Eduardo Costa", "edu.costa@example.com", "123456789", "Male", "2000-04-01", "123 Main Tuty", "ADS", "profile.jpg")
#sistema.register_student(estudante)

#ver estudantes
#todos_alunos = sistema.view_students()

#buscar estudante por ID
#aluno_especifico = sistema.search_students()

#atualizar estudante
#estudante = ("Johan", "jh.a@example.com", "555-5555", "Male", "2006-04-01", "123 Main Tuty", "Computer Science", "profile.jpg", 2)
#nova_informacao = sistema.update_student(estudante)]

#excluir estudante
#sistema.delete_student(1)
