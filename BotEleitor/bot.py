
# Import for the Web Bot
from botcity.web import WebBot, Browser, By
import requests
# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
#configuracao chromer
from webdriver_manager.chrome import ChromeDriverManager
#configurar http, antes tem executar terminal: pip install botcity-http-plugin
from botcity.plugins.http import BotHttpPlugin
from datetime import datetime

import planilha.planilha as planilha
import e_mail.e_mail as e_mail
import pdf.pdf as pdf
import pdf


# Definir as funções

def acessar_site(bot):
 # Acessar o site do TSE
    bot.browse("https://www.tse.jus.br/servicos-eleitorais/titulo-eleitoral")
    
    # Aguardar o carregamento do site
    bot.wait(2000)  # Tempo extra para garantir que a página esteja carregada

    

def main():
    bot = WebBot()

    # Configurar se deve rodar em modo headless
    bot.headless = False

    # Configurar o navegador para ser o Chrome
    bot.browser = Browser.CHROME

    # Instalar e configurar o ChromeDriver
    bot.driver_path = ChromeDriverManager().install()

    # Acessar o site e tentar clicar no item do menu
    acessar_site(bot)
    
    # Esperar alguns segundos antes de finalizar
    bot.wait(3000)

    # Gerar o PDF
    pdf.gerar_pdf()

    # Finalizar e limpar o navegador
    bot.stop_browser()


if __name__ == '__main__':
    main()