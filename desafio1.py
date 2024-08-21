# - ***Desafio 1 Condicionais***

# ***Crie um sistema de e-commerce, onde o usuário possa:***

# - ***cadastrar-se***
# - ***comprar um produto***
# - ***descobrir o valor total***
# - ***pagar***

print('CADASTRO DO CLIENTE')

nome = (input('Digite seu nome')) 
cpf = (input('Digite seu CPF'))
endereço = (input('Digite seu endereço'))

print(nome)
print(cpf)
print(endereço)

vestuarios = ['calça', 'camisa', 'tenis']
precos = [10.0, 5.00, 20.0]


carrinho = []
total = 0

print("Vestuários disponíveis:")
print("1. calca - R$ 10.00")
print("2. camisa - R$ 5.00")
print("3. tenis - R$ 20.00")



escolha1 = input("Escolha o número do vestuário que deseja adicionar ao carrinho (ou '0' para finalizar): ")

if escolha1 == '1':
    carrinho.append(vestuarios[0])
    total += precos[0]
elif escolha1 == '2':
    carrinho.append(vestuarios[1])
    total += precos[1]
elif escolha1 == '3':
    carrinho.append(vestuarios[2])
    total += precos[2]


escolha2 = input("Escolha o número do vestuário que deseja adicionar ao carrinho (ou '0' para finalizar): ")

if escolha2 == '1':
    carrinho.append(vestuarios[0])
    total += precos[0]
elif escolha2 == '2':
    carrinho.append(vestuarios[1])
    total += precos[1]
elif escolha2 == '3':
    carrinho.append(vestuarios[2])
    total += precos[2]



escolha3 = input("Escolha o número do vestuário que deseja adicionar ao carrinho (ou '0' para finalizar): ")

if escolha3 == '1':
    carrinho.append(vestuarios[0])
    total += precos[0]
elif escolha3 == '2':
    carrinho.append(vestuarios[1])
    total += precos[1]
elif escolha3 == '3':
    carrinho.append(vestuarios[2])
    total += precos[2]



print("\nVocê comprou:")
if len(carrinho) > 0:
    print(carrinho)
    print(f"Total: R$ {total:.2f}")
else:
    print("Nenhum vestuário comprado.")