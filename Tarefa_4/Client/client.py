import rpyc
from const import *

class Client:
      
    print(f"Conectando com servidor de diretórios raiz de IP: {SERVER_SOURCESERVER} e porta: {PORT_SOURCESERVER}...")
      
    conn = rpyc.connect(SERVER_SOURCESERVER, PORT_SOURCESERVER) # Connect to the server
      
    print(f"Buscando outros servidores de diretórios...")
      
    #DeptVendas
      
    print(f"Buscando no servidor de diretórios DeptVendas")
    DeptVendas  =  conn.root.exposed_lookup(SERVER_DEPTVENDAS_NAME)
    print(f"Conectando ao servidor de diretórios DeptVendas com IP:{DeptVendas[0]} e porta:{DeptVendas[1]}...")
    connDeptVendas = rpyc.connect(DeptVendas[0], DeptVendas[1])
      
    print(f"Buscando no servidor de diretórios DeptVendas do servidor CalcServer...")
    deptVendasCalcServer  =  connDeptVendas.root.exposed_lookup('CalcServer')

    print(f"Conectando ao CalcServer do servidor de diretórios DeptVendas com IP:{deptVendasCalcServer[0]} e porta:{deptVendasCalcServer[1]}...")
    CalcServerDeptVendas  =  rpyc.connect(deptVendasCalcServer[0], deptVendasCalcServer[1])
      
    print(f"Somando valores do CalcServer do servidor de diretórios DeptVendas, valor A: 1 valor B: 2 ... \nResultado: {CalcServerDeptVendas.root.exposed_soma(1,2)} ")
    print(f"Subtraindo valores do CalcServer do servidor de diretórios DeptVendas, valor A: 4 valor B: 5 ... \nResultado: {CalcServerDeptVendas.root.exposed_sub(4,5)} ")
    print(f"Multiplicando valores do CalcServer do servidor de diretórios DeptVendas, valor A: 56 valor B: 28 ... \nResultado: {CalcServerDeptVendas.root.exposed_mult(56,28)} ")
    print(f"Dividindo valores do CalcServer do servidor de diretórios DeptVendas, valor A: 10 valor B: 1000 ... \nResultado: {CalcServerDeptVendas.root.exposed_div(10,100)} ")
      
    print(f"Buscando no servidor de diretórios DeptVendas do servidor WeatherServer")  
    deptVendasWeatherServer  =  connDeptVendas.root.exposed_lookup('WeatherServer')

    print(f"Conectando ao WeatherServer do servidor de diretórios DeptVendas com IP:{deptVendasWeatherServer[0]} e porta:{deptVendasWeatherServer[1]}...")
    WeatherServerDeptVendas  =  rpyc.connect(deptVendasWeatherServer[0], deptVendasWeatherServer[1])
      
    print(f"Verificando o clima através do servidor WeatherServer")
    print(WeatherServerDeptVendas.root.exposed_append())
      
    print(f"Buscando no servidor de diretórios DeptVendas do servidor TimeServer")
    deptVendasTimeServer  =  connDeptVendas.root.exposed_lookup('TimeServer')
      
    print(f"Conectando ao TimeServer do servidor de diretórios DeptVendas com IP:{deptVendasTimeServer[0]} e porta:{deptVendasTimeServer[1]}...")
    TimeServerDeptVendas  =  rpyc.connect(deptVendasTimeServer[0], deptVendasTimeServer[1])
      
    print(TimeServerDeptVendas.root.exposed_hourNow(f"{conn.root.get_service_name()}:{connDeptVendas.root.get_service_name()}"))

    #DeptRH
    print(f"Buscando no servidor de diretórios DeptRH...")
    DeptRH  =  conn.root.exposed_lookup(SERVER_DEPTRH_NAME)
    print(f"Conectando ao servidor de diretórios DeptRH com IP:{DeptRH[0]} e porta:{DeptRH[1]}")
    connDeptRH = rpyc.connect(DeptRH[0], DeptRH[1])

    print(f"Buscando no servidor de diretórios DeptRH do servidor CalcServer...")
    deptRHCalcServer  =  connDeptRH.root.exposed_lookup('CalcServer')

    print(f"Conectando ao CalcServer do servidor de diretórios DeptRH com IP:{deptRHCalcServer[0]} e porta:{deptRHCalcServer[1]}...")
    CalcServerDeptRH  =  rpyc.connect(deptRHCalcServer[0], deptRHCalcServer[1])
      
    print(f"Somando valores do CalcServer do servidor de diretórios DeptRH, valor A: 1 valor B: 2 ... \nResultado: {CalcServerDeptRH.root.exposed_soma(1,2)} ")
    print(f"Subtraindo valores do CalcServer do servidor de diretórios DeptRH, valor A: 4 valor B: 5 ... \nResultado: {CalcServerDeptRH.root.exposed_sub(4,5)} ")
    print(f"Multiplicando valores do CalcServer do servidor de diretórios DeptRH, valor A: 56 valor B: 28 ... \nResultado: {CalcServerDeptRH.root.exposed_mult(56,28)} ")
    print(f"Dividindo valores do CalcServer do servidor de diretórios DeptRH, valor A: 10 valor B: 1000 ... \nResultado: {CalcServerDeptRH.root.exposed_div(10,100)} ")
    
    print(f"Buscando no servidor de diretórios DeptRH do servidor ValeuServer do servidor de diretórios DeptVendas...")  
    deptRHWeatherServer  =  connDeptRH.root.exposed_lookup(f"{SERVER_DEPTVENDAS_NAME}:WeatherServer")

    print(f"Conectando ao WeatherServer do servidor de diretórios DeptVendas atraves do DeptRH com IP:{deptRHWeatherServer[0]} e porta:{deptRHWeatherServer[1]}...")
    WeatherServerDeptRH  =  rpyc.connect(deptRHWeatherServer[0], deptRHWeatherServer[1])
      
    print(f"Verificando o clima através do servidor WeatherServer...")
    print(WeatherServerDeptVendas.root.exposed_append())
        
    print(f"Buscando no servidor de diretórios DeptRH do servidor TimeServer...")
    deptRHTimeServer  =  connDeptRH.root.exposed_lookup('TimeServer')
      
    print(f"Conectando ao TimeServer do servidor de diretórios DeptRH com IP:{deptRHTimeServer[0]} e porta:{deptRHTimeServer[1]}...")
    TimeServerDeptRH  =  rpyc.connect(deptRHTimeServer[0], deptRHTimeServer[1])
    print(TimeServerDeptRH.root.exposed_hourNow(f"{conn.root.get_service_name()}:{connDeptRH.root.get_service_name()}"))