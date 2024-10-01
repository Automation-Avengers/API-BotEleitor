from fpdf import FPDF
import os

# Função para gerar o arquivo PDF
def gerar_pdf(caminho_diretorio, nro_cpf, titulo, situacao, secao, zona, local_votacao, endereco, bairro, municipio_uf, pais):
    # Criar uma instância do FPDF
    pdf = FPDF()
    pdf.add_page()
    
    # Definir o título do documento
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Informações do Título Eleitoral", ln=True, align='C')

    # Adicionar os detalhes no PDF
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt=f"Número do título: {titulo}", ln=True)
    pdf.cell(200, 10, txt=f"Situação: {situacao}", ln=True)
    pdf.cell(200, 10, txt=f"Seção: {secao}", ln=True)
    pdf.cell(200, 10, txt=f"Zona: {zona}", ln=True)
    pdf.cell(200, 10, txt=f"Local de votação: {local_votacao}", ln=True)
    pdf.cell(200, 10, txt=f"Endereço: {endereco}", ln=True)
    pdf.cell(200, 10, txt=f"Bairro: {bairro}", ln=True)
    pdf.cell(200, 10, txt=f"Município/UF: {municipio_uf}", ln=True)
    pdf.cell(200, 10, txt=f"País: {pais}", ln=True)
    
    # Definir o nome do arquivo no formato nroCPF_titulo.pdf
    nome_arquivo = f"{nro_cpf}_titulo.pdf"
    
    # Definir o caminho completo do arquivo
    caminho_completo = os.path.join(caminho_diretorio, nome_arquivo)

    # Verificar se o diretório existe, caso contrário, criar
    if not os.path.exists(caminho_diretorio):
        os.makedirs(caminho_diretorio)
    
    # Salvar o arquivo no diretório especificado
    pdf.output(caminho_completo)
    
    print(f"PDF gerado com sucesso em: {caminho_completo}")


# Exemplo de uso da função
if __name__ == "__main__":
 
    caminho_diretorio = "C:\provafinal\API-BotEleitor\BotEleitor\pdf"

    nro_cpf = "57014540297"
    titulo = "123456789"
    situacao = "REGULAR"
    secao = "123"
    zona = "456"
    local_votacao = "Escola Municipal"
    endereco = "Rua ABC, 123"
    bairro = "Centro"
    municipio_uf = "São Paulo/SP"
    pais = "Brasil"
    
    # Gerar o PDF
    gerar_pdf(caminho_diretorio, nro_cpf, titulo, situacao, secao, zona, local_votacao, endereco, bairro, municipio_uf, pais)
