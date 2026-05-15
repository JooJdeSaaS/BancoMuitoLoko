import sqlite3
import re


def busca_usuario_por_email(email_digitado):
    # 1. Validação básica de entrada (Regex para e-mail)
    # Garante que o input segue um formato de e-mail válido antes de processar
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(padrao_email, email_digitado):
        print("Erro: Formato de e-mail inválido.")
        return None

    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    # 2. Uso de Consultas Parametrizadas (Prepared Statements)
    # O '?' atua como um placeholder, impedindo que o input seja interpretado como comando SQL
    query = "SELECT nome, email FROM usuarios WHERE email = ?"

    # Os dados são passados como uma tupla no segundo argumento do execute()
    cursor.execute(query, (email_digitado,))

    resultado = cursor.fetchone()
    conexao.close()

    return resultado