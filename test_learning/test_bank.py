import pytest
from learning.Bank import Bank, formata_valor


# Utils

def test_verSaldo():
    bank = Bank(200)
    assert bank.verSaldo() == 200

def test_validaSaldo():
    # Test with an invalid input (a string)
    with pytest.raises(AttributeError) as excinfo:
        bank = Bank('abc')

def test_sacar():
    saldo = 200
    valor_sacado = 100
    bank = Bank(saldo)
    assert bank.sacar(valor_sacado) == saldo - valor_sacado

def test_depositar():
    saldo = 200
    valor_depositado = 100
    bank = Bank(saldo)
    assert bank.depositar(valor_depositado) == saldo + valor_depositado 

def test_ver_extrato():
    bank = Bank(0)
    assert isinstance(bank.ver_extrato(), str) 

def test_formata_valor():
    valor = float(200)
    assert formata_valor(valor) == "R$ 200.00"

def test_concatena_extrato():
    bank = Bank(0)
    assert bank.concatena_extrato(1, 'saque', 200) == f"\n1. Saque de R$ 200.00"

