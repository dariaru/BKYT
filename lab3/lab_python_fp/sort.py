#data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
#Вывод: [123, 100, -100, -30, 30, 4, -4, 1, -1, 0]
#Необходимо решить задачу двумя способами:
#С использованием lambda-функции.
#Без использования lambda-функции.

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sorted(data, reverse=True, key=abs)
    print("without lambda", result)

    result_with_lambda = sorted(data, reverse=True, key=lambda x: abs(x))
    print("with lambda", result_with_lambda)