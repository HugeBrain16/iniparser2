# iniparser2
  
[![Build Status](https://travis-ci.com/HugeBrain16/iniparser2.svg?branch=main)](https://travis-ci.com/HugeBrain16/iniparser2)  
  
**iniparser2** is An INI parser or a Config parser.  
  
this package is the improved version of [**iniparser**](https://github.com/HugeBrain16/iniparser) (it's gone, but will be back soon...) with more features.
  
---
  
## Installation
- using pip
    + from pypi
        * `pip install iniparser2`
        * `pip install iniparser2 --upgrade`
    + from github repository
        * `pip install git+https://github.com/HugeBrain16/iniparser2.git`
    + from source
        * `pip install .`
- from source
    + `python setup.py install`
    + `python setup.py install --user`
  
## Examples
#### reading ini basic example  
```py
import iniparser2

string = """
[stuff] # stuff that i stole from your house
microwave = 2
bagle = 8
money = $2100
person = 1
something_else = 69
"""

parser = iniparser2.INI()
parser.read(string)

print(parser)
```

#### read-write example
`something.ini`
```ini
[stuff] # stuff that i stole from your house
microwave = 2
bagle = 8
money = $2100
person = 1
something_else = 69
```
  
`le_main.py`
```py
import iniparser2

parser = iniparser2.INI(convert_property=True) # this `convert_property` does something like conversion...

parser.read_file('something.ini')
print(parser) # old stuff

# let's steal some more stuff
parser.set('person', parser.get('person', section='stuff') + 1, section='stuff') # kidnap one more person from your house
parser.set('bagle', parser.get('bagle', section='stuff') + 3, section='stuff') # and some bagles...
parser.set('dog', 1, section='stuff') # ohh, there is a dog, imma take that
parser.write('something.ini') # update file

print(parser) # let's see what i got here..., ohh wait!-

parser.remove_property('dog', section='stuff') # nevermind
parser.write('something.ini') # alright let's get outta here

# overread parser items
parser.read_file('something.ini')
print(parser) # new stuff
```
  
#### weird binary file stuff
```py
import iniparser2

string = """
[robot-1]
text = beep boop?

[robot-2]
text = boop? beep beep sus

[robot-3]
text = amogus
"""

parser = iniparser2.INI()
parser.write_string_bin('something.ini', string)
parser.read_binfile('something.ini')

print(parser)
```
  
### Exceptions
exceptions because why not
  
- base exception
    + `ParsingError`
        * `SectionError`
        * `PropertyError`
- something else
    + `DuplicateError`