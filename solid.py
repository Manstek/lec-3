class Task: # S
    """Класс, для хранения данных о задаче."""
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.is_done = False


class TaskFilter: # O
    """Базовый класс для всех фильтров."""
    def filter(self, tasks: list[Task]):
        pass


class DoneFilter(TaskFilter):
    """Фильтр для выполненных задач."""
    def filter(self, tasks):
        done_tasks: list[TaskFilter] = []
        for task in tasks:
            if task.is_done:
                done_tasks.append(task)
        return done_tasks


class UncompletedFilter(TaskFilter):
    """Фильтр невыполненных задач."""
    def filter(self, tasks):
        uncompleted_tasks: list[TaskFilter] = []
        for task in tasks:
            if not task.is_done:
                uncompleted_tasks.append(task)
        return uncompleted_tasks


def show_tasks(tasks: list[Task], task_filter: TaskFilter): # L
    """Функция для отображения задач по фильтрам."""
    class_filter = task_filter
    for task in class_filter.filter(tasks):
        print(f'{task.title} ({task.description})')


task1 = Task('Мусор', 'Вынести мусор на кухне')
task2 = Task('Полы', 'Помыть полы')
task3 = Task('Посуда', 'Помыть посуду')
task2.is_done = True

show_tasks([task1, task2, task3], UncompletedFilter())

