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

#### These examples is for getting the value from the properties

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
{'name':'Mike Hawk'}
```

**OR** With `stream` method

`test.py`:
```py
from iniparser2 import INI_STREAM

x = INI_STREAM()
data = x.parse(
"""
name=Mike Hawk
""")

print(data)
```

#### Output:
```py
{'name':'Mike Hawk'}
```

**OR** With tag

`test.ini`:
```ini
[id]
name=Mike Hawk
age=-69
```

`test.py`:
```py
from iniparser2 import INI

x = INI('test.ini','id') # 'id' is the tag name
data = x.get()

print(data)
```

#### Output:
```py
{'name':'Mike Hawk','age':'-69'}
```

**pass_tag** argument

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

x = INI('test.ini',pass_tag=True) # or you just don't have to put the tag name, it will override the `pass_tag` argument
data = x.get()

print(data)
```

#### Output:
```py
{"brief":"someone's identity"}
```

#### These example is for properties stuff

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
