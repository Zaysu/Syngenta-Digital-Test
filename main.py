from hoteis import Hoteis

tipoCliente = int(input( "Digite o tipo de cliente: (1- Regular / 2 - Reward) "))
dataEntrada = int(input("Digite a data 1: "))
dataSaida = int(input( "Digite a data 2: "))

reserva = Hoteis(tipoCliente, dataEntrada, dataSaida)

print(f"Entrada: {reserva.getDataEntrada()}")
print(f"{reserva.getTipoCliente()} : {dataEntrada}/Mai2022 {reserva.valoresHoteis().keys()} ")
print(f"{reserva.getTipoCliente()} : {dataSaida}/Mai2022 {reserva.valoresHoteis().keys()} ")
print(f"Saida: {reserva.getDataSaida()}")




