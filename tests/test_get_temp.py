from iniparser2 import INI_TEMP

file = """
[character]
name=Esmephasia Williamsanic

[statistic]
power=80
energy=10

[inventory]
gold=50000
gems=40000
"""

x = INI_TEMP()
data = x.parse(file)

print(data)
