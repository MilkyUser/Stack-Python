import sys


class Stack:
    def __init__(self):
        self.top = StackItem(None)
        self.size = 0

    def __add__(self, other):
        other.next_elem = self.top
        self.top = other
        self.size += 1
        return self

    def empilha(self, other):
        return self.__add__(other)

    def desempilha(self):
        if self.size > 0:
            to_remove = self.top
            self.top = self.top.next_elem
            self.size -= 1
            return to_remove

    def vazia(self):
        return self.size == 0

    def sort(self):
        aux_stack = Stack()

        while not self.vazia():
            temp = self.desempilha()

            while not aux_stack.vazia() and aux_stack.top.data < temp.data:
                self.empilha(aux_stack.desempilha())

            aux_stack.empilha(temp)

        return aux_stack


class StackItem:
    def __init__(self, data):
        self.data = data
        self.next_elem = None


if __name__ == '__main__':
    stack = Stack()

    for i in sys.argv[2:]:
        stack.empilha(StackItem(int(i)))

    stack = stack.sort()
    elem = stack.top

    for _ in range(stack.size - 1):
        print(elem.data, end=" ")
        elem = elem.next_elem

    print(elem.data)
