# iniparser2

An INI parser or maybe a Config parser.

this module is the improved version of [**iniparser**](https://github.com/HugeBrain16/iniparser) with more features.

---

# Quick Start
how to import this module is by putting the module folder in the same directory as the main Python file to execute.
</br>

### For Example </br>

this is your directory -> `./main.py`, then put the module folder in `./` <- here, or... you can put it in `.../Python3x/Lib/site-packages/` <- here, so you don't have to
put another folder of this module into another directories

## Examples

**These examples below is for getting the value from the properties**
</br>
basic example

`test.ini`:
```ini
name=Mike Hawk
```

`test.py`:
```py
from iniparser2 import INI

x = INI('test.ini')
data = x.get()

print(data)
```

#### Output:
```py
{'name': 'Mike Hawk'}
```

**OR** With `temp` method

`test.py`:
```py
from iniparser2 import INI_TEMP

x = INI_TEMP()
data = x.parse(
"""
name=Mike Hawk
""")

print(data)
```

#### Output:
```py
{'name': 'Mike Hawk'}
```

**OR** With section

`test.ini`:
```ini
[id]
name=Mike Hawk
age=-69
```

`test.py`:
```py
from iniparser2 import INI

x = INI('test.ini','id') # 'id' is the section name
data = x.get()

print(data)
```

#### Output:
```py
{'name': 'Mike Hawk', 'age': '-69'}
```

**pass_section** argument

`test.ini`:
```ini
brief=someone's identity

[id]
name=Mike Hawk
age=-69
```

`test.py`:
```py
from iniparser2 import INI

x = INI('test.ini',pass_section=True) # or you just don't have to put the section name, it will override the `pass_section` argument
data = x.get()

print(data)
```

#### Output:
```py
{'brief': "someone's identity", 'id': {'name': 'Mike Hawk', 'age': '-69'}}
```

**These example below is for properties stuff**
</br>
basic example

the `test.ini` file is empty

`test.py`:
```py
from iniparser2 import INI

x = INI('test.ini')
x.set('name','Mike Hawk')
```

and the `test.ini` file would be like this
```ini
name=Mike Hawk
```

it would update the value of the property if there's an existing property inside the file

to unset property
`test.py`:
```py
from iniparser2 import INI

x = INI('test.ini')
x.unset('name')
```

and the property would be gone!
