import pytest
from validator import validar_cep

@pytest.mark.parametrize("cidade, cep, esperado", [
    ("Sorocaba", "18.050-100", True),
    ("Capela do Alto", "18.195-000", True),
    ("São Roque", "18.130-020", True),
    ("Votorantim", "19.000-000", False)
])
def test_validar_cep(cidade, cep, esperado):
    assert validar_cep(cidade, cep) == esperado
