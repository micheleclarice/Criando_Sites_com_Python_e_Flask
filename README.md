# Criando Sites com Python e Flash 


<p>Aprendendo a Criar Sites, com Python e Flask.
  
O intuito é entender, a estrutura de códigos, para uma página web em um “local host”.

Obs: Minha ideia, é, criar meu portfólio para Engenharia de Dados, disponível em uma página web!</p>👩🏻‍💻📊

# Tutorial

O Flask é um dos principais microframeworks do ecossistema Python e principal concorrente do Django. Já vimos aqui no blog o que é o Flask e quando utilizá-lo ao invés do Django.

Sabendo disso, veremos neste artigo como criar nossa primeira app com Flask e do que vamos precisar para tal tarefa.

# 1) Configurando ambiente
Por ser um framework Python, o Flask possui os mesmos requisitos básicos que o Django (possuir o Python instalado e uma IDE para escrever o código). Aqui no blog, já temos um artigo sobre como configurar nosso ambiente de desenvolvimento para o Django, mas que pode ser utilizado para o Flask sem maiores problemas :)

# 2) Criando Projeto
Com o ambiente de desenvolvimento devidamente configurado, podemos iniciar e criar nossa primeira aplicação com Flask. Para isso, o primeiro passo é criar um projeto com o PyCharm que vai armazenar os arquivos de código da nossa aplicação Flask.

Sendo assim, ao abrir o PyCharm, veremos a seguinte tela:

Dentre as três opções disponíveis, selecionaremos a “Create New Project” para que possamos criar o primeiro projeto com PyCharm. Fazendo isso, seremos redirecionados para a seguinte tela:

Nesta tela, definimos a localização do projeto e onde será armazenada sua virtualenv. Caso você não saiba do que se trata uma virtualenv, falamos sobre ela neste artigo, recomendo fortemente sua leitura :)

Costumo armazenar a virtualenv de cada projeto em seu próprio diretório. Assim, cada projeto possuirá sua virtualenv isolada.

Por fim, após indicar o caminho e o nome do projeto, podemos clicar em “Create”. Isso fará com que uma nova janela do PyCharm seja aberta com o seguinte conteúdo:

# 3) Instalando o Flask
Com o projeto do PyCharm criado, já podemos criar nossa app Flask. Para isso, o primeiro passo é instalar o pacote em nossa virtualenv. Para isso, o PyCharm possui uma interface gráfica que auxilia todo este processo, localizada em File > Settings > Project Interpreter (se você está utilizando o Windows ou Linux) ou PyCharm > Preferences (se você está utilizando o macOS).

É nesta janela que poderemos adicionar os pacotes à nossa virtualenv. Para isso, clicamos no botão “+” localizado no canto inferior esquerdo da janela, que exibirá uma tela para buscarmos pelo pacote desejado.

Nesta janela, buscamos pelo pacote “Flask” e clicamos em “Install Package”. Após isso, o PyCharm (utilizando o PIP) vai baixar o pacote selecionado e instalar na virtualenv do projeto:

Ao finalizar este processo, podemos fechar a janela e notaremos que o pacote foi instalado com sucesso:

# 4) Criando primeira APP Flask:

Com todo o ambiente configurado e os pacotes necessários instalados, podemos iniciar o desenvolvimento da nossa aplicação. Neste artigo, veremos uma aplicação que responde a uma requisição e devolve uma string como resposta. Nos próximos artigos veremos como trabalhar com rotas, templates, bancos de dados, etc…


# Portanto, dentro do projeto do PyCharm, criaremos um arquivo chamado app.py e colamos o seguinte conteúdo:

from flask import Flask
app = Flask(__name__)

@app.route("/teste")
def index():
	return 'Olá Mundo!'

if __name__ == "__main__":
	app.run()

Linha a linha, o código acima pode ser entendido da seguinte forma:

Importamos o pacote Flask da nossa virtualenv;

Criamos uma instância do Flask e salvamos na variável app. É essa variável que representa a aplicação Flask que estamos criando;

Definimos que a rota “/” vai executar o método index() do nosso arquivo, que retornará a string “Olá Mundo!”;

Verificamos se o arquivo app.pyestá sendo executado pelo terminal e, caso positivo, iniciamos o servidor do Flask.

Agora, para executar nosso script, clicamos no botão verde ao lado da linha 8 do nosso script e selecionamos a opção “Run ‘app’”:Ao fazer isso, o servidor do Flask será executado no terminal do próprio PyCharm e uma URL para acessá-lo será exibida:
Clicando na rota disponibilizada, o navegador padrão do computador irá abrir e, ao executar a rota “/teste”, teremos o seguinte retorno:
Conclusão
Vimos neste artigo o quão simples é instalar o Flask e criar nossa primeira app. 


Fonte:
https://www.treinaweb.com.br/blog/criando-primeira-app-com-flask/
