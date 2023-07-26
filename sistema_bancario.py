saldo = 500
saques = 1
LIMITE_SAQUES = 3
LIMITE_SAQUE_MAXIMO = 500

opcao = -1

while opcao != 0:
    if saques > LIMITE_SAQUES:
       break 

    opcao = int(input("Escolha uma operação:\n"))

    match opcao:
        case 1:
            break
        case 2:
            break
        case 3:
            break
        case 4:
            break
        case 0:
            break
        case _:
            print("Opção inválida.")
