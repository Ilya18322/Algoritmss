from dataclasses import dataclass
from Stack_and_Queue.task import Task
from Stack_and_Queue.stack import MyStack


@dataclass()
class Thread:
    work_time: int = None
    task_type: int = None
    idle: bool = True


class Processor:
    def __init__(self):
        self.thread1 = Thread()
        self.thread2 = Thread()
        self.wait = MyStack()

    def __str__(self):
        out = '|thread|type|time|idle |\n'
        out += '{:<9}{:<5}{:<5}{:<6}'.format('  1', str(self.thread1.task_type), str(self.thread1.work_time),
                                             str(self.thread1.idle)) + '\n'
        out += '{:<9}{:<5}{:<5}{:<6}'.format('  2', str(self.thread2.task_type), str(self.thread2.work_time),
                                             str(self.thread2.idle))
        return out

    def add_task(self, task: Task):
        if task.get_type() == 1:
            if self.thread1.idle:
                self.thread1.task_type = task.get_type()
                self.thread1.work_time = task.get_time()
                self.thread1.idle = False
            elif self.thread1.task_type == 2:
                denied_task = Task(self.thread1.task_type, self.thread1.work_time)
                self.thread1.task_type = task.get_type()
                self.thread1.work_time = task.get_time()
                self.wait.push(denied_task)
            else:
                self.wait.push(task)
        elif task.get_type() == 2:
            if self.thread2.idle:
                self.thread2.task_type = task.get_type()
                self.thread2.work_time = task.get_time()
                self.thread2.idle = False
            elif self.thread1.idle:
                self.thread1.task_type = task.get_type()
                self.thread1.work_time = task.get_time()
                self.thread1.idle = False
            else:
                self.wait.push(task)

    def __run_task_t1(self):
        self.thread1.work_time -= 1
        if self.thread1.work_time <= 0:
            self.thread1.idle = True
            self.thread1.task_type = None
            self.thread1.work_time = None

    def __run_task_t2(self):
        self.thread2.work_time -= 1
        if self.thread2.work_time <= 0:
            self.thread2.idle = True
            self.thread2.task_type = None
            self.thread2.work_time = None

    def running(self):
        if not self.thread1.idle:
            self.__run_task_t1()
        else:
            self.thread1.idle = True
        if not self.thread2.idle:
            self.__run_task_t2()
        else:
            self.thread2.idle = True

    def idle_thread(self):
        return self.thread1.idle or self.thread2.idle

    def idle_proc(self):
        return self.thread1.idle and self.thread2.idle