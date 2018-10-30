# print()方法只能打印异常信息，Python 中提供了 raise 方法来抛出一个异常信息。下面例子演示了 raise 的
# 用法
def say_error(name=None):
    if name is None:
        raise BaseException('"name" cant be empty')
    else:
        print("hello %s"%name)

say_error()