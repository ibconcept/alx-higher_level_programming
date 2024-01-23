
0x06-python-classes
Why Python programming is awesome:
Readability and simplicity: Python code is easy to read and write, promoting a clean and readable syntax.
Extensive libraries: Python has a vast standard library and a rich ecosystem of third-party libraries, making it versatile for various tasks.
Community support: Python has a large and active community, providing support through forums, documentation, and a wealth of online resources.
Cross-platform compatibility: Python code can run on different operating systems without modification, enhancing portability.
Versatility: Python is suitable for various applications, from web development to data science and machine learning.
Object-Oriented Programming (OOP):
OOP is a programming paradigm that organizes code into objects, each representing an instance of a class. Objects have attributes (characteristics) and methods (functions) associated with them. OOP concepts include encapsulation, inheritance, and polymorphism.

“First-class everything”:
In Python, everything is treated as an object, and objects can be assigned to variables, passed as arguments, and returned as values. This is known as "first-class everything" and is a key feature of Python's flexibility.

Class:
A class is a blueprint for creating objects. It defines attributes and methods that will be associated with the objects created from the class.

Object and Instance:
An object is an instance of a class. When a class is instantiated, it creates an object, and that object is referred to as an instance of the class.

Difference between a class and an object or instance:
A class is a blueprint, while an object (or instance) is a concrete realization of that blueprint.

Attribute:
An attribute is a characteristic or property of an object, defined within a class.

Public, Protected, and Private Attributes:
Public attributes are accessible from outside the class.
Protected attributes have a single leading underscore and are considered internal, but they can still be accessed.
Private attributes have a double leading underscore and are meant to be private, usually accessed through name mangling.
Self:
self is a convention in Python that refers to the instance of the class. It is the first parameter in every method of a class and is used to access attributes and methods within the class.

Method:
A method is a function associated with a class, typically performing actions on the class's instance.

Special __init__ method:
__init__ is a special method used for initializing object attributes when an object is created.

Data Abstraction, Data Encapsulation, and Information Hiding:
Data Abstraction: Hiding the implementation details and exposing only what is necessary.
Data Encapsulation: Bundling data (attributes) and methods that operate on the data within a single unit (class).
Information Hiding: Restricting access to certain details of an object and exposing only what is necessary.
Property:
A property is a special kind of attribute that is accessed like an attribute but has methods for getting, setting, and deleting its value.

Difference between an attribute and a property in Python:
An attribute is a characteristic of an object, while a property is a special kind of attribute that has getter, setter, and deleter methods.

Pythonic way to write getters and setters:
Use the @property, @<property_name>.setter, and @<property_name>.deleter decorators.

Dynamically create arbitrary new attributes:
Use the setattr function to dynamically set attributes on instances.

Bind attributes to object and classes:
Attributes are bound to objects at runtime by assignment. Class attributes are set within the class body.

__dict__ of a class/instance:
__dict__ is a dictionary containing a class or instance's attributes.

How Python finds attributes:
Python looks for attributes in the instance, then in the class, and finally in the class's ancestors.

How to use the getattr function:
getattr(obj, 'attribute_name') is used to get the value of an attribute dynamically. It raises an AttributeError if the attribute is not found
