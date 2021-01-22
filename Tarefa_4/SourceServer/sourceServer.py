from logging import root
from threading import local
from const import *
import rpyc
from rpyc.utils.server import ThreadedServer


class SourceServer(rpyc.Service):
	
    exposed_name = "SourceServer"
    serverNotFound = f"Server não encontrado ou não existente."
    serverNotRegister = f"Servidor não registrado."
    List = {}

    def exposed_get_name(self):
        return self.get_service_name()

    def exposed_register(self, serverName, ipAdress, portNum):
        print(root)
        self.List[serverName] = (ipAdress, portNum)
        print(f"Registrando servidor...")
        print(self.List)
        print(f"{self.get_service_name()}:{serverName}")

    def exposed_lookup(self, serverName):
        print(f"Buscando servidor...")
        ListNames = serverName.split(":")
        print(ListNames)
        if len(ListNames) > 0:
            if ListNames[NAMEROOT] in self.List:
                print(f"Verificando se existe segundo nível...")
                if len(ListNames) > 1:
                    secondLayerIP = self.List[ListNames[NAMEROOT]][0]
                    secondLayerPort = self.List[ListNames[NAMEROOT]][1]
                    print(f"Existe segundo nível, conectando no IP: {secondLayerIP} e porta: {secondLayerPort}...")
                    secondLayerServer = rpyc.connect(secondLayerIP, secondLayerPort)
                    print(f"Buscando servidor no segundo nível com o nome: {ListNames[NAMESERVE]}...")
                    return secondLayerServer.root.exposed_lookup(ListNames[NAMESERVE])
                else:
                    print(f"Servidor encontrado.")
                    return self.List[ListNames[NAMEROOT]]
            else:
                print(f"Servidor não encontrado.")
                return self.serverNotFound
        else:
            print(f"Server não encontrado.")
            return self.serverNotFound

    def exposed_re_register(self, serverName, ipAdress, portNum):
        print(f"Registrando servidor novamente...")
        if serverName in self.List:
            print(f"Elemento que vai ser registrado novamente foi encontrado.")
            self.List[serverName] = (ipAdress, portNum)
            print(f"Registrando servidor...")
            print(self.List)
            print(f"{self.get_service_name()}:{serverName}")
        else:
            print(f"Elemento não registrado.")
            return self.serverNotRegister

    def exposed_unregister(self, serverName):
        print(f"Removendo servidor...")
        if serverName in self.List:
            print(f"Servidor a ser removido foi encontrado.")
            ElementoRemovido = self.List[serverName]
            print(
                f"Guardando o elemento: {ElementoRemovido} para ser usado no return...")
            self.List.pop(key=serverName)
            print(f"Removendo elemento do servidor...")

        else:
            print(f"Servidor a ser removido não foi encontrado.")
            return self.serverNotRegister


if __name__ == "__main__":

    print(f"Iniciando o servidor de diretórios na porta: {PORT_SOURCESERVER}...")
    sourceServer = ThreadedServer(SourceServer, port=PORT_SOURCESERVER)
    sourceServer.start()