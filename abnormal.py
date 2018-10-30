# try:
#     open("abc.txt","r")
#     print(a)
# except BaseException as msg1:
#     print(msg1)

try:

    print(b)
except NameError as msg:
    print(msg)
finally:
    print("不管是否有异常都执行")