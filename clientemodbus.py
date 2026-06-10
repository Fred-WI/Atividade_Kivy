from pymodbus.client import ModbusTcpClient
from time import sleep

class ClienteMODBUS():
     
    def __init__(self, server_ip, porta, scan_time=1):
        # Cria o cliente TCP
        self._cliente = ModbusTcpClient(host=server_ip, port=porta)
        self._scan_time = scan_time
    

    def leitura(self, addr):

        # Holding Register (função 03)
        resp = self._cliente.read_holding_registers(address=addr, count=1, device_id=1)
        if resp and not resp.isError():
            return resp.registers[0]
        return None
        
    def escrita(self, addr, valor):

        # Holding Register (função 06 - single)
       
        resp = self._cliente.write_register(address=addr, values=valor, device_id=1)
        return bool(resp and not resp.isError())
        
        
    def leitura_float(self, addr):
         # Lê 2 Holding Registers consecutivos
        resp = self._cliente.read_holding_registers(
        address=addr,
        count=2,
        device_id=1)

        if resp and not resp.isError():
            valor = self._cliente.convert_from_registers(resp.registers,self._cliente.DATATYPE.FLOAT32)
            return valor
        return None


    def escrita_float(self, addr, valor):
        regs = self._cliente.convert_to_registers(valor,self._cliente.DATATYPE.FLOAT32)
        resp = self._cliente.write_registers(address=addr, values=regs, device_id=1)
        return bool(resp and not resp.isError()) 
    
    def leitura_bits(self, addr):

        # Lê 1 Holding Register
        resp = self._cliente.read_holding_registers(
            address=addr,
            count=1,
            device_id=1
        )

        valor = self._cliente.convert_from_registers(resp.registers,self._cliente.DATATYPE.BITS)

        if resp and not resp.isError():
            return valor
        return None




    def escrita_bit(self, addr, num_bit, dado):

        # Lê o registrador atual
        resp = self._cliente.read_holding_registers(
            address=addr,
            count=1,
            device_id=1
        )

        valor = self.leitura_bits
        valor[num_bit] = dado
        reg = self._cliente.convert_to_registers(valor,self._cliente.DATATYPE.UINT16)
        resp = self._cliente.write_registers(address=addr, values=reg, device_id=1)
        return bool(resp and not resp.isError()) 
