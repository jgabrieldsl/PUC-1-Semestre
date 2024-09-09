# Jogo zero cancela

num = 0
soma = 0
considerados = 1
desconsiderados = 0

n_anterior = 0
n_anterior2 = 0
n_anterior3 = 0


while num >= 0 :
    num = int (input("Digite um número: "))
    if num > 0 :
        # Atribuindo um novo valor a num e, consequentemente, a soma (em loop).
        soma += num
        # Números considerados para a soma 
        considerados += 1

        zeros = 0

        n_anterior3 = n_anterior2
        n_anterior2 = n_anterior
        n_anterior = num

        

    elif num == 0 :
        if zeros == 3 :
            print("Apague somente três números! Pare o programa ou digite outro número.")

        else :
            # Se a quantidade de zeros for menor que 3, vai subtrair o ultimo número digitado da soma total!
            soma = soma - n_anterior

            #Para contar os zeros digitados
            zeros = zeros + 1

            #Eliminar 1 dos considerados
            considerados -= 1

            #
            desconsiderados +=1
            

if num < 0:
    considerados -= 1
    print(f"Confira os dados obtidos: \n Soma total: {soma} \n Números considerados: {considerados} \n Números desconsiderados: {desconsiderados} ")

 