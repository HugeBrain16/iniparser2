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

def test_get():
    file = """
    rat = 5
    size = 9.0
    roach = false
    """

    parser = iniparser2.INI()
    parser.read(file)

    assert type(parser.get_int('rat')) is int, "boo"
    assert type(parser.get_float("size")) is float, "boo"
    assert type(parser.get_bool("roach")) is bool, "boo"

def test_get_bool():
    file = """
    imposter_sus = true
    me = false
    fard = 1
    fart = 0
    amogus = no
    no_more_amogus = yes
    lights = off
    bobux_generator = on
    """

    parser = iniparser2.INI()
    parser.read(file)

    assert parser.get_bool("imposter_sus") is True, "boo"
    assert parser.get_bool("me") is False, "boo"
    assert parser.get_bool("fard") is True, "boo"
    assert parser.get_bool("fart") is False, "boo"
    assert parser.get_bool("amogus") is False, "boo"
    assert parser.get_bool("no_more_amogus") is True, "boo"
    assert parser.get_bool("lights") is False, "boo"
    assert parser.get_bool("bobux_generator") is True, "boo"

def test_update():
    parser = iniparser2.INI()
    parser.update({"house": {"cockroach": "infinity", "trash": 0}})

    assert "house" in parser, "boo"
    assert type(parser["house"]) is dict, "boo"
    assert "cockroach" in parser["house"], "boo"
    assert "trash" in parser["house"], "boo"
    assert parser["house"]["cockroach"] == "infinity", "boo"
    assert parser["house"]["trash"] == 0, "boo"
