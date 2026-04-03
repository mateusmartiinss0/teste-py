try:
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Acesso Liberado!")
    elif idade >= 0:
        print("Acesso Negado!")
    else:
        print("Idade Inválida!")

except ValueError:
    print("Por favor, digite um número válido!")