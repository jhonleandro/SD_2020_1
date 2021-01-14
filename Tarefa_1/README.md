# Tarefa 1 - Implementação de Referências Remotas

As máquinas são iniciadas na ordem: servidor, cliente_2, cliente_1. O servidor é iniciado, o cliente_2 é iniciado e fica aguardando dados do cliente_1. O cliente_1 é iniciado, ele cria a referência remota para o servidor, e também cria uma lista de dados e adiciona conteúdo('Client 1') nela, o cliente_2 que estava esperando recebe a referência remota. O cliente_2 desempacota a lista e adiciona conteúdo('Client 1') nela, então ele faz conexão com o servidor e manda um STOP.
