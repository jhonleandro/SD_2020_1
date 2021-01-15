from const import *
import rpyc
from rpyc.utils.server import ThreadedServer


class Server_Directory(rpyc.Service):
    
    servidor_inexistente = f"Servidor não encontrado"
    
    lista_diretorio = {}
    
    def __init__(self, lista):
        self.lista_diretorio = lista

    def exposed_registraServer(self, serverName, ipAdress, portNum):
        self.lista_diretorio.update({serverName : (ipAdress, portNum)})
        print(f"Registrando Servidor...")
        print(self.lista_diretorio)

    def exposed_buscaServer(self, serverName):
        print(f"Buscando Servidor...")
        print({serverName})
        print(f"Tem na lista: {serverName in self.lista_diretorio}")

        if  serverName in self.lista_diretorio:
            print(f"Servidor encontrado")
            print(self.lista_diretorio)
            return self.lista_diretorio[serverName]
        else:
            print(f"Servidor não encontrado")
            print(self.lista_diretorio)
            return self.servidor_inexistente


if __name__ == "__main__":
    lista_diretorio = {}
    print(f"Iniciando servidor de diretórios na porta: {PORT_DIR}")
    server_dir = ThreadedServer(Server_Directory(lista_diretorio), port=12310)
    server_dir.start()