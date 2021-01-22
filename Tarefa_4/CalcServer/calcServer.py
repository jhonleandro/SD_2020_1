import rpyc
import socket
from const import * #-
from rpyc.utils.server import ThreadedServer
 
class CalcServer(rpyc.Service):

    def exposed_soma(self, valorA, valorB):
        print(f"Somando {valorA} e {valorB}...")
        return valorA + valorB
  
    def exposed_sub(self, valorA, valorB):
        print(f"Subtraindo {valorA} e {valorB}...")
        return valorA - valorB

    def exposed_mult(self, valorA, valorB):
        print(f"Multiplicando {valorA} e {valorB}...")
        return valorA * valorB

    def exposed_div(self, valorA, valorB):
        print(f"Dividindo {valorA} e {valorB}...")
        return valorA / valorB
           
if __name__ == "__main__":
    print(f"Gerando servidor {SERVER_CALCSERVER_NAME}...") 
    calcServer = ThreadedServer(CalcServer, port = PORT_CALCSERVER)
    print(f"Conectando ao servidor de diretórios DeptVendas...")  
    conn_serverDeptVendas = rpyc.connect(SERVER_DEPTVENDAS,PORT_DEPTVENDAS)
    print(f"Conectando ao servidor de diretórios DeptRH...")  
    conn_serverDeptRH = rpyc.connect(SERVER_DEPTRH,PORT_DEPTRH)
    print(f"Obtendo ipadress da {SERVER_CALCSERVER_NAME}")  
    ipAdress = socket.gethostbyname(socket.gethostname())
    print(f"Registrando no servidor de diretórios DeptVendas...") 
    conn_serverDeptVendas.root.exposed_register(SERVER_CALCSERVER_NAME,ipAdress,PORT_CALCSERVER)
    print(f"Registrando no servidor de diretórios DeptRH...") 
    conn_serverDeptRH.root.exposed_register(SERVER_CALCSERVER_NAME,ipAdress,PORT_CALCSERVER)
    calcServer.start()