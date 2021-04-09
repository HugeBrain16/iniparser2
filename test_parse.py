# uhh... ¯\_(ツ)_/¯ -> i... don't... know...

import iniparser2

def test_parse():
	file = '''
	[E]
	name = Josh Tucker
	age = 14
	'''
	data = iniparser2.parse(file)
	assert 'E' in list(data), "Parse Error"

def test_parse_comment():
	file = '''
	[check]
	this = one
	#not = this
	'''
	data = iniparser2.parse(file)
	assert not 'not' in list(data['check']), "Parse error"

def test_parse_comment_section():
	file = '''
	;[dont]
	this = is
	not = in
	"dont" = section
	'''
	data = iniparser2.parse(file)
	assert not 'dont' in list(data), "Parse error"