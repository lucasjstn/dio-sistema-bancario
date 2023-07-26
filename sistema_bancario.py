saldo = 500
saques = 1
LIMITE_SAQUES = 3
LIMITE_SAQUE_MAXIMO = 500

opcao = -1

menu = f"""
--------------------------------

Escolha uma opção:

[1] Ver Saldo
[2] Depositar
[3] Sacar
[4] Extrato
[0] Sair

---------------------------------
"""
def formataNumero(numero):
    return f"R${numero:.2f}"

def depositar(valor, saldo):
    return saldo + valor


while opcao != 0:
    if saques > LIMITE_SAQUES:
       break 
    
    print(menu)
    opcao = int(input("Escolha uma operação:\n"))

    match opcao:
        case 1:
            print(f"Seu saldo é de: {formataNumero(saldo)}")
            break
        case 2:
            valor = float(input(f"Insira o valor a ser depositado:\n"))
            saldo = depositar(valor, saldo)
            print(f"Seu novo saldo é de: {formataNumero(saldo)}")
            continue 
        case 3:
            break
        case 4:
            break
        case _:
            print("Opção inválida.")
