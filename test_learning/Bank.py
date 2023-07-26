class Bank:

    def __init__(self, saldo) -> None:
        if not isinstance(saldo, (int, float)):
           raise AttributeError("Entrada inválida")

        self.saldo = saldo
        self.extrato = ""
        pass

    def verSaldo(self):
        return self.saldo

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def ver_extrato(self):
        return self.extrato

    def concatena_extrato(self, numero_operacao, operacao, valor):
        return f"{self.extrato}\n{numero_operacao}. {operacao.title()} de {formata_valor(valor)}"

def formata_valor(valor) -> str:
    # valor = float(valor)
    return f'R$ {valor:.2f}'

