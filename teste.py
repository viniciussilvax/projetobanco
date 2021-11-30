from models.cliente import Cliente
from models.conta import Conta

vinicius: Cliente = Cliente('Vinicius Silva', '014.195.132-42', '10/03/1992')
danieli: Cliente = Cliente('Danieli Hentges Ferreira', '012.195.164-41', '20/03/1986')

# print(vinicius)
# print(danieli)

contav: Conta = Conta(vinicius)
contad: Conta = Conta(danieli)

print(contav)
print(contad)