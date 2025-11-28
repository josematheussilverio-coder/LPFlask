from flask import flash, Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from dao.ContatoDao import ContatoDao
from model import Contato


app = Flask(__name__)
app.secret_key =''

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='123456'
app.config['MYSQL_DB']='aula_bd'
app.config['MYSQL_PORT']=3306
db = MySQL(app)

dao = ContatoDao(db)

@app.route('/inicio')
def listar():
    lista_contato = dao.listar()
    return render_template('lista.html',
                           titulo='Contatos',
                           lista=lista_contato)
@app.route('/novo')
def novo():
    return render_template('novo.html',
                           titulo='Novo Contato')

@app.route('/atualizar', methods={'POST',})
def atualizar():
    id = request.form['id']
    nome = request.form['nome']
    celular = request.form['celular']
    email = request.form['email']
    data = request.form['dt_nasc']
    contato = Contato(nome, celular, email, data)
    dao.salvar(contato)
    return redirect('/inicio')


@app.route('/editar/<int:id>')
def editar(id):
    contato = dao.listar_por_id(id)
    return render_template('editar.html',
                           titulo='Atualiza Contato',
                           contato=contato)

@app.route('/deletar/<int:id>')
def deletar(id):
    dao.deletar(id)
    flash('Contato deletando com sucesso.')
    return redirect('/inicio')


app.run(debug=True)