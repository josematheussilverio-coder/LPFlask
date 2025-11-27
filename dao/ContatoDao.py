from model import Contato

SQL_SELECT_CONTATOS = 'SELECT * FROM contato'
SQL_SELECT_CONTATO_ID = 'SELECT * FROM contato WHERE id_contato=%s'

SQL_INSERT_CONTATO = ('INSERT INTO contato '
'(nome_contato, cel_contato, email_contato, data_nasc_contato) '
'VALUES (%s, %s, %s, %s)')

SQL_UPDATE_CONTATO = ('UPDATE contato SET nome_contato=%s, '
    'cel_contato=%s, email_contato=%s, data_nasc_contato=%s '
    'WHERE id_contato=%s')

SQL_DELETE_CONTATO = 'DELETE FROM contato WHERE id_contato=%s'

class ContatoDao:

    def __init__(self, db):
        self.__db = db

    def salvar(self, contato):
        cursor = self.__db.connection.cursor()
        # insert
        if contato.id is None:
            cursor.execute(SQL_INSERT_CONTATO,
                (contato.nome, contato.celular,
                 contato.email, contato.data_nasc))
            contato.id = cursor.lastrowid
        else:# update
            cursor.execute(SQL_UPDATE_CONTATO,
                (contato.nome, contato.celular, contato.email,
                 contato.data_nasc, contato.id))

        self.__db.connection.commit()
        return contato

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_CONTATOS)
        lista_tuplas = cursor.fetchall()
        lista_contatos = self.__traduz_contatos(lista_tuplas)
        return lista_contatos

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_CONTATO_ID, (id,))
        tupla = cursor.fetchone()
        cont = self.__traduz_contato(tupla)
        return cont

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_CONTATO, (id,))
        self.__db.connection.commit()

    def __traduz_contato(self, tupla):
        cont = Contato(tupla[1], tupla[2], tupla[3], tupla[4], tupla[0])
        return cont

    def __traduz_contatos(self, lista):
        lista_contatos = []
        for tupla in lista:
            cont = self.__traduz_contato(tupla)
            lista_contatos.append(cont)
        return lista_contatos

