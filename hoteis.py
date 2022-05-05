class Hoteis:
    def __init__(self, tipoCliente, dataEntrada, dataSaida):
        self.tipoCliente = tipoCliente
        self.dataEntrada = dataEntrada
        self.dataSaida = dataSaida
    
    def getTipoCliente(self):
        if self.tipoCliente == 1:
            self.tipoCliente = "Regular"
            return self.tipoCliente
        if self.tipoCliente == 2:
            self.tipoCliente = "Reward"
            return self.tipoCliente
    
    def getDataEntrada(self):
        return self.dataEntrada
    
    def getDataSaida(self):
        return self.dataSaida
    
    def datas(self):
        data = self.dataSaida - self.dataEntrada
        return data
    
    def valoresHoteis(self):
        hoteis = [{'Lakewood': 3} , {' Bridgewood': 4} , {' Ridgewood': 5}]
        valoresNormal =[110, 160, 220] #normal
        valoresReward =[80, 110, 100] #reward
        adicionalNormal = [90, 60, 150] #Addnormal
        adcionalReward = [80, 50, 40] #Addreward
        
        normallakewood = valoresNormal[0]
        rewardlakewood = valoresReward[0]
        lakewoodNormal = valoresNormal[0] + adicionalNormal[0] #FimDeSemana-Normal-Lakewood
        lakewoodReward = valoresReward[0] + adcionalReward[0] #FimDeSemana-Reward-Lakewood
        
        normabridgewood = valoresNormal[1]
        rewardbridgewood = valoresReward[1]
        bridgewoodNormal1 = valoresNormal[1] + adicionalNormal[1] #FimDeSemana-Normal-Bridgewood (220)
        bridgewoodReward2 = valoresReward[1] + adcionalReward[1] #FimDeSemana-Reward-Bridgewood (160)
        
        normalridgewood = valoresNormal[2]
        rewardridgewood = valoresReward[2]
        ridgewoodNormal2 = valoresNormal[2] + adicionalNormal[2] #FimDeSemana-Normal-Ridgewood (370)
        ridgewoodReward2 = valoresReward[2] + adcionalReward[2] #FimDeSemana-Reward-Ridgewood (140)
        
        data = self.dataSaida - self.dataEntrada
        
        if self.tipoCliente == "Regular":
            if data * normallakewood < data * normabridgewood and data * normallakewood < data * normalridgewood:
                return hoteis[0]
            
            elif data * normabridgewood < data * normallakewood and data * normabridgewood < data * normalridgewood:
                return hoteis[1]
            
            elif data * normalridgewood < data * normallakewood and data * normalridgewood < data * normabridgewood:
                return hoteis[2]
         
        if self.tipoCliente == "Reward":
            if data * rewardlakewood < data * rewardbridgewood and data * rewardlakewood < data * rewardridgewood:
                return hoteis[0]
            
            elif data * rewardbridgewood < data * rewardlakewood and data * rewardbridgewood < data * rewardridgewood:
                return hoteis[1]
            
            elif data * rewardridgewood < data * rewardbridgewood and data * rewardridgewood < data * rewardlakewood:
                return hoteis[2]
            
            
    ##################### ------------ PareiAqui falta fazer verificação por dia da semana  --------#############################  
            
        
    def classificacao(self):
        return "oi"
    
        
            
            