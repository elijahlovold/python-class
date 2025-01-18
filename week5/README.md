# Notes - Week 5 

## Content

* pip 
* functions 
    * recursion

### modules 
* how to install packages

* pip commands
to install a new package: 
    `pip install` name_of_package
    e.g., `pip install matplotlib`
to list existing packages: 
    `pip list`
to uninstall a package: 
    `pip uninstall` name_of_package
    e.g., `pip uninstall matplotlib`

* how to import modules

to import the whole module: 
`import matplotlib`

to import a part of the module as an alias: 
`import matplotlib.pyplot as plt`

to import an object from the package
`from matplotlib.pyplot import plot`

to import an all objects from the package (not recommended)
`from matplotlib.pyplot import *`

note, you can also import files in your same dir as modules
use '.' to indicate dir seperation

example, with this structure: 
```
main.py
utils/helpers.py
```
to import helpers.py in main.py, use: 
`import utils.helpers as hlp`
note the '.' replaces / and the .py is not needed


### functions
#### basic function structure 
```
def name_of_function(arg1, arg2, ...): 
    # code implementation

    return ret1, ret2
```

example:
```
def is_int(value): 
    ret = type(value) == int

    return ret
```

now, when we call it, whatever we put in () replaces value, i.e., the input args. also, the function call itself gets replaced by whatever was returned

example using this function
```
query = is_int(23)
# query now equals True

# note, the var 'value' in the is_int function becomes 23 - the input
# also, the is_int(23) is 'replaced' by whatever returns, in this case the value 
# of the ret variable in the function. 

query = is_int('not an int')
# query now equals False
```

note, when we pass multiple args, each arg is assigned to the corresponding
variable in the function header. 

example:
```
def do_something_helpful(foo, bar, temp): 
    # does some code
```

when we call the function and pass in 1, 2, 3, the variables foo, bar, temp are assigned these values in order

example:
```
do_something_helpful(1, 2, 3)

# in the function (note, i just mean here the vars get assigned the inputs, 
                    don't take any meaning from the syntax as this technically
                    does something else...)
def do_something_helpful(foo=1, bar=2, temp=3): 
    ...
```

note, we can also pass in variables here like: 
```
do_something_helpful(x, y, z)

# in the function
def do_something_helpful(foo=x, bar=y, temp=z): 
    ...
```

additionally, we can all functions within functions like: 

```
def do_something_helpful(foo, bar, temp): 
    # some code ...

    foo_is_int = is_int(foo)

    # more code...
```

#### recursion
note! if we call the function inside itself, this is valid. it is called a **recursive** function. be careful as these as they can call recurse infinitely and crash the program. generally this crashes due to stack overflow; however, python knows what's happening here and just throws a max recursion depth error. 

example: 
``` 
def prog_breaker(iteration): 
    print(iteration)
    prog_breaker(iteration+1)
```

because of the potential safety issues with this type of function, they should used carefully and **ALWAYS** have some exit condition **BEFORE** recursing. For some examples of when this would be helpful: 
* printing a list which can have lists inside
* solving knight's tour
* factorial and fibonacci
* binary search


#### default arguments

some more details on function usage, say you have a parameter you only want to use sometimes but normally want it to just assume a default arg. You can do this by adding = followed by the default value. this is called a **default parameter**

example: 
```
def another_function(foo, bar=3): 
    # some code

# when called like: 
another_function(2) 
# inside the function, foo=2 and bar=3 

# however, we can still do: 
another_function(2, 2345) 
# inside the function, foo=2 and bar=2345 
```

#### keyword arguments

another cool trick, say you forget the arg order or want to specify each arg for better readability, in the function call, you can perform the assignment of the variables using their actual names (in the function header). these are called **keyword arguments** when you pass them in this manner. 

example: 
```
def kwarg_function_example(foo, bar): 
    ...

kwarg_function_example(foo=3, bar=4)

# this works regardless of order
kwarg_function_example(foo=3, bar=4)

# you can mix and match too
kwarg_function_example(3, bar=4)

# you can't do ANY positional args after kwargs 
kwarg_function_example(foo=3, 8)    # this is invalid

# you also can't do the same positional args as the kwargs 
kwarg_function_example(3, 8, bar=9)    # this is invalid

```


note, if you see these and want to know what they are, ask. We'll probably revisit this in the future...
```
def some_func(*args, **kwargs): 
    ...
```

