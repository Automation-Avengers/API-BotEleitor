from flask import Flask, make_response, jsonify, request, Response
import mysql.connector
import sys
import os

import repository.eleitor as eleitor
import repository.database as database
import repository.usuario as usuario

# Instanciar 
app_api = Flask('api_database')
app_api.config['JSON_SORT_KEYS'] = False

# --------------------------------------------------------
#           Inicio: Serviços da api eleitor
# --------------------------------------------------------

# Incluir um novo Eleitor
@app_api.route('/eleitor', methods=['POST'])
def criar_eleitor():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    eleitor_json = request.json # corpo da requisição
    try:
        eleitor.criar_eleitor(eleitor_json)
        sucesso = True
        _mensagem = 'Eleitor inserido com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Inclusao do eleitor: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem 
        )
    )

# Obter eleitor pelo CPF
@app_api.route('/eleitor/cpf/<string:cpf>', methods=['GET'])
def obter_eleitor(cpf):
    eleitor = obter_eleitor(cpf)
    if eleitor:
        return jsonify(status=True, dados=eleitor)
    else:
        return jsonify(status=False, mensagem='Eleitor não encontrado'), 404

# Listar eleitor
@app_api.route('/eleitor', methods=['GET'])
def lista_eleitores():
    lista_eleitor = eleitor.listar_eleitores()  # Implemente essa função para obter os eleitores
    if len(lista_eleitor) == 0:
        sucesso = False
        _mensagem = 'Lista de eleitores vazia'
    else:
        sucesso = True
        _mensagem = 'Lista de eleitores obtida com sucesso'

    # Construir um Response
    return make_response(
        jsonify(
            status=sucesso, 
            mensagem=_mensagem,
            dados=lista_eleitor
        )
    )

# Obter eleitor
@app_api.route('/eleitor/<string:cpf>', methods=['GET'])
def obter_eleitor_por_cpf(cpf):
    sucesso = False
    eleitor_cpf = {}
    
    try:
        if eleitor.existe_eleitor(cpf):
            eleitor_tuple = eleitor.obter_eleitor_cpf(cpf)
            # Converter a tupla para um dicionário com mapeamento correto
            eleitor_cpf = {
                'cpf': eleitor_tuple[0],
                'nome': eleitor_tuple[1],
                'data_nascimento': eleitor_tuple[2],
                'nome_mae': eleitor_tuple[3],
                'cep': eleitor_tuple[4],
                'nro_endereco': eleitor_tuple[5],
                'nro_titulo': eleitor_tuple[6],
                'situacao': eleitor_tuple[7],
                'secao': eleitor_tuple[8],
                'zona': eleitor_tuple[9],
                'local_votacao': eleitor_tuple[10],
                'endereco_votacao': eleitor_tuple[11],
                'bairro': eleitor_tuple[12],
                'municipio_uf': eleitor_tuple[13],
                'pais': eleitor_tuple[14]
            }
            sucesso = True
            _mensagem = 'Eleitor encontrado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Eleitor não existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro ao buscar eleitor: {ex}'
    
    return make_response(
        jsonify(status=sucesso, mensagem=_mensagem, dados=eleitor_cpf)
    )
  

# Atualizar eleitor
@app_api.route('/eleitor', methods=['PUT'])
def atualizar_eleitor_api():
    # Captura o JSON com os dados enviados pelo cliente
    eleitor_json = request.get_json()  # Obtém o corpo da requisição com os dados do eleitor
    
    cpf = eleitor_json['cpf']  # Obtém o CPF do eleitor
    
    try:
        # Verifica se o eleitor existe
        if eleitor.existe_eleitor(cpf):
            # Atualiza o eleitor com os dados recebidos
            eleitor.atualizar_eleitor(eleitor_json)  # Passa o JSON como parâmetro
            sucesso = True
            _mensagem = 'Eleitor atualizado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Eleitor não existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro ao atualizar eleitor: {ex}'
    
    return make_response(
        jsonify(
            status=sucesso,
            mensagem=_mensagem
        )
    )


# Deletar eleitor  
@app_api.route('/eleitor/<string:cpf>', methods=['DELETE'])
def deletar_eleitor(cpf):
    try:
        if eleitor.existe_eleitor(cpf) == True:
            eleitor.deletar_eleitor(cpf)
            sucesso = True
            _mensagem = 'Eleitor deletado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Eleitor nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Exclusao de eleitor: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )
# -- Fim: Serviços da api eleitor ------------------------


# --------------------------------------------------------
#           Inicio: Serviços da api Usuario
# --------------------------------------------------------

# Inserir usuário
@app_api.route('/usuario', methods=['POST'])
def criar_usuario():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    usuario_json = request.json # corpo da requisição
    id_usuario=0
    try:
        id_usuario = usuario.criar_usuario(usuario_json)
        sucesso = True
        _mensagem = 'Usuario inserido com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Inclusao do usuario: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem ,
                id = id_usuario
        )
    )
# Fim: criar_usuario()

# Atualizar usuário
@app_api.route('/usuario', methods=['PUT'])
def atualizar_usuario():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    usuario_json = request.json # corpo da requisição
    id = int(usuario_json['id'])
    try:
        if usuario.existe_usuario(id) == True:
            usuario.atualizar_usuario(usuario_json)
            sucesso = True
            _mensagem = 'Usuario alterado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Usuario nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Alteracao do usuario: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )

# Deletar usuário
@app_api.route('/usuario/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    try:
        if usuario.existe_usuario(id) == True:
            usuario.deletar_usuario(id)
            sucesso = True
            _mensagem = 'Usuario deletado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Usuario nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Exclusao de usuario: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )

# Serviço: Obter usuário pelo id
@app_api.route('/usuario/<int:id>', methods=['GET'])
def obter_usuario_id(id):
    # Declarando uma tupla vazia
    usuario_id = ()
    sucesso = False
    if usuario.existe_usuario(id) == True:
        usuario_id = usuario.obter_usuario_id(id)
        sucesso = True
        _mensagem = 'Usuario encontrado com sucesso'
    else:
        sucesso = False
        _mensagem = 'Usuario existe'
    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = usuario_id
        )
    )
# Fim: obter_usuario_id(id)

# Serviço: Obter a lista de usuário
@app_api.route('/usuario', methods=['GET'])
def lista_usuarios():
    lista_usuario = list()
    lista_usuario = usuario.lista_usuarios()
    if len(lista_usuario) == 0:
        sucesso = False
        _mensagem = 'Lista de usuario vazia'
    else:
        sucesso = True
        _mensagem = 'Lista de usuario'

    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = lista_usuario
        )
    )
# Fim: lista_usuarios()

# -- Fim: Serviços da api usuário ------------------------

# Levantar/Executar API REST: api_database
app_api.run()



