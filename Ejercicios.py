class Stack:
    def __init__(self, limit):
        self.limit = limit
        self.items = [None] * self.limit
        self.size_stack = 0

    def push(self, item: int):
        if self.size_stack <= self.limit - 1:
            self.items[self.size_stack] = item
            self.size_stack += 1
        else:
            print("Llorelo")

    def pop(self):
        if not self.is_empty():
            self.size_stack -= 1
            item_delete = self.items[self.size_stack]
            self.items[self.size_stack] = None
            return item_delete
        else:
            raise Exception == "Error de pila está tratando de borrar una posición no accesible"

    def top(self):
        if not self.is_empty():
            return "Su último elemento es: {0}".format(self.items[self.size_stack - 1])
        else:
            raise Exception == "Error de pila está tratando de ingresar o borrar una posición no accesbible"

    def is_empty(self):
        return self.size_stack == 0

    def size(self):
        return "La longitud de la lista es: {0}".format(len(self.items))


stack = Stack(3)

print(stack.pop())


