"""
EXEMPLO EDUCACIONAL - Vulnerabilidades XSS e SQL Injection (CORRIGIDO)
Este codigo demonstra como CORRIGIR vulnerabilidades de seguranca.
NAO USE EM PRODUCAO SEM REVISAO COMPLETA!
"""

from flask import Flask, request
import sqlite3
import html
import os

app = Flask(__name__)

# Inicializar banco de dados
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    cursor.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'admin123')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (2, 'user', 'pass123')")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return '''
        <h1>Exemplos de Vulnerabilidades (Corrigidas)</h1>
        <h2>XSS - Pesquisa</h2>
        <form action="/search" method="GET">
            <input type="text" name="q" placeholder="Digite sua busca">
            <button type="submit">Buscar</button>
        </form>
        <h2>SQL Injection - Login</h2>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Usuario"><br>
            <input type="password" name="password" placeholder="Senha"><br>
            <button type="submit">Login</button>
        </form>
        <h2>SQL Injection - Buscar Usuario</h2>
        <form action="/user" method="GET">
            <input type="text" name="id" placeholder="ID do usuario">
            <button type="submit">Buscar</button>
        </form>
    '''

@app.route('/search')
def search():
    query = request.args.get('q', '')
    # CORRIGIDO: html.escape() converte caracteres especiais (<, >, &, ", ')
    # em entidades HTML, prevenindo XSS.
    # VULNERAVEL seria: return f'<h1>Resultados para: {query}</h1>'
    safe_query = html.escape(query)
    return f'''
        <h1>Resultados para: {safe_query}</h1>
        <p>Nenhum resultado encontrado.</p>
        <a href="/">Voltar</a>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    # CORRIGIDO: Usando parametros preparados (?) em vez de concatenacao de strings.
    # VULNERAVEL seria:
    #   query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    # Isso permitiria injecao como: admin' OR '1'='1
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        # CORRIGIDO: Escapando o username para prevenir XSS secundario
        safe_username = html.escape(user[1])
        return f'''
            <h1>Login bem-sucedido!</h1>
            <p>Bem-vindo, {safe_username}!</p>
            <a href="/">Voltar</a>
        '''
    else:
        return '''
            <h1>Login falhou!</h1>
            <p>Usuario ou senha incorretos.</p>
            <a href="/">Voltar</a>
        '''

@app.route('/user')
def get_user():
    user_id = request.args.get('id', '')

    # CORRIGIDO: Validacao de entrada antes de usar o parametro
    if not user_id:
        return '<h1>Erro: ID nao fornecido</h1><a href="/">Voltar</a>'

    # CORRIGIDO: Usando parametros preparados (?) em vez de concatenacao de strings.
    # VULNERAVEL seria: query = "SELECT * FROM users WHERE id=" + user_id
    # Isso permitiria injecao como: 1 OR 1=1
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id=?"
    cursor.execute(query, (user_id,))
    users = cursor.fetchall()
    conn.close()

    # CORRIGIDO: Escapando dados do banco para prevenir XSS
    result = '<h1>Usuarios encontrados:</h1>'
    for user in users:
        safe_id = html.escape(str(user[0]))
        safe_username = html.escape(str(user[1]))
        result += f'<p>ID: {safe_id}, Usuario: {safe_username}</p>'
    result += '<a href="/">Voltar</a>'

    return result

if __name__ == '__main__':
    # CORRIGIDO: Usando variavel de ambiente para controlar o modo debug.
    # VULNERAVEL seria: app.run(debug=True) — expoe stack traces e console interativo em producao.
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)
