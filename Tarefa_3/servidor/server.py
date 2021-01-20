import rpyc
import socket
from const import * #-
from rpyc.utils.server import ThreadedServer
 
class Legivel(rpyc.Service):
    value = []

    def exposed_append(self, data):
        print(f"Concatenando valor: {data}")
        self.value = self.value + [data]
        return self.value

    def exposed_value(self):
        print(f"Retornando valor...")
        return self.value
    
    def exposed_remove(self, data):
        if data in self.value:
            print(f"Removendo valor...")
            self.value.remove(data)
            return self.value

    def exposed_search(self, data):
        if data in self.value:
            print(f"Retornando valor e posição...")
            return (data, self.value.index(data) + 1)

if __name__ == "__main__":
    print(f"Criando Servidor Legivel...") 
    server = ThreadedServer(Legivel, port = PORT)
    print(f"Conectando ao servidor de diretório...")  
    conn_ServerDirectory = rpyc.connect(SERVER_DIR,PORT_DIR)
    print(f"Obtendo endereço IP de Legivel...")  
    ipAdress = socket.gethostbyname(socket.gethostname())
    print(f"Registrando no servidor de diretório...") 
    conn_ServerDirectory.root.exposed_registraServer('Legivel',ipAdress,PORT)
    server.start()
