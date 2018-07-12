from traceback import print_exc
def divide(x, y):
    try:
        result = x / y
        print result
    except Exception as ex:
        print ex

divide(3, 0)
# jinsei wa kamihikouki