# List Of Files In The Project

## Code Files

### 0-lookup.py
Returns the list of all attributes and methods in the class.

### 1-my_list.py
prints out the elements of an instance of the `MyList` class in a sorted order (ascending order). NOTE that the `MyList` class is a subclass of the builtin `list` class.

### 2-is_same_class.py
contains the function `is_same_class` which takes two arguments; an object `obj` and a class `a_class` and  returns `True` if `obj` is an instance of `a_class`. Otherwise, it returns `False`.

### 3-is_kind_of_class.py
contains the function `is_kind_of_class` which takes two arguments; an object `obj` and a class `a_class` and returns `True` if `obj` is an instance of `a_class` or an instance of any of it's subclasses. Otherwise, it returns `False`.

### 4-inherits_from.py
contains the function `inherits_from` which takes two arguments; an object `obj` and a class `a_class` and returns `True` if `obj` is an instance of a subclass of `a_class`. Otherwise, it returns `False`.

### 5-base_geometry.py
contains the definition of an empty version of the `BaseGeometry` class. 

### 6-base_geometry.py
contains the definition of a version of the `BaseGeometry` class which is simply an extension of the version created in the `5-base_geometry.py` file created above.

### 7-base_geometry.py
contains the definition of a version of the `BaseGeometry` class which is simply an extensionof the version created in the `6-base_geometry.py` file above. It contains an incomplete implementation of the `integer_validator` method.

### 8-rectangle.py
contains the definition of the `Rectangle` class, a subclass of the version of the `BaseGeometry` class from the `7-base_geometry.py` file above.

### 9-rectangle.py
contains the definition of a more complete version of the `Rectangle` class introduced in the `8-rectangle.py` file above.

### 10-square.py
contains the definition of the class `Square`, a subclass of the `Rectangle` class which it'self is a subclass of the `BaseGeometry` class.

### 11-square.py
contains the definition of a more complete version of the `Square` class as introduced in the `10-square.py` file above.

### 100-my_int.py
contains the definition of user-defined class `MyInt` which is a subclass of the `int` class.

### 101-add_attribute.py
contains the function `add_attribute` which adds a specified attribute to a given object. If it can't it returns a `TypeError` and the message `can't add new attribute`     

## Test Files

### tests/1-my_list.txt
tests out the functionality of the code in the `1-my_list.py` file.

### tests/7-base_geometry.txt
tests out the functionality of the `integer_validator` method defined in the `BaseGeometry` class found in the `7-base_geometry.py` file.
