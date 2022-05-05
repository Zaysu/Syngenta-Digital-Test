from hoteis import Hoteis

dataEntrada = int(input("Digite a data de entrada: "))
dataSaida = int(input( "Digite a data de saida: "))
tipoCliente = int(input( "Digite o tipo de cliente: (1- Reward / 2 - Regular) "))

reserva = Hoteis(tipoCliente, dataEntrada, dataSaida)

print(f"Tipo de cliente: {reserva.getTipoCliente()}")
print(f"Entrada: {reserva.getDataEntrada()}")
print(f"Saida: {reserva.getDataSaida()}")
print(f"Total de Dias: {reserva.datas()}")
print(f"Valores: {reserva.valoresHoteis()}")



