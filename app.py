from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form["nome"]
        mensagem = request.form["mensagem"]
        return render_template("obrigado.html", nome=nome, mensagem=mensagem)
    return render_template("contato.html")

@app.route("/dolly")
def dolly():
    return render_template("dolly.html")

if __name__ == "__main__":
    app.run(debug=True)