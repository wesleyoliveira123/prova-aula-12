class Veiculo:
    def movimentar(self):
        return f"Veículo está em movimento."

class Carro(Veiculo):
    def movimentar(self):
        return f"Carro está dirigindo."

class Moto(Veiculo):
    def movimentar(self):
        return f"Moto está acelerando."


veiculo=Veiculo()
carro=Carro()
moto=Moto()

print(veiculo.movimentar())
print(carro.movimentar())
print(moto.movimentar())
