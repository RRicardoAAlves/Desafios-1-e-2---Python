# <!-- - ***Desafio 2:  Condicionais***

# ***Sistema de Reservas de Hotel:***

# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

# - *Cadastro de Cliente:*

# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

# - *Reservas de Quartos:*

# ***O sistema deve oferecer 3 tipos de quartos:*** 

# ***"Simples", "Duplo" e "Luxo".***

# ***Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***

# - ***Cálculo da Estadia:***

# ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.*** -->


print('CADASTRO DO CLIENTE')

nome_clientes = []
idade = []




nome1 = input('Digite o nome do 1º cliente')
idade1 = input('Digite a idade')
nome2 = input('Digite o nome do 2º cliente')
idade2 = input('Digite a sua idade')
nome3 = input('Digite o nome do 3º cliente')
idade3 = input('Digite a sua idade')

nome_clientes.append(nome1)
idade.append(idade1)
nome_clientes.append(nome2)
idade.append(idade2)
nome_clientes.append(nome3)
idade.append(idade3)


print('Quartos: Simples, Duplo, Luxo')

quarto_cliente1 = input('Escolha a opcão de quarto do 1º cliente: ')
quarto_cliente2 = input('Escolha a opcão de quarto do 2º cliente: ')
quarto_cliente3 = input('Escolha a opcão de quarto do 3º cliente: ')


valor_simples = 100
valor_duplo = 150
valor_luxo = 250

dias_cliente1 = int(input(f'Informe quantidade de dias o 1º cliente ({nome_clientes[0]}) ficará hospedado? '))
dias_cliente2 = int(input(f'Informe quantidade de dias o 2º cliente ({nome_clientes[1]}) ficará hospedado? '))
dias_cliente3 = int(input(f'Informe quantidade de dias o 3º cliente ({nome_clientes[2]}) ficará hospedado? '))


if quarto_cliente1 == 'simples':
    valor_cliente1 = valor_simples * dias_cliente1
elif quarto_cliente1 == 'duplo':
    valor_cliente1 = valor_duplo * dias_cliente1
else:
    valor_cliente1 = valor_luxo * dias_cliente1

if quarto_cliente2 == 'simples':
    valor_cliente2 = valor_simples * dias_cliente2
elif quarto_cliente2 == 'duplo':
    valor_cliente2 = valor_duplo * dias_cliente2
else:
    valor_cliente2 = valor_luxo * dias_cliente2

if quarto_cliente3 == 'simples':
    valor_cliente3 = valor_simples * dias_cliente3
elif quarto_cliente3 == 'duplo':
    valor_cliente3 = valor_duplo * dias_cliente3
else:
    valor_cliente3 = valor_luxo * dias_cliente3


print(f'Cliente 1: {nome_clientes[0]}, {idade[0]} anos, Quarto {quarto_cliente1}, {dias_cliente1} dias')
print(f'Valor Total do 1º cliente: R$ {valor_cliente1:.2f}')

print(f'Cliente 2: {nome_clientes[1]}, {idade[1]} anos, Quarto {quarto_cliente2}, {dias_cliente2} dias')
print(f'Valor Total do 2º cliente: R$ {valor_cliente2:.2f}')

print(f'Cliente 3: {nome_clientes[2]}, {idade[2]} anos, Quarto {quarto_cliente3}, {dias_cliente3} dias')
print(f'Valor Total do 3º cliente: R$ {valor_cliente3:.2f}')