import pytest

from calcular_desconto import calcular_desconto


@pytest.mark.parametrize("valor_compra, tipo_cliente, desconto_esperado", [
    (50, "COMUM", 0),
    (100, "COMUM", 10),
    (300, "COMUM", 30),
    (499.99, "COMUM", 49.99),
    (500, "COMUM", 100),
    (700, "COMUM", 140),

    (50, "VIP", 2.50),
    (100, "VIP", 15),
    (300, "VIP", 45),
    (500, "VIP", 125),

    (300, "vip", 45),
    (300, "Vip", 45),

    (1000, "COMUM", 200),
    (1000, "VIP", 200),
    (2000, "VIP", 200),
])
def test_calcular_desconto(
    valor_compra,
    tipo_cliente,
    desconto_esperado
):
    resultado = calcular_desconto(valor_compra, tipo_cliente)

    assert resultado == pytest.approx(desconto_esperado)