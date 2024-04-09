# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.

class TodoList():
    def __init__(self):
        self._tasks = []

    def add(self, task):
        self._tasks.append(task)
    
    def list_incomplete(self):
        return self._tasks

    def mark_complete(self, index):
        if index < 0 or index >= len(self._tasks):
            raise Exception("No such task to mark complete")
        del self._tasks[index]
        
