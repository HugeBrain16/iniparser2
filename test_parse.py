import iniparser2

def test_parse():
	file = "name=ahaha\nage=99"
	data = iniparser2.parse(file)
	assert 'name' in list(data), "Parse Error"

def test_parse_comment():
	file = '#name=ahaha\nage=1293'
	data = iniparser2.parse(file)
	assert not 'name' in list(data), "Parse error"

def test_parse_comment_section():
	file = ';[data]'
	data = iniparser2.parse(file)
	assert not 'data' in list(data), "Parse error"