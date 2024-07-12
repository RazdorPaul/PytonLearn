class StepValueError(ValueError):
    def __str__(self):
        return ("шаг итеоации не может быть нулевым, объект не создан")

class Iterator:
    def __init__(self, start, end, step = 1):
        self.start = start
        self.end = end
        if step == 0:
            raise StepValueError
        else:
            self.step = step
        self.pointer = start

    def __iter__(self):
        return self

    def __next__(self):
        self.pointer = self.start
        self.start += self.step
        if (self.step < 0 and self.pointer < self.end) or (self.step > 0 and self.pointer > self.end):
            raise StopIteration
        return self.pointer

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as ex:
    print(ex)

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)
for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
