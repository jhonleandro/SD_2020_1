from const import *
import rpyc
from rpyc.utils.server import ThreadedServer

class ServerDirectory(rpyc.Service):
    
    servidorInexistente = f"Servidor não encontrado..."
    servidorNaoRegistrado = f"Servidor não registrado..."
    
    listaDiretorio = {}
    
    def __init__(self, lista):
        self.listaDiretorio = lista

    def exposed_registraServidor(self, serverName, ipAdress, portNum):
        self.listaDiretorio.update({serverName : (ipAdress, portNum)})
        print(f"Registrando Servidor...")
        print(self.listaDiretorio)

    def exposed_buscaServidor(self, serverName):
        print(f"Buscando Servidor...")

        if  serverName in self.listaDiretorio:
            print(f"Servidor encontrado...")
            print(self.listaDiretorio)
            return self.listaDiretorio[serverName]
        else:
            print(f"Servidor não encontrado...")
            print(self.listaDiretorio)
            return self.servidorInexistente
    
    def exposed_registraServidorNovamente(self, serverName, ipAdress, portNum):
        print(f"Registrando Servidor Novamente...")
        
        if serverName in self.listaDiretorio:
            print(f"Achou item que vai ser registrado novamente...")
            self.listaDiretorio[serverName] = (ipAdress, portNum)
            return self.listaDiretorio[serverName]
        else:
            print(f"Item não registrado...")
            return self.servidorNaoRegistrado

    def exposed_removaServidor(self, serverName):
        print(f"Removendo Servidor...")
        
        if  serverName in self.listaDiretorio:
            print(f"Servidor a ser removido foi encontrado...")
            elementoRemovido = self.listaDiretorio[serverName]
            print(f"Guardando o elemento: {elementoRemovido} para ser retornado...")
            self.listaDiretorio.pop(key=serverName)
            print(f"Removendo elemento do servidor...")
            return elementoRemovido
        else:
            print(f"Servidor a ser removido não foi encontrado...")
            return self.serverNaoRegistrado


if __name__ == "__main__":
    listaDiretorio = {}
    print(f"Iniciando servidor de diretórios na porta: {PORT_DIR}")
    server_dir = ThreadedServer(ServerDirectory(listaDiretorio), port=12310)
    server_dir.start()
