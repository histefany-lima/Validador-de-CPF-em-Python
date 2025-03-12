# Validador de CPF em Python

Utilizando conceitos básicos de algoritmos, criei um validador de CPF na linguagem Python com base nas regras de CPF.

## Descrição

Este projeto é um validador de CPF desenvolvido em Python. O CPF (Cadastro de Pessoas Físicas) é um número de registro emitido pela Receita Federal do Brasil para identificar os contribuintes. Este script verifica se um CPF é válido de acordo com as regras de validação do CPF.

## Como funciona

O script realiza os seguintes passos para validar um CPF:

1. Solicita ao usuário que insira o número do CPF.
2. Calcula o primeiro dígito verificador somando o produto de cada dígito e um peso decrescente de 10 a 2.
3. Calcula o segundo dígito verificador repetindo o cálculo com pesos de 11 a 2.
4. Verifica se os dígitos verificadores calculados correspondem aos dígitos verificadores do CPF inserido.
5. Exibe se o CPF é válido ou inválido.

## Como usar

1. Clone este repositório:
   ```sh
   git clone https://github.com/histefany-lima/Validador-de-CPF-em-Python.git

2. Navegue até o diretório do projeto:
    ```sh
    cd Validador-de-CPF-em-Python

3. Execute o script:
   ```sh
   python validador-cpf.py

## Exemplo

Insira seu CPF: 12345678909

CPF INSERIDO:  12345678909

========== VERIFICANDO O PRIMEIRO DÍGITO ===========
Soma dos valores para o primeiro dígito:  210
Resto da divisão da soma por 11:  1
Digíto verificador 1:  0

========== VERIFICANDO O SEGUNDO DÍGITO ===========
Soma dos valores para o segundo dígito:  255
Resto da divisão da soma por 11:  2
Digíto verificador 2:  9

========== RESULTADO DA VALIDAÇÃO ===========
O CPF inserido é INVÁLIDO
   
