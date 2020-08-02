class create_message(str):
    def __call__(self, s = ''):
        return create_message(f'{self} {s}'.strip())



def create_message2(s):
    xs = [s]
    def wrapper(other=''):
        if not other:
            return ' '.join(xs)
        xs.append(other)
        return wrapper
    return wrapper


class add(int):
    def __call__(self,n):
        return add(self+n)

def add(x=0):
    t = [x]
    # print(t)
    def wrapper(s=0):
        print(t)
        if not s:
            return sum(t)
        t.append(s)
        return wrapper
    return wrapper


print(create_message2("Hello")("World!")("how")("are")("you?")())

print(add(1)(2)(3)
