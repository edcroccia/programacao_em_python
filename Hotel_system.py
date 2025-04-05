# Sistema que gerencie reservas de quartos e o pagamento de diárias.
# Cadastro de clientes deverá permitir o cadastro de até 3 clientes.

clientes = []

# Coletando dados de até 3 clientes
cliente1 = input("Digite o nome do cliente 1: ")
cliente1a = input("Digite a idade do cliente 1: ")
clientes +=(cliente1,cliente1a)
cliente2 = input("Digite o nome do cliente 2: ")
cliente2a = input("Digite a idade do cliente 2: ")
clientes +=(cliente2,cliente2a)
cliente3 = input("Digite o nome do cliente 3: ")
cliente3a = input("Digite a idade do cliente 3: ")
clientes +=(cliente3,cliente3a)
print("Clientes Cadastrados:", clientes)
#***O sistema deve oferecer 3 tipos de quartos:*** 
#***"Simples", "Duplo" e "Luxo".***
#Cada cliente deve escolher um quarto para sua estadia. O preço da diária varia conforme o tipo de quarto:
#Simples: R$ 100,00 por dia.
#Duplo: R$ 150,00 por dia.
#Luxo: R$ 250,00 por dia.
Cliente = input('Quem é o cliente? Digite entre 1, 2 ou 3 :')
if Cliente == '1':
    print("Escolha o tipo de quarto:")
    print("4. Quarto Simples")
    print("5. Quarto Duplo")
    print("6. Quarto Luxo")

    tipo_quarto = input("Digite o número da opção desejada (4, 5 ou 6): ")
    
    # Verificar a escolha do tipo de quarto
    if tipo_quarto == '4':
        tipo_quarto_escolhido = "Quarto Simples"
    elif tipo_quarto == '5':
        tipo_quarto_escolhido = "Quarto Duplo"
        # p5 = 150
    elif tipo_quarto == '6':
        tipo_quarto_escolhido = "Quarto Luxo"
        # p6 = 250
    else:
        tipo_quarto_escolhido = "Opção inválida"
     
    # Se a opção for válida, solicitar o período de hospedagem
    if tipo_quarto_escolhido != "Opção inválida":
        if tipo_quarto_escolhido == "Quarto Simples":
            A = 100
            periodo = int(input("Digite o período de hospedagem (em dias): "))
            print(f"Cliente 1 - Você escolheu: {tipo_quarto_escolhido} por {periodo} dias.")
            total1 = (A * periodo)
            print(f"Cliente 1 - Seu total a pagar por sua estadia será de {total1}")
        elif tipo_quarto_escolhido == "Quarto Duplo":
            B = 150
            periodo = int(input("Digite o período de hospedagem (em dias): "))
            print(f"Cliente 1 - Você escolheu: {tipo_quarto_escolhido} por {periodo} dias.")
            total2 = (B * periodo)
            print(f"Cliente 1 - Seu total a pagar por sua estadia será de {total2}")
        else:
            C = 250
            periodo = int(input("Digite o período de hospedagem (em dias): "))
            print(f"Cliente 1 - Você escolheu: {tipo_quarto_escolhido} por {periodo} dias.")
            total3 = (C * periodo)
            print(f"Cliente 1 - Seu total a pagar por sua estadia será de R$ {total3}")
    else:
        print("Por favor, escolha um tipo de quarto válido.")

elif Cliente == '2':
    print("Escolha o tipo de quarto:")
    print("4. Quarto Simples")
    print("5. Quarto Duplo")
    print("6. Quarto Luxo")

    tipo_quarto = input("Digite o número da opção desejada (4, 5 ou 6): ")
    
    # Verificar a escolha do tipo de quarto
    if tipo_quarto == '4':
        tipo_quarto_escolhido = "Quarto Simples"
        # p4 = 100
    elif tipo_quarto == '5':
        tipo_quarto_escolhido = "Quarto Duplo"
        # p5 = 150
    elif tipo_quarto == '6':
        tipo_quarto_escolhido = "Quarto Luxo"
        # p6 = 250
    else:
        tipo_quarto_escolhido = "Opção inválida"
     
    # Se a opção for válida, solicitar o período de hospedagem
    if tipo_quarto_escolhido != "Opção inválida":
        if tipo_quarto_escolhido == "Quarto Simples":
            A = 100
            periodo = int(input("Digite o período de hospedagem (em dias): "))
            print(f"Cliente 2 - Você escolheu: {tipo_quarto_escolhido} por {periodo} dias.")
            total1 = (A * periodo)
            print(f"Cliente 2 - Seu total a pagar por sua estadia será de {total1}")
        elif tipo_quarto_escolhido == "Quarto Duplo":
            B = 150
            periodo = int(input("Digite o período de hospedagem (em dias): "))
            print(f"Cliente 2 - Você escolheu: {tipo_quarto_escolhido} por {periodo} dias.")
            total2 = (B * periodo)
            print(f"Cliente 2 - Seu total a pagar por sua estadia será de {total2}")
        else:
            C = 250
            periodo = int(input("Digite o período de hospedagem (em dias): "))
            print(f"Cliente 2 - Você escolheu: {tipo_quarto_escolhido} por {periodo} dias.")
            total3 = (C * periodo)
            print(f"Cliente 2 - Seu total a pagar por sua estadia será de R$ {total3}")
    else:
        print("Por favor, escolha um tipo de quarto válido.")
else:
    print("Escolha o tipo de quarto:")
    print("4. Quarto Simples")
    print("5. Quarto Duplo")
    print("6. Quarto Luxo")

    tipo_quarto = input("Digite o número da opção desejada (4, 5 ou 6): ")
    
    # Verificar a escolha do tipo de quarto
    if tipo_quarto == '4':
        tipo_quarto_escolhido = "Quarto Simples"
        # p4 = 100
    elif tipo_quarto == '5':
        tipo_quarto_escolhido = "Quarto Duplo"
        # p5 = 150
    elif tipo_quarto == '6':
        tipo_quarto_escolhido = "Quarto Luxo"
        # p6 = 250
    else:
        tipo_quarto_escolhido = "Opção inválida"
     
    # Se a opção for válida, solicitar o período de hospedagem
    if tipo_quarto_escolhido != "Opção inválida":
        if tipo_quarto_escolhido == "Quarto Simples":
            A = 100
            periodo = int(input("Digite o período de hospedagem (em dias): "))
            print(f"Cliente 3 - Você escolheu: {tipo_quarto_escolhido} por {periodo} dias.")
            total1 = (A * periodo)
            print(f"Cliente 3 - Seu total a pagar por sua estadia será de {total1}")
        elif tipo_quarto_escolhido == "Quarto Duplo":
            B = 150
            periodo = int(input("Digite o período de hospedagem (em dias): "))
            print(f"Cliente 3 - Você escolheu: {tipo_quarto_escolhido} por {periodo} dias.")
            total2 = (B * periodo)
            print(f"Cliente 3 - Seu total a pagar por sua estadia será de {total2}")
        else:
            C = 250
            periodo = int(input("Digite o período de hospedagem (em dias): "))
            print(f"Cliente 3 - Você escolheu: {tipo_quarto_escolhido} por {periodo} dias.")
            total3 = (C * periodo)
            print(f"Cliente 3 - Seu total a pagar por sua estadia será de R$ {total3}")
    else:
        print("Por favor, escolha um tipo de quarto válido.")