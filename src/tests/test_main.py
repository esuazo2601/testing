from src.main import ohce, main_input
import pytest
import sys
import datetime
hora_actual = datetime.datetime.now().hour

#Test para el saludo inicial
@pytest.mark.parametrize("name",["Pedro","Esteban","Gustavo"])
def test_main1(name, monkeypatch):
    monkeypatch.setattr(sys,"argv",["main.py",name])
    print(hora_actual)
    if hora_actual >= 6 and hora_actual <= 12:
        assert ohce(hora_actual) == f'¡Buenos dias {name}!'
    elif hora_actual > 12 and hora_actual < 20:
        assert ohce(hora_actual) == f'¡Buenas tardes {name}!'
    else :
        assert ohce(hora_actual) == f'¡Buenas noches {name}!'

#Test para que acabe la ejecución al escribir Stop!
@pytest.mark.parametrize("name",["Pedro","Esteban","Gustavo"])
def test_input_function(monkeypatch, capsys, name):
    # Simula la entrada de datos por teclado
    user_input = ["Stop!"]
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop())
    result = main_input

    # Captura la salida estándar
    captured = capsys.readouterr()

    # Realiza las aserciones necesarias
    assert result == f"Adios {name}"

