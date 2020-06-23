class MyQueue:
    def __init__(self):
        self.data = []
        self.empty = True

    def __str__(self):
        out = '['
        for i in range(self.size() - 1):
            out += str(self.data[i])
        return out + ']'

    def push(self, item):
        self.data.insert(0, item)
        if self.empty:
            self.empty = False

    def pop(self):
        if not self.check_empty():
            out = self.data.pop()
        else:
            out = None
        if not self.data:
            self.empty = True
        return out

    def check_empty(self):
        if self.empty:
            return self.empty
        else:
            return self.empty

    def size(self):
        return len(self.data)