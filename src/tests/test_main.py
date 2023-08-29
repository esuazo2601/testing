from src.main import ohce
import pytest
import sys
import datetime
hora_actual = datetime.datetime.now().hour

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
