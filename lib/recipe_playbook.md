# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

The interface of a class includes:

The name of the class.
The design of its initializer, the parameters it takes, and their data types
The design of any properties the user will need to read or write, and their data types
The design of its public methods, including:
Their names and purposes
What parameters they take and the data types
What they return and that data type
Any other side effects they might have

```python
# EXAMPLE

class TodoList:
    

    def __init__(self):
        self.task = []

    def add_task(self, task):
        # Parameters
        #...task:string, representing a task
    def list(self):
        # Returns
        #...A list of incomplete tasks
    def list_incomplete(self):
        # Returns:
        #... A list of incomplete tasks
    def mark_complete(self, index):
        # Parameters
        #...index: an integer representing the task complet
        # side-effect:
        #...Removes the task at index from the list of tasks
        
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Initially, there are no tasks
"""
todo = TodoList()
todo.list_incomplete() # => []

"""
When we add a task
It is reflected in the list of tasks
"""
todo = TodoList()
todo.add("Go to the park")
todo.list_incomplete() # => ["Go to the park"]

"""
When we add multiple tasks
They are all reflected in the list of tasks
"""
todo = TodoList()
todo.add("Wash the dishes")
todo.add("Pick up the boys")
todo.add("Go to the nail shop")
todo.list_incomplete()
...# => ["Wash the dishes", "Pick up the boys", "Go to the nail shop"]

"""
When we add multiple tasks
And mark one complete
It disappears from the task list
"""
todo = TodoList()
todo.add("Wash the dishes")
todo.add("Pick up the boys")
todo.add("Go to the nail shop")
todo.mark_complete(1)
todo.list_incomplete()
...# => ["Wash the dishes", "Pick up the boys"]

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
