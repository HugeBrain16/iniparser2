from iniparser2 import INI_TEMP, INI
import pytest

def test_main():
	x = INI('data.ini')
	assert x.filename == 'data.ini'

def test_temp():
	tmp = INI_TEMP()
	data = tmp.parse("""
	temp=IxHdgTszZ1oz

	[main]
	data=400
	""")

	assert data == {'temp': 'IxHdgTszZ1oz', 'main': {'data': '400'}}

def test_parse():
	file="""
	; no section here
	brief=test parse
	#nothing=yes
	comment_me=yes # ok

	[main]
	; a random comment
	data=400=500
	string="Hello"
	something="hi hi'hello"
	comment_here=again? # haha

	[[section]]
	; another random comment
	prop=nothing
	#e=haha
	"""

	tmp = INI_TEMP()
	data = tmp.parse(file)

	assert data == {'brief': 'test parse', 'comment_me': 'yes ', 'main': {'data': '400=500', 'string': '"Hello"', 'something': '"hi hi\'hello"', 'comment_here': 'again? '}, '[section': {'prop': 'nothing'}}