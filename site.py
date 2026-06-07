from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <html>
        <head>
            <title>Meu Site</title>
            <style>
                body {
                    background-color: #1a1a2e;
                    color: white;
                    font-family: Arial;
                    text-align: center;
                    padding: 50px;
                }
                h1 { color: #00d4ff; }
                p  { color: #a0a0a0; }
                a {
                    color: #00d4ff;
                    font-size: 18px;
                    margin: 10px;
                }
            </style>
        </head>
        <body>
            <h1>Página Inicial</h1>
            <p>Bem vindo ao meu site!</p>
            <a href="/sobre">Ir para Sobre</a>
            <a href="/contato">Ir para Contato</a>
            <a href='/dolly'>Ir para Dolly</a>
        </body>
    </html>
    """

@app.route("/sobre")
def sobre():
    return """
    <html>
        <head>
            <title>Sobre</title>
            <style>
                body {
                    background-color: #1a1a2e;
                    color: white;
                    font-family: Arial;
                    text-align: center;
                    padding: 50px;
                }
                h1 { color: #00d4ff; }
                a  { color: #00d4ff; font-size: 18px; }
            </style>
        </head>
        <body>
            <h1>Sobre mim</h1>
            <p>Estou aprendendo Python e Flask!</p>
            <a href="/">Voltar para inicio</a>
        </body>
    </html>
    """

@app.route("/contato")
def contato():
    return """
    <html>
        <head>
            <title>Contato</title>
            <style>
                body {
                    background-color: #1a1a2e;
                    color: white;
                    font-family: Arial;
                    text-align: center;
                    padding: 50px;
                }
                h1 { color: #00d4ff; }
                a  { color: #00d4ff; font-size: 18px; }
            </style>
        </head>
        <body>
            <h1>Contato</h1>
            <p>Me encontre no Discord!</p>
            <a href="/">Voltar para inicio</a>
        </body>
    </html>
    """

@app.route('/dolly')
def dolly():
    return """
    <html>
        <head>
            <title>Dolly</title>
            <style>
                body {
                    background-color: #1a1a2e;
                    color: white;
                    font-family: Arial;
                    text-align: center;
                    padding: 50px;
                }
                h1 { color: #00d64ff; }
            </style>
        </head>
        <body>
            <h1>Dolly</h1>
            <p>Eu sou o Dolly, tenho 15 anos e quero ser um programador profissional!</p>
            <a href="/">Voltar para inicio</a>
        </body>
    </html>            
    """
if __name__ == "__main__":
    app.run(debug=True)