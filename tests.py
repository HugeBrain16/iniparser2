import iniparser2


def test_parse():
    file = """
    [me]
    name = josh
    age = 14
    """
    parser = iniparser2.INI(convert_property=True)
    parser.read(file)

    assert "me" in parser.ini, "boo"
    assert parser["me"]["name"] == "josh", "boo"
    assert parser["me"]["age"] == 14, "boo"


def test_comment():
    file = """
	[beep]
	robot = 4
	#human = 1032131923

	;[human]
	[#boop]
	"""
    parser = iniparser2.INI()
    parser.read(file)

    assert "human" not in parser.ini, "boo"
    assert "human" not in parser["beep"], "boo"
    assert "#boop" in parser.ini, "boo"


def test_conversion():
    file = """
	rat = 5
	size = 9.0
	roach = false
	mushroom = "infinity"
	"""

    parser = iniparser2.INI(convert_property=True)
    parser.read(file)

    assert type(parser["rat"]) is int, "boo"
    assert type(parser["size"]) is float, "boo"
    assert type(parser["roach"]) is bool, "boo"
    assert type(parser["mushroom"]) is str, "boo"
