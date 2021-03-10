from iniparser2 import INI_TEMP, INI
import pytest

def test_main():
	x = INI('data.ini')
	assert x.filename == 'data.ini'

def test_pass_section_x():
	x = INI('data.ini','main')
	assert x.pass_section == False

def test_pass_section_y():
	x = INI('data.ini')
	assert x.pass_section == True

def test_trace_x():
	x = INI('data.ini',trace_verbose=2)
	assert x.trace == False

def test_parse_no_section():
	file="""
	name=ok
	"""
	x = INI_TEMP()
	data = x.parse(file)
	assert data['name'] == 'ok'

def test_parse_section():
	file="""
	name=ok

	#[data]
	ok=yes
	"""
	x = INI_TEMP()
	data = x.parse(file)
	assert data['ok'] == 'yes'

def test_parse_comment():
	file="""
	name=ok
	#age=no
	"""

	x = INI_TEMP()
	data = x.parse(file)
	assert (not 'age' in data) == True

def test_parse_comment_sc():
	file="""
	; test semicolon comment
	name=ok
	;age=np
	"""

	x = INI_TEMP()
	data = x.parse(file)
	assert (not 'age' in data or not ';age' in data) == True