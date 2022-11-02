class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop(-1)

    def peek(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False


def user_input() -> str:
    string = input('Введите строку со скобками:')
    if not string:
        raise Exception('Строка пуста')
    for s in string:
        if s not in ('(', ')',
                     '[', ']',
                     '{', '}'):
            raise Exception(f'Строка содержит посторонний символ: {s}')
    return string


def is_balanced_check(parentheses_string: str) -> bool:
    open_parentheses = ('(', '[', '{')
    stack = Stack()
    for p in parentheses_string:
        if p in open_parentheses:
            stack.push(p)
        elif stack.is_empty():
            return False
        elif (p == ')' and stack.peek() == '(' or
                p == ']' and stack.peek() == '[' or
                p == '}' and stack.peek() == '{'):
            stack.pop()
        else:
            return False
    return True


if __name__ == '__main__':
    if is_balanced_check(user_input()):
        print('Сбалансированно')
    else:
        print('Несбалансированно')
