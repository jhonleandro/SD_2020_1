from logging import root
import rpyc
import socket
from datetime import datetime, time
from const import * #-
from rpyc.utils.server import ThreadedServer
 
class TimeServer(rpyc.Service):
  
    def exposed_hourNow(self, nameServer):
        return f"FQN:{nameServer}:{self.get_service_name()} Hour:{datetime.now()}"

   
           
if __name__ == "__main__":

    print(f"Gerando o servidor TimeServer...") 
    timeServer = ThreadedServer(TimeServer, port = PORT_TIMESERVER)
    print(f"Conectando ao servidor de diretórios DeptVendas...")  
    conn_serverDeptVendas = rpyc.connect(SERVER_DEPTVENDAS,PORT_DEPTVENDAS)
    print(f"Conectando ao servidor de diretórios DeptRH...")  
    conn_serverDeptRH = rpyc.connect(SERVER_DEPTRH,PORT_DEPTRH)
    print(f"Obtendo o IP do servidor TimeServer...")  
    ipAdress = socket.gethostbyname(socket.gethostname())
    print(f"Registrando no servidor de diretórios DeptVendas...") 
    conn_serverDeptVendas.root.exposed_register('TimeServer',ipAdress,PORT_TIMESERVER)
    print(f"Registrando no servidor de diretórios DeptRH...") 
    conn_serverDeptRH.root.exposed_register('TimeServer',ipAdress,PORT_TIMESERVER)

    timeServer.start()