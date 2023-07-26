saldo = 500
saques = 1
LIMITE_SAQUES = 3
LIMITE_SAQUE_MAXIMO = 500
extrato = ""

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

def sacar(valor, saldo):
    return saldo - valor


while opcao != 0:
    if saques > LIMITE_SAQUES:
       break 
    
    print(menu)
    opcao = int(input("Escolha uma operação:\n"))

    match opcao:
        case 1:
            print(f"Seu saldo é de: {formataNumero(saldo)}")
            continue 
        case 2:
            try:
                valor = float(input(f"Insira o valor a ser depositado:\n"))
                saldo = depositar(valor, saldo)
                print(f"Seu novo saldo é de: {formataNumero(saldo)}")
                extrato = f"{extrato}\n Depósito de {formataNumero(valor)}, saldo {formataNumero(saldo)}"
                continue 
            except ValueError as Error:
                print("Valor inválido, apenas números permitidos, insira valor decimal com pontos.")
                continue
        case 3:
            if saldo <= 0:
                print(f"Você não pode efetuar nenhum saque. Saldo insuficiente.")
                continue 
            valor = float(input(f"Insira o valor a ser sacado:\n"))
            
            if valor > saldo:
                print(f"Valor não disponível na sua conta.")
                print(f"Seu saldo é de: {formataNumero(saldo)}")
                continue

            saldo = sacar(valor, saldo)
            print(f"Seu novo saldo é de: {formataNumero(saldo)}")
            print(f"Você pode efetuar mais {LIMITE_SAQUES - saques} saque(s)")
            extrato = f"{extrato}\n Saque de {formataNumero(valor)}, saldo {formataNumero(saldo)}"
            saques += 1
            continue 
        case 4:
            print(f"{extrato}")
            continue
        case 0:
            break
        case _:
            print("Opção inválida.")
