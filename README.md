# tuple_space
Essa é uma implemetação de um espaço de tupla distribuido, onde são levantandos 3 serviços os quais se comunicam utilizando o protocolo de raft para manter um consenso entre os valores do espaço.
# Para utilização
É necessario instalar o gerenciador de dempedencias para python Poetry
pipx install poetry
Também é necessario instalar a biblioteca PySyncObj
pip install pysyncobj
# Para execução
Para executar basta rodar o comando
poetry run python t2_tuple_space 8000 8001 8002
poetry run python t2_tuple_space 8001 8000 8002
poetry run python t2_tuple_space 8002 8000 8001

O prompt de execução indicara como utilizar o espaço de tuplas
