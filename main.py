from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from clientemodbus import ClienteMODBUS

class MyWidget(MDScreen):
    pass

class TelaApp(MDApp):

    def build(self):

        self.cliente = None
        self.evento = None

        return MyWidget()

    def conectar(self):

        ip = self.root.ids.ip.text
        porta = int(self.root.ids.porta.text)

        self.cliente = ClienteMODBUS(ip, porta)

        self.root.ids.resultado.text = "Conectado"

    def ler(self):

        addr = int(self.root.ids.endereco.text)

        valor = self.cliente.leitura(addr)

        self.root.ids.resultado.text = str(valor)

    def escrever(self):

        addr = int(self.root.ids.endereco.text)
        valor = int(self.root.ids.valor.text)

        status = self.cliente.escrita(addr, valor)

        self.root.ids.resultado.text = str(status)


TelaApp().run()