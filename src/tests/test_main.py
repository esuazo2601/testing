from src.main import ohce

def test_main1():
    assert ohce('¡Buenos dias!') == '¡Buenos dias!'
    assert ohce('¡Buenas tardes!') == '¡Buenas tardes!'
    assert ohce('¡Buenas noches!') == '¡Buenas noches!'

