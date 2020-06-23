from dataclasses import dataclass
from Stack_and_Queue.queue import MyQueue
import random as rd


@dataclass()
class TaskData:
    time: int = None
    type: int = None


class Task:
    def __init__(self, task_type, task_time):
        self.current_task = TaskData()
        self.current_task.time = task_time
        self.current_task.type = task_type

    def __str__(self):
        return '[' + str(self.get_type()) + ',' + str(self.get_time()) + ']'

    def get_time(self):
        return self.current_task.time

    def get_type(self):
        return self.current_task.type


class TaskGenerator:
    def __init__(self):
        self.queue1 = MyQueue()
        self.queue2 = MyQueue()

    def __str__(self):
        out = str(self.queue1) + '\n' + str(self.queue2)
        return out + '\n'

    def gen_task(self):
        task = Task(rd.randint(1, 2), rd.randint(4, 8))
        if task.get_type() == 1:
            self.queue1.push(task)
        else:
            self.queue2.push(task)

    def get_task(self):
        queue = rd.randint(1, 2)
        if queue == 1 and not self.queue1.check_empty():
            task = self.queue1.pop()
        elif queue == 2 and not self.queue2.check_empty():
            task = self.queue2.pop()
        elif queue == 1 and self.queue1.check_empty():
            task = self.queue2.pop()
        elif queue == 2 and self.queue2.check_empty():
            task = self.queue1.pop()
        else:
            task = None
        return task

    def none_task(self):
        return self.queue1.check_empty() and self.queue2.check_empty()