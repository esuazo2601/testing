from src.main import ohce, greetings

def test_main1():
    assert ohce() == '¡Buenas tardes'

def test_main2():
    assert ohce() == '¡Buenos dias!'
