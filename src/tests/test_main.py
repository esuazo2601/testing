from src.main import ohce
import pytest
import sys


@pytest.mark.parametrize("name",["Pedro","Esteban","Gustavo"])
def test_main1(name, monkeypatch):
    monkeypatch.setattr(sys,"argv",["main.py",name])
    assert ohce('¡Buenos dias') == f'¡Buenos dias {name}!'
    assert ohce('¡Buenas tardes') == f'¡Buenas tardes {name}!'
    assert ohce('¡Buenas noches') == f'¡Buenas noches {name}!'
