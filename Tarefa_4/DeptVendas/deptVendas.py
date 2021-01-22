from logging import root
from const import *
import rpyc
import socket
from rpyc.utils.server import ThreadedServer


class DeptVendas(rpyc.Service):
    
    exposed_name = "DeptVendas"
    serverNotFound = f"Servidor não encontrado ou não existente."
    serverNotRegister = f"Servidor não registrado."
    List = {}

    def exposed_get_name(self):
        return self.get_service_name()
    
    def exposed_register(self, serverName, ipAdress, portNum):
        print(root)
        NameRoot = SERVER_SOURCESERVER_NAME
        self.List[serverName] = (ipAdress, portNum)
        print(f"Registrando servidor...")
        print(self.List)
        print(f"{NameRoot}:{self.get_service_name()}:{serverName}")
        
    def exposed_lookup(self, serverName):
        print(f"Buscando servidor...")
        if  serverName in self.List:
            print(f"Servidor encontrado.")
            return self.List[serverName]
        else:
            print(f"Servidor local não encotrado, voltando ao servidor raiz...")
            firstLayerServer = rpyc.connect(SERVER_SOURCESERVER,PORT_SOURCESERVER)
            return firstLayerServer.root.exposed_lookup(serverName)
        
    def exposed_re_register(self, serverName, ipAdress, portNum):
        print(f"Registrando servidor novamente...")
        if serverName in self.List:
            print(f"Elemento que vai ser registrado novamente foi encontrado.")
            NameRoot = SERVER_SOURCESERVER_NAME
            self.List[serverName] = (ipAdress, portNum)
            print(f"Registrando servidor...")
            print(self.List)
            print(f"{NameRoot}:{self.get_service_name()}:{serverName}")
        else:
            print(f"Elemento não registrado.")
            return self.serverNotRegister
        

    def exposed_unregister(self, serverName):
        print(f"Removendo servidor...")
        if  serverName in self.List:
            print(f"Servidor a ser removido foi encontrado.")
            ElementoRemovido = self.List[serverName]
            print(f"Guardando o elemento: {ElementoRemovido} para ser usado no return...")
            self.List.pop(key=serverName)
            print(f"Removendo elemento do servidor...")
            return ElementoRemovido
        else:
            print(f"Servidor a ser removido não foi encontrado.")
            return self.serverNotRegister
        

if __name__ == "__main__":
    
    print(f"Iniciando o servidor de diretórios DeptVendas nível 2 na porta: {PORT_DEPTVENDAS}...")
    serverDeptVendas = ThreadedServer(DeptVendas, port = PORT_DEPTVENDAS)
    print(f"Conectando ao servidor de diretórios raiz...")  
    conn_sourceServer = rpyc.connect(SERVER_SOURCESERVER,PORT_SOURCESERVER)
    print(f"Obtendo o IP do servidor de diretórios DeptVendas...")  
    ipAdress = socket.gethostbyname(socket.gethostname())
    print(f"Registrando no servidor de diretórios DeptVendas no servidor de diretórios raiz...") 
    conn_sourceServer.root.exposed_register('DeptVendas',ipAdress,PORT_DEPTVENDAS)
    serverDeptVendas.start()