from Stack_and_Queue.processor import Processor
from Stack_and_Queue.task import TaskGenerator


generator = TaskGenerator()
processor = Processor()

for i in range(50):
    generator.gen_task()

while True:
    task = generator.get_task()
    if processor.idle_thread():
        if not generator.none_task():
            processor.add_task(task)
        elif not processor.wait.check_empty():
            processor.add_task(processor.wait.pop())
    processor.running()
    print('Tasks\n', generator)
    print('Processor:\n', processor)
    print('Stack:', processor.wait)
    if generator.none_task() and processor.wait.check_empty() and processor.idle_proc():
        break