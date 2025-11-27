from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from dao.ContatoDao import ContatoDao
from model import Contato 
#cria app

app = Flask(__name__)

#banco

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='221@s3nhaforte'
app.config['MYSQL_DB']='aula_bd'
app.config['MYSQL_PORT']=3306
db = MySQL(app)

dao = ContatoDao(db)

@app.route('/inicio')
def listar():
    lista_contatos = dao.listar()
    print (len(lista_contatos))
    return render_template('lista.html', titulo= 'Contatos',lista = lista_contatos)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Contato')

@app.route('/criar',methods=['POST',])
def criar():
    nome = request.form['nome']
    celular = request.form['celular']
    email = request.form['email']
    data_nasc = request.form['dt_nasc']
    contato = Contato(nome, celular, email, data_nasc)
    dao.salvar(contato)
    return redirect('/inicio')


@app.route('/editar/<int:id>')
def editar(id):
    contato = dao.listar_por_id(id)
    return render_template('editar.html', titulo='Atualiza Contato', contato=contato)

#roda
app.run(debug=True)

