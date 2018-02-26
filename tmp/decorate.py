def decorator_no_args(fn):
    print('Before wrapper')
    # 简单的包装 fn ，所以实际上装饰器等同于 decorator_no_args(fn)
    def wrapper(*args, **kw):
        print('   Before fn')
        fn(*args, **kw)
        print('   After fn')
    print('After wrapper')

    return wrapper

@decorator_no_args
def print_hello():
    print('        hello')

print_hello()


def decorator_args(*decorator_args):
    print('Before real_decorator')
    # 这才是真正的装饰器，所以实际上带参数的装饰器等同于 decorator_args(*decorator_args)(fn)
    def real_decorator(fn):
        print('    Before wrapper')
        def wrapper(*args, **kw):
            # 参数传入其实是利用了闭包
            print('       Decorator args:' + str(decorator_args))
            print('       Before fn')
            fn(*args, **kw)
            print('       After fn')
        print('    After wrapper')
        return wrapper

    print('After real_decorator')
    # 真正的装饰器其实是被“创建”出来的
    return real_decorator

@decorator_args('these', 'are', 'args')
def print_world():
    print('            world')

print_world()