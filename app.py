"""
EXEMPLO EDUCACIONAL - Vulnerabilidade XSS
Este codigo demonstra uma vulnerabilidade XSS para fins de aprendizado.
NAO USE EM PRODUCAO!
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Pesquisa</h1>
        <form action="/search" method="GET">
            <input type="text" name="q" placeholder="Digite sua busca">
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

if __name__ == '__main__':
    app.run(debug=True)
