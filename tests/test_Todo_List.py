from lib.Todo_List import *
import pytest

def test_initially_has_no_tasks():
    todo = TodoList()
    assert todo.list_incomplete() == []

def test_add_task_reflected_in_tasks():
    todo = TodoList()
    todo.add("Go to the park")
    assert todo.list_incomplete() == ["Go to the park"]

def test_add_multiple_task():
    todo = TodoList()
    todo.add("Wash the dishes")
    todo.add("Pick up the boys")
    todo.add("Go to the nail shop")
    assert todo.list_incomplete() == ["Wash the dishes", "Pick up the boys", "Go to the nail shop"]

def test_marks_task_complete():
    todo = TodoList()
    todo.add("Wash the dishes")
    todo.add("Pick up the boys")
    todo.add("Go to the nail shop")
    todo.mark_complete(2)
    assert todo.list_incomplete() == ["Wash the dishes", "Pick up the boys"]

# If we try to mark a task complete that does not Exist 
# It raises an error

def test_mark_task_that_does_not_exist():
    todo = TodoList()
    todo.add("Go to the park")
    with pytest.raises(Exception) as err:
        todo.mark_complete(-1)
    assert str(err.value) == "No such task to mark complete"

