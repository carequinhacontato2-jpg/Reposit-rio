from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "A maioria das pessoas que sofre de dependência tecnológica sente estresse quando fica sem internet.",

    "Mais de 50% das pessoas entre 18 e 34 anos se consideram dependentes de smartphones.",

    "Uma forma de combater a dependência tecnológica é procurar atividades que melhorem o humor."
]

password_chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%"

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Página Inicial</title>

        <link rel="stylesheet" href="/static/style.css">
    </head>

    <body>

        <h1>Dependência Tecnológica</h1>

        <p>Bem-vindo ao site!</p>

        <a href="/random_fact">Veja um fato aleatório!</a>

        <br><br>

        <a href="/secret">Página secreta 🔐</a>

    </body>
    </html>
    """

@app.route("/random_fact")
def random_fact():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Fato Aleatório</title>

        <link rel="stylesheet" href="/static/style.css">
    </head>

    <body>

        <h1>Fato Aleatório</h1>

        <p>{random.choice(facts_list)}</p>

        <a href="/">Voltar</a>

    </body>
    </html>
    """

@app.route("/secret")
def secret():
    password = ""

    for i in range(12):
        password += random.choice(password_chars)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Página Secreta</title>

        <link rel="stylesheet" href="/static/style.css">
    </head>

    <body>

        <h1>Gerador de Senhas 🔐</h1>

        <h2>Sua senha aleatória:</h2>

        <p>{password}</p>

        <a href="/">Voltar</a>

    </body>
    </html>
    """

app.run(debug=True)
