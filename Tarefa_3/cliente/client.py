import rpyc
from const import *

class Client:
    print(f"Iniciando conexão com servidor de diretórios de IP: {SERVER_DIR} e porta: {PORT_DIR}")
    conn = rpyc.connect(SERVER_DIR, PORT_DIR) # Connect to the server
  
    print(f"Fazendo busca por Legivel...")
    nome_diretorio  =  conn.root.exposed_buscaServer('Legivel')
  
    print(f"Busca finalizada, resultado: ")
    print(nome_diretorio) # Print the result