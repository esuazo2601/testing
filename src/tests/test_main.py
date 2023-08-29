from src.main import ohce
import pytest
import sys



def test_main1():
    assert ohce('¡Buenos dias!') == '¡Buenos dias!'
    assert ohce('¡Buenas tardes!') == '¡Buenas tardes!'
    assert ohce('¡Buenas noches!') == '¡Buenas noches!'

@pytest.mark.parametrize("name",["Pedro","Esteban","Gustavo"])
def test_main2(name, monkeypatch):
    monkeypatch.setattr(sys,"argv",["main.py",name])
    assert ohce ('¡Buenos dias!') == f'¡Buenos dias {name}'