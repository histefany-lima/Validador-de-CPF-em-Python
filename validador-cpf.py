# ========== PROGRAMA PARA VERIFICAR SE UM CPF É VÁLIDO, OU SEJA, SE ESTÁ DE ACORDO COM AS REGRAS DE CPF ========== #

cpf = input("\nInsira seu CPF: ")

soma_resultado = 0
valor = 10

for item in range (0,9):
    acumulador = int(cpf[item])
    soma_resultado = soma_resultado + (acumulador * valor)
    valor = valor - 1

#ENCONTRANDO O RESTO DA DIVISÃO PARA DESCOBRIR O PRIMEIRO DIGITO VERIFICADOR
resto_divisao = soma_resultado%11

#COMPARANDO SE O RESTO DA DIVISÃO FEITA ANTERIORMENTE É IGUAL A 0 OU 1, POIS SE FOR, O DÍGITO SERÁ 0
if (resto_divisao == 0 or resto_divisao == 1):

    dig1 = 0

#CASO CONTRÁRIO, O DÍGITO VERIFICADOR SERÁ A SUBTRAÇÃO DE 11 MENOS O RESTO
else:
    dig1 = (11 - resto_divisao)

print("\nCPF INSERIDO: ",*cpf)

print("\n========== VERIFICANDO O PRIMEIRO DÍGITO ===========")
print("Soma dos valores para o primeiro dígito: ", soma_resultado)
print("Resto da divisão da soma por 11: ", resto_divisao)
print("Digíto verificador 1: ", dig1)

soma_resultado2 = 0
valor2 = 10

for item in range (1,10):
    acumulador2 = int(cpf[item])
    soma_resultado2 = soma_resultado2 + (acumulador2 * valor2)
    valor2 = valor2 - 1

resto_divisao2 = soma_resultado2%11

if (resto_divisao2 == 0 or resto_divisao2 == 1):

    dig2 = 0

#CASO CONTRÁRIO, O DÍGITO VERIFICADOR SERÁ A SUBTRAÇÃO DE 11 MENOS O RESTO
else:

    dig2 = (11 - resto_divisao2)

print("\n========== VERIFICANDO O SEGUNDO DÍGITO ===========")
print("Soma dos valores para o segundo dígito: ", soma_resultado2)
print("Resto da divisão da soma por 11: ", resto_divisao2)
print("Digíto verificador 2: ", dig2)

print("\n========== RESULTADO DA VALIDAÇÃO ===========")

if(int(cpf[9]) == dig1 and int(cpf[10]) == dig2):
    print("O CPF inserido é VÁLIDO")
else:
    print("O CPF inserido é INVÁLIDO")