from flask import Flask, render_template
app = Flask(__name__, template_folder='template')

app = Flask(__name__)

#Criando site em Python com Flask
##criar a primeira página: route  mulheresnati2022.com/ função: o que quer exibir naquela página e teplate: criar um html
@app.route("/")
def homepage():
    return"<p>Meu Portfólio de Engenharia de Dados</p>"

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

if __name__ == "__main__":
    app.run(debug=True)


# servidor do heroku
