# peepy
A simple Observer Pattern implementation with decorators

## Installation

Simply instasll from pypi:

``` bash
pip3 install peepy
```

### Usage

Observables can be connected to oserver callbacks siply by callling the bind_to method or by using the observe, observe_dict and observer_function decorators

``` python
from peepy.Observables import Observable, ObservableDict, observe, observe_dict

foo = Observable('important object')
foo2 = Observable('important object 2')

@observe(foo, foo2)
def observer(label, old, new):
    print('Changing {0}\'s value from {1} to {2}'.format(label, old, new))

foo.value = 'bar'
foo.value = 'baz'

foo2.value = foo

foo_dict = ObservableDict({'foo': 1, 'bar':{}})

@foo_dict.observer_function
def dict_observer(label, old, new):
    print('Changing key {0} from {1} to {2}'.format(label, old, new))
    
foo_dict['foo'] = 2
foo_dict['foo2'] = 20
foo_dict['bar'] = {'baz':None}
```
