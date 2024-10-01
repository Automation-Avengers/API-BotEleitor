from repository import database

# Inserir eleitor
def criar_eleitor(eleitor):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = (
            f"INSERT INTO eleitor(cpf, nome, data_nascimento, nome_mae, cep, nro_endereco, nro_titulo, situacao, secao, zona, local_votacao, endereco_votacao, bairro, municipio_uf, pais) "
            f"VALUES ('{eleitor['cpf']}', '{eleitor['nome']}', '{eleitor['data_nascimento']}', '{eleitor['nome_mae']}', '{eleitor['cep']}', '{eleitor['nro_endereco']}', "
            f"'{eleitor['nro_titulo']}', '{eleitor['situacao']}', '{eleitor['secao']}', '{eleitor['zona']}', '{eleitor['local_votacao']}', '{eleitor['endereco_votacao']}', "
            f"'{eleitor['bairro']}', '{eleitor['municipio_uf']}', '{eleitor['pais']}')"
        )
        
        print(sql)
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na inclusão: {ex}')
    finally:
        cursor.close()
        conect.close()

# Existe eleitor
def existe_eleitor(cpf):
    conect = database.criar_db()
    cursor = conect.cursor()
    try:
        cursor.execute("SELECT COUNT(1) FROM eleitor WHERE cpf = %s", (cpf,))
        return cursor.fetchone()[0] > 0
    except Exception as ex:
        print(f'Erro ao verificar eleitor: {ex}')
        return False
    finally:
        cursor.close()
        conect.close()

# Obter eleitor
def obter_eleitor_cpf(cpf):
    # Declar uma tupla vazia
    eleitor = ()
    try:
        conect = database.criar_db()
        cursor = conect.cursor() 
        sql = f"SELECT * FROM eleitor WHERE cpf = '{cpf}'" 
        cursor.execute(sql)
        eleitor = cursor.fetchone()
    except Exception as ex:
        print(f'Erro na verificacao da existencia do produto: {ex}')
    finally:
        cursor.close()
        conect.close()
    return eleitor


def listar_eleitores():
    eleitores = list()
    try:
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = 'SELECT * FROM eleitor ORDER BY nome'  # Ordenando por nome ou outro critério
        cursor.execute(sql)
        lista_eleitor = cursor.fetchall()
        
        # Tratar dados para uma estrutura JSON
        for eleitor in lista_eleitor:
            eleitores.append(
                {
                    'cpf': eleitor[0],
                    'nome': eleitor[1],
                    'data_nascimento': eleitor[2],
                    'nome_mae': eleitor[3],
                    'cep': eleitor[4],
                    'nro_endereco': eleitor[5],
                    'nro_titulo': eleitor[6],
                    'situacao': eleitor[7],
                    'secao': eleitor[8],
                    'zona': eleitor[9],
                    'local_votacao': eleitor[10],
                    'endereco_votacao': eleitor[11],
                    'bairro': eleitor[12],
                    'municipio_uf': eleitor[13],
                    'pais': eleitor[14]
                }
            )
    except Exception as ex:
        print(f'Erro: Listar eleitores: {ex}')
    finally:
        cursor.close()
        conect.close()
    
    return eleitores


# Atualizar eleitor
def atualizar_eleitor(eleitor):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()

        # Montar a query de atualização
        sql = (
            f"UPDATE eleitor SET "
            f"nome = '{eleitor['nome']}', "
            f"data_nascimento = '{eleitor['data_nascimento']}', "
            f"nome_mae = '{eleitor['nome_mae']}', "
            f"cep = '{eleitor['cep']}',"
            f"nro_endereco = '{eleitor['nro_endereco']}', "
            f"nro_titulo = '{eleitor['nro_titulo']}', "
            f"situacao = '{eleitor['situacao']}', "
            f"secao = '{eleitor['secao']}', "
            f"zona = '{eleitor['zona']}', "
            f"local_votacao = '{eleitor['local_votacao']}', "
            f"endereco_votacao = '{eleitor['endereco_votacao']}', "
            f"bairro = '{eleitor['bairro']}', "
            f"municipio_uf = '{eleitor['municipio_uf']}', "
            f"pais = '{eleitor['pais']}' "
            f"WHERE cpf = '{eleitor['cpf']}'"
        )

        print(sql)  # Verifique a consulta SQL gerada

        cursor.execute(sql)
        conect.commit()  # Assegure-se de que o commit está sendo chamado
    except Exception as ex:
        conect.rollback()  # Desfaz as mudanças em caso de erro
        print(f'Erro: Falha na alteração: {ex}')
    finally:
        cursor.close()
        conect.close()


# Deletar eleitor 
def deletar_eleitor(cpf):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f'DELETE FROM eleitor WHERE cpf = {cpf}'
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na deleção do produto: {ex}')
    finally:
        cursor.close()
        conect.close()
# fim: listar_eleitores()

# fim: obter_eleitor_cpf(cpf)


# Fim: criar_eleitor(produto)