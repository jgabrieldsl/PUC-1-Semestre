# Atividade Avaliativa A2 –  2024 : A FOLHA DE PAGAMENTO

import os
import pandas as pd
from tabulate import tabulate

# Cleaner Prompt
def clear_screen():
    os.system('cls')
clear_screen()

funcionarios = { }

# Menu
def menu() :
    print ('\n', '-' * 40)
    print('\n BEM VINDO A FOLHA DE PAGAMENTO')
    print ('\n', '-' * 40)
    print (" 1. Inserir Funcionários\n 2. Remover Funcionários\n 3. Determinar a folha de pagamento de um determinado funcionário\n 4. Determinar um relatório com o salário bruto e líquido de todos os funcionários\n 5. Imprimir as informações do funcionário com maior salário líquido\n 6. Imprimir as informações do funcionário com o maior número de faltas no mês\n 0. Sair")
    print ('-' * 40, '\n' )

def mostrar_funcionarios():
    dados_func = []
    for matricula, values in funcionarios.items():
        dados_func.append({"Matricula": matricula, "Nome": values[0], "Código": values[1], "Função": values[2], "Faltas": values[3], "Salário Bruto": f"R${values[4]}", "Imposto": values[5], "Salário Líquido": f"R${values[6]}"})

    table_funcionarios = pd.DataFrame(dados_func)
    print(tabulate(table_funcionarios, headers='keys', tablefmt='fancy_grid', showindex=False))

def calcular_imposto(salario):
    if (2259.21 <= salario <= 2828.65) :
        salario = salario - (salario * 0.075)
        percent_imposto = '7.5%'

    elif (2828.66 <= salario <= 3751.05):
        salario = salario - (salario * 0.15)
        percent_imposto = '15%'
    
    elif (3751.06 <= salario <= 4664.68):
        salario = salario - (salario * 0.225)
        percent_imposto = '22.5%'
    
    elif salario > 4664.68:
        salario = salario - (salario * 0.275)
        percent_imposto = '27.5%'

    else :
        salario = salario
        percent_imposto = '0%'

    return salario, percent_imposto

# 1
def inserir_func ():
    while True :
        try :
            matricula = int (input("Matrícula: "))
            if matricula in funcionarios.keys() :
                print (f"Funcionário com a matrícula {matricula} já cadastrado no sistema, tente novamente.")
            else :
                break
        except ValueError :
            print (f"Digite um número inteiro para fazer o cadastro da matrícula.")

    nome = (input("Nome do funcionário: "))
    
    while True :
        try :
            codigo = int (input("Código: "))
            if 101 <= codigo <= 102 :
                break
            else :
                print("Código inválido, digite 101 para Vendedor ou 102 para Administrativo.")
        except ValueError :
            print("Código inválido, digite apenas números, 101 para Vendedor ou 102 para Administrativo.")

    faltas = int (input("Faltas: "))  
    
    # Vendedor
    if codigo == 101:
            funcao = 'Vendedor'
            while True :
                try :
                    vendas = float (input("Qual o volume de vendas do funcionário? R$"))
                    break
                except ValueError :
                    print ("Formato Inválido, tente novamente. Ex: R$1290.22")

            desconto = faltas * 50

            salario_bruto = 1500.00 + (0.09 * vendas)

            salario = salario_bruto - desconto

            salario, percent_imposto = calcular_imposto(salario)
            
            funcionarios[matricula] = [nome, codigo, funcao, faltas, round(salario_bruto, 2), percent_imposto, round(salario, 2), desconto]

    # Administrativo
    else :
        funcao = 'Administrativo'
        while True :
            try:
                salario = float (input("Digite o salário do funcionário: R$"))
                if 2150 <= salario <= 6950 :
                    salario = salario
                    break
                else :
                    print ("Digite um salário válido, entre R$2150 e R$6950")
            except ValueError :
                print ('Digite em um formato válido. Ex: R$3594.32')
                
        desconto = faltas * (salario/30)

        salario_bruto = salario

        salario = salario - (desconto)

        salario, percent_imposto = calcular_imposto(salario)

        funcionarios[matricula] = [nome, codigo, funcao, faltas, round(salario_bruto, 2), percent_imposto, round(salario, 2), desconto]
    
    print("\nFuncionário inserido com sucesso! Confira a tabela atualizada:")
    mostrar_funcionarios()
    
# 2
def remover_func ():
    mostrar_funcionarios()
    while True:
        try :
            matricula= int(input("\nDigite a matricula do funcionario que deseja remover: "))
            if matricula in funcionarios.keys() :
                del funcionarios[matricula]
                break
            else :
                print ("Funcionário não encontrado, tente novamente.")
        except ValueError :
            print("Digite algo válido.")
    print("\nFuncionário removido com sucesso! Confira a tabela atualizada:")
    mostrar_funcionarios()

# 3
def folha_determinado_func():
    matricula_desejada = int(input("Digite a matrícula do funcionário que deseja obter os dados: "))
    encontrado = False
    dados_func = []

    for matricula, values in funcionarios.items():
        if matricula_desejada == matricula:
            encontrado = True
            dados_func.append({"Matricula": matricula, "Nome": values[0], "Código": values[1], "Função": values[2], "Faltas": values[3], "Salário Bruto": f"R${values[4]}", "Imposto": values[5], "Salário Líquido": f"R${values[6]}"})
    
    if encontrado :
        table_funcionarios = pd.DataFrame(dados_func)
        print(f"\nConfira os dados do funcionário {matricula_desejada}:")
        print(tabulate(table_funcionarios, headers='keys', tablefmt='fancy_grid', showindex=False))

    else :
        print("\nFuncionário não encontrado!")

# 4
def folha_bruto_liquido ():
    dados_func = []
    for matricula, values in funcionarios.items():
        dados_func.append({"Matricula": matricula, "Nome": values[0], "Código": values[1], "Salário Bruto": f"R${values[4]}", "Salário Líquido": f"R${values[6]}"})

    table_funcionarios = pd.DataFrame(dados_func)
    print(" \nConfira o relatório com o salário bruto e líquido de todos os funcionários:")
    print(tabulate(table_funcionarios, headers='keys', tablefmt='fancy_grid', showindex=False))


# 5
def func_maior_salario ():
    dados_func = []
    maior_salario = 0
    
    for values in funcionarios.values():
        if values[6] > maior_salario :
            maior_salario = values[6]
    
    for matricula, values in funcionarios.items():
        if maior_salario == values[6]:
            dados_func.append({"Matricula": matricula, "Nome": values[0], "Código": values[1], "Função": values[2], "Salário Bruto": f"R${values[4]}", "Imposto": values[5], "Salário Líquido": f"R${values[6]}"})

         
    table_funcionarios = pd.DataFrame(dados_func)
    print(" \nConfira o relatório com os dados do funcionários com maior salário:")
    print(tabulate(table_funcionarios, headers='keys', tablefmt='fancy_grid', showindex=False))

# 6
def faltas_maior ():
    dados_func = []
    maior_falta = 0
    for values in funcionarios.values():
        if values[3] > maior_falta :
            maior_falta = values[3]
    
    for matricula, values in funcionarios.items():
        if maior_falta == values[3] :
            dados_func.append({"Matricula": matricula, "Nome": values[0], "Código": values[1], "Faltas": values[3], "Desconto": f"R${values[7]}"})

    if maior_falta > 0 :        
        table_funcionarios = pd.DataFrame(dados_func)
        print(" \nConfira o relatório com os dados do funcionários com o maior número de faltas:")
        print(tabulate(table_funcionarios, headers='keys', tablefmt='fancy_grid', showindex=False))
    else :
        print("\nNenhum funcionário faltou esse mês!")

while True:
    menu()
    opcao = int (input("Escolha uma opção: "))

    if opcao == 1 :
         inserir_func()

    elif opcao == 2 :
        remover_func ()

    elif opcao == 3 :
        folha_determinado_func ()
    
    elif opcao == 4 :
        folha_bruto_liquido ()
    
    elif opcao == 5 :
        func_maior_salario()

    elif opcao == 6 :
        faltas_maior()

    elif opcao == 0 :
        print ("Saindo...")
        break
    
    else :
        print ("Opção inválida, digite novamente.")
         
