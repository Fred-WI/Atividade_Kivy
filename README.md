
Descrição
Este projeto consiste no desenvolvimento de uma aplicação gráfica em Python utilizando o framework KivyMD para comunicação com servidores Modbus TCP.

A aplicação permite estabelecer conexão com um servidor Modbus TCP e realizar operações de leitura e escrita de dados através de uma interface gráfica amigável.

Funcionalidades Implementadas

* Conexão com servidor Modbus TCP através de endereço IP e porta.
* Leitura de Holding Registers.
* Escrita de Holding Registers.
* Leitura de valores Float (32 bits).
* Escrita de valores Float (32 bits).
* Leitura de bits de um registrador.
* Escrita de bits individuais em registradores.
* Leitura única ou recorrente utilizando o módulo Clock do Kivy.
* Interface gráfica desenvolvida com KivyMD.

Estrutura do Projeto

main.py
Responsável pela interface gráfica e interação do usuário.

clientemodbus.py
Responsável pela comunicação Modbus TCP, leitura, escrita e conversão de dados.

tela.kv
Define os elementos visuais da aplicação utilizando a linguagem KV.

Requisitos

Python 3.x

Bibliotecas necessárias:

* kivy
* kivymd
* pymodbus

Instalação

Instalar as dependências:

pip install kivy
pip install kivymd
pip install pymodbus

Execução

Executar o arquivo principal:

python main.py

Observações

A aplicação foi desenvolvida seguindo o princípio de separação de responsabilidades:

* A classe ClienteMODBUS contém exclusivamente a lógica de comunicação Modbus.
* A interface gráfica apenas realiza chamadas aos métodos da classe ClienteMODBUS.
* Toda a comunicação com o servidor é realizada através do protocolo Modbus TCP.

