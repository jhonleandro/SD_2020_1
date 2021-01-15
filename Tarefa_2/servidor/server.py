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
    print(f"Retornando valor")
    return self.value

if __name__ == "__main__":
  print(f"Criando Servidor Legivel...") 
  server = ThreadedServer(Legivel, port = PORT)
  print(f"Conectando ao servidor de diretório...")  
  conn_serverDir = rpyc.connect(SERVER_DIR,PORT_DIR)
  print(f"Obtendo ipadress da Legivel...")  
  ipAdress = socket.gethostbyname(socket.gethostname())
  print(f"Registrando no servidor de diretório...") 
  conn_serverDir.root.exposed_registraServer('Legivel',ipAdress,PORT)
  server.start()