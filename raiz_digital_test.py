import pytest
from raiz_digital import digital_root

def test_digital_root():
    assert digital_root(9) == 9 # Teste com apenas um numero

def test_digital_root_4():
    assert digital_root(3192312) == 3 # Teste com multiplos numeros

def test_digital_root_negative():
    assert digital_root(-20) == "O numero não pode ser negativo" # Teste com numero negativo

def test_digital_root_string():
    assert digital_root("Teste") == "Um numero deverá ser enviado" # Teste utilizando uma String
