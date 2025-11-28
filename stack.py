from typing import Any


class Stack:
    """Класс, реализующий структуру данных - стек."""

    def __init__(self):
        self.__items: list[Any] = []
    
    def push(self, item):
        """Добавить в стек."""
        self.__items.append(item)
    
    def pop(self):
        """Удалить последний элемент из стека."""
        return self.__items.pop()
    
    def see_last_el(self):
        """Просмотр последнего элемента."""
        return self.__items[-1]
    
    def len_stack(self):
        """Просмотр длины стека."""
        return len(self.__items)
    

stack = Stack()
stack.push('Hello, Git!')
stack.push(False)
stack.push(12500)
stack.push({
    "user": "aleksandr",
    "age": 22
})

print(stack.len_stack())
print(stack.pop())
print(f'{stack.see_last_el()}, длина стека -  {stack.len_stack()}')
print(stack.len_stack())
stack.push('Последний элемент')
print(stack.len_stack())
