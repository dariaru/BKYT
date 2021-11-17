# Здесь должна быть реализация декоратора
def print_result(func):
     def decor(*args, **kwargs):
         result = func(*args, **kwargs)
         print(func.__name__)
         if isinstance(result, list):
             for i in result:
                 print(i)
         elif isinstance(result, dict):
             for i in result:
                print(str(i) + " = " + str(result[i]))
         else:
            print(result)
         return result
     return decor


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 11, 'b': 82}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()