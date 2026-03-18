"""
EXEMPLO EDUCACIONAL - Vulnerabilidades XSS e SQL Injection
Este codigo demonstra vulnerabilidades de seguranca para fins de aprendizado.
NAO USE EM PRODUCAO!
"""

from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Inicializar banco de dados vulneravel
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
        <h1>Exemplos de Vulnerabilidades</h1>
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
    # VULNERAVEL: O input do usuario e renderizado diretamente no HTML
    # sem sanitizacao, permitindo injecao de scripts maliciosos
    return f'''
        <h1>Resultados para: {query}</h1>
        <p>Nenhum resultado encontrado.</p>
        <a href="/">Voltar</a>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    # VULNERAVEL: SQL Injection - concatenacao direta de strings na query
    # Permite que atacantes injetem SQL arbitrario (ex: admin' OR '1'='1)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        return f'''
            <h1>Login bem-sucedido!</h1>
            <p>Bem-vindo, {user[1]}!</p>
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

    # VULNERAVEL: SQL Injection - parametro user_id concatenado diretamente
    # Permite extracao de dados (ex: 1 OR 1=1)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id=" + user_id
    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()

    result = '<h1>Usuarios encontrados:</h1>'
    for user in users:
        result += f'<p>ID: {user[0]}, Usuario: {user[1]}</p>'
    result += '<a href="/">Voltar</a>'

    return result

if __name__ == '__main__':
    app.run(debug=True)
