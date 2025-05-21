# Variável de saída
saida = ''

# Funções de adição
def adicao(num1, num2):
    return num1 + num2

# Funções de subtração
def subtracao(num1, num2):
    return num1 - num2

# Funções de multiplicação
def multiplicacao(num1, num2):
    return num1 * num2

# Funções de divisão
def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2

# calculadora
def calculadora(num1, num2, operacao):
    operacao = operacao.lower()

    if operacao in ['+', 'adicao', 'adição']:
        resultado = adicao(num1, num2)
    elif operacao in ['-', 'subtracao', 'subtração']:
        resultado = subtracao(num1, num2)
    elif operacao in ['*', 'x', 'multiplicacao', 'multiplicação']:
        resultado = multiplicacao(num1, num2)
    elif operacao in ['/', 'divisao', 'divisão']:
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'
    
    return resultado

# Laço 
while saida.lower() != 'n':
    try:
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        operacao = input('Digite a operação desejada (+, -, *, / ou nome da operação): ')
        
        resultado = calculadora(numero1, numero2, operacao)
        
        print('Resultado da operação:', resultado)
        
        saida = input('Deseja continuar? (S para sim / N para não): ')
    except ValueError:
        print('Entrada inválida. Por favor, digite números válidos.')
