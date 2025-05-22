Trabalho Prático | DGT2817 LÓGICA, ALGORITMOS E
PROGRAMAÇÃO DE COMPUTADORES

Documentação do Projeto – Calculadora em Python
Aluno: Robson Batista Neto
Curso: Desenvolvimento Full Stack
Instituição: Estácio
Tutor: Cláudio
Data: Maio/2025

Sumário
Introdução

Objetivos

Tecnologias Utilizadas

Funcionalidades do Projeto

Estrutura do Código

Instruções de Instalação e Execução

Considerações Finais

Referências

1. Introdução
Este projeto tem como objetivo desenvolver uma calculadora simples utilizando a linguagem de programação Python. A aplicação permite que o usuário realize operações básicas como adição, subtração, multiplicação e divisão, interagindo através do terminal.

2. Objetivos
Objetivo Geral:
Desenvolver uma aplicação em Python que execute operações matemáticas básicas, promovendo a prática de funções, estruturas de repetição, condicionais e tratamento de erros.

Objetivos Específicos:

Implementar operações matemáticas básicas.

Desenvolver funções específicas para cada operação.

Utilizar estruturas condicionais e laços de repetição.

Aplicar tratamento de erros para entradas inválidas.

3. Tecnologias Utilizadas
Linguagem: Python 3.x

Editor de código: VS Code, PyCharm ou outro de sua preferência

Ambiente: Terminal ou console para execução

4. Funcionalidades do Projeto
Realiza operações de adição, subtração, multiplicação e divisão.

Reconhece tanto os símbolos matemáticos (+, -, *, /) quanto os nomes das operações (adição, subtração, multiplicação, divisão).

Faz validação de divisão por zero, retornando uma mensagem apropriada.

Estrutura de repetição que permite realizar várias operações até o usuário decidir sair.

Faz tratamento de erros, como validação de entradas não numéricas.

5. Estrutura do Código
Variável de controle:

python
Copiar
Editar
saida = ''
Funções Matemáticas:

python
Copiar
Editar
def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2
Função Principal – Calculadora:

python
Copiar
Editar
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
Laço de repetição:

python
Copiar
Editar
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
6. Instruções de Instalação e Execução
Pré-requisitos:

Ter o Python 3 instalado no computador.

Utilizar um editor de texto, IDE (VS Code, PyCharm) ou até mesmo o IDLE do Python.

Passos para Executar:

Copie o código e salve em um arquivo chamado, por exemplo, calculadora.py.

Abra o terminal ou prompt de comando na pasta onde está o arquivo.

Execute o comando:

bash
Copiar
Editar
python calculadora.py
Siga as instruções que aparecem no terminal.

7. Considerações Finais
Este projeto serviu como uma excelente prática para aplicar os fundamentos da linguagem Python, como funções, condicionais, laços e tratamento de exceções.
A calculadora funciona de maneira simples e eficiente via terminal. Pode ser aprimorada no futuro para incluir mais operações matemáticas, melhorias de interface ou até uma interface gráfica com bibliotecas como Tkinter ou PyQt.

8. Referências
Documentação Oficial do Python – https://docs.python.org/pt-br/3/

Materiais fornecidos pela disciplina

Conteúdos da Estácio

