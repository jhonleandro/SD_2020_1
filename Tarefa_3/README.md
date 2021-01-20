# Tarefa 3 - Melhorias no servidor de diretório

Nessa tarefa há 3 instâncias: cliente, servidor e servidor de diretório. Em cada pasta há 2 arquivos, sendo um deles, o const.py comum todos, e outro arquivo correspondendo ao nome da pasta e instância. O objetivo é que servidor registre seu IP, sua porta e um nome no servidor de diretório, então o cliente irá usar o nome do servidor para obter o IP e a porta por meio de uma chamada remota no servidor de diretório. E por fim, o cliente fará algumas chamadas no servidor para mostrar que obteve acesso.

## const.py

O const.py é um arquivo onde armazenamos constantes que são comuns para as 3 instâncias, tais como IPs e Portas.

## client.py

O client.py é um arquivo onde há código, ele se conecta ao servidor de diretório e realiza uma busca pelo servidor, através do nome deste e finalizando mostrando o acesso.

## server.py

O server.py assim como o client.py é um arquivo onde há código, nele é criado o servidor "Legivel", que é o servidor que o client.py busca. Após a criação temos a conexão com o servidor diretório, ele registra os seus dados(IP, porta e nome) no servidor diretório.

### Melhorias

Novas funcionalidades: excluir elementos da lista(exposed_remove) e consultar elementos da lista(exposed_search).

## server_dir.py

Assim como os arquivos anteriores, esse é um arquivo onde há código. Ele é quem o faz o papel de intermediário entre servidor e cliente. Ele tem duas funções básicas, a primeira é o registro de servidores, ele pega os dados(IP, porta e nome) que são passados pelo servidor e registra. A segunda função é busca de servidores, o cliente passa o nome do servidor e então o servidor de diretório faz a busca nos registros, se houver um servidor com nome correspondente, os dados(IP, porta e nome) são passados ao cliente.

### Melhorias

Novas funcionalidades: registrar um nome já existente(exposed_registraServidorNovamente) e excluir elementos da lista(exposed_removaServidor).
Obs: a melhoria "Evitar o lookup de nomes não existentes" já existia dentro de (exposed_buscaServidor).
