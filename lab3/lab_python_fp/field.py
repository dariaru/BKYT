# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}
def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for dictionary in items:
            note = dictionary.get(args[0])
            if note is not None:
                yield note
    else:
        for _dictionary in items:
            d = dict()
            for arg in args:
                note = _dictionary.get(arg)
                if note is not None:
                    d[arg] = note
            if len(d) != 0:
                yield d

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': None, 'price': 100, 'color': 'black'},
        {'title': 'Кровать', 'price': 15000, 'color': 'yellow'}
    ]
    data1 = list()
    data2 = list()

    for i in field(goods, 'title'):
        data1.append(i)
    print(data1)

    for i in field(goods, 'title', 'price'):
        data2.append(i)
    print(data2)