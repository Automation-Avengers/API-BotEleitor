"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
import e_mail.e_mail as e_mail

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def enviar_email(api_lista_usuarios, e_mail, caminho_anexo):
    """
    Função para enviar e-mails com arquivo de produtos em anexo para uma lista de usuários.

    Args:
    - api_lista_usuarios: Função que retorna a lista de usuários no formato JSON.
    - e_mail: Objeto responsável por enviar o e-mail.
    - caminho_anexo: Caminho do arquivo PDF a ser anexado.
    """
    print('Enviando E-mail para a lista de usuários com o arquivo Produtos.pdf em anexo.')
    
    # Chama a API para obter a lista de usuários
    retornoJSON_usuarios = api_lista_usuarios()
    
    # Obtém a lista de usuários a partir do retorno JSON
    lista_produto = retornoJSON_usuarios['dados']
    
    # Loop para enviar o e-mail para cada usuário
    for usuario in lista_produto:
        destinatario = usuario['email']
        print(f'Enviando e-mail para: {destinatario}')
        
        # Define o assunto e conteúdo do e-mail
        assunto = "Lista de Produtos"
        conteudo = "<h1>Sistema Automatizado!</h1> Em anexo, a lista de produtos."
        
        # Envia o e-mail com o arquivo anexo
        e_mail.enviar_email_anexo(destinatario, assunto, conteudo, caminho_anexo)
    
    print('Fim do processamento...')



def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()

    # Opens the BotCity website.
    bot.browse("https://www.botcity.dev")

    arq_anexo = r'C:\Users\matutino\Desktop\API-BotEleitor\BotEleitor\pdf'
    enviar_email(api_lista_usuarios, e_mail, arq_anexo)

    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
