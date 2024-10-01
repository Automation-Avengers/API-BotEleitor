from fpdf import FPDF
import os

def gerar_pdf(caminho_diretorio, nro_cpf, titulo, situacao, secao, zona, local_votacao, endereco, bairro, municipio_uf, pais):
 
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Informações do Título Eleitoral", ln=True, align='C')

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
    
    nome_arquivo = f"{nro_cpf}_titulo.pdf"
 
    caminho_completo = os.path.join(caminho_diretorio, nome_arquivo)

    if not os.path.exists(caminho_diretorio):
        os.makedirs(caminho_diretorio)
 
    pdf.output(caminho_completo)
    
    print(f"PDF gerado com sucesso em: {caminho_completo}")

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
 
    gerar_pdf(caminho_diretorio, nro_cpf, titulo, situacao, secao, zona, local_votacao, endereco, bairro, municipio_uf, pais)
