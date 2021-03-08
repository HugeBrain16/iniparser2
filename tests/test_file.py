from iniparser2 import INI

x = INI('data/test.ini')
data = x.get()

print(data)
