import rpyc
import socket
import random
from const import * #-
from rpyc.utils.server import ThreadedServer
 
class WeatherServer(rpyc.Service):
    
    badWeather = f"O tempo hoje será nublado, é melhor levar um guarda-chuva."
    goodWeather = f"O tempo hoje será ótimo!"
  
    def exposed_append(self): 
        if random.randrange(1,10)%2 = 0:
            return self.goodWeather
        else:
            return self.badWeather
        
if __name__ == "__main__":
    print(f"Gerando servidor WeatherServer...") 
    weatherServer = ThreadedServer(WeatherServer, port = PORT_WEATHERSERVER)
    print(f"Conectando ao servidor de diretórios DeptVendas...")  
    conn_serverDeptVendas = rpyc.connect(SERVER_DEPTVENDAS,PORT_DEPTVENDAS)
    print(f"Obtendo o IP do servidor WeatherServer...")  
    ipAdress = socket.gethostbyname(socket.gethostname())
    print(f"Registrando no servidor de diretórios DeptVendas...") 
    conn_serverDeptVendas.root.exposed_register('WeatherServer',ipAdress,PORT_WEATHERSERVER)
    weatherServer.start()