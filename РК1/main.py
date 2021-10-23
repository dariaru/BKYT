from operator import itemgetter

class File:
    """Файл"""
    def __init__(self, id, name_file, catalog_id, size):
      self.id = id
      self.name_file = name_file
      self.catalog_id = catalog_id
      self.size = size

class Catalog:
    """Каталог"""
    def __init__(self, id, name_catalog):
        self.id = id
        self.name_catalog = name_catalog

class DirectoryFiles:
    """Файлы каталога для связи М:М"""
    def __init__(self, catalog_id, file_id):
        self.catalog_id = catalog_id
        self.file_id = file_id
#Файлы
files = [
    File(1, 'photo.pdf', 2, 4.5),
    File(2, 'image.pdf', 3, 2.1),
    File(3, 'image.jpg', 4, 3.25),
    File(4, 'image0.jpg', 4, 1.7),
    File(5, 'my_work.pdf', 1, 1.3),
    File(6, 'dz1_oop.jpg', 3, 2.4)
]

#Каталоги
cataloges = [
    Catalog(1, 'Рабочий стол'),
    Catalog(2, 'Панель управления'),
    Catalog(3, 'Папка1'),
    Catalog(4, 'Папка2'),
    Catalog(5, 'Работы'),
    Catalog(6, 'Домашнее задание'),
]

directory_files = [
    DirectoryFiles(2, 1),
    DirectoryFiles(3, 2),
    DirectoryFiles(4, 3),
    DirectoryFiles(4, 4),
    DirectoryFiles(1, 5),
    DirectoryFiles(3, 6)
]

def main():
    #связь один-ко-многим
    one_to_many = [(e.name_file, e.size, d.name_catalog)
                   for d in cataloges
                   for e in files
                   if e.catalog_id == d.id]

    # связь многие-ко-многим
    many_to_many_temp = [(d.name_catalog, ed.file_id, ed.catalog_id)
                         for d in cataloges
                         for ed in directory_files
                         if d.id == ed.catalog_id]

    many_to_many = [(e.name_file, e.size, cat_name)
                    for cat_name, file_id, catalog_id in many_to_many_temp
                    for e in files if e.id == file_id]

    print('Задание B1')
    """
        "Файл" и "Каталог" связаны соотношением один-ко-многим. 
        Вывести список всех файлов, у которых название начинается на "i", и названия их каталогов.
    """
    res_1 = []
    for name_file, size, name_catalog in one_to_many:
        if name_file[0] == 'i':
            res_1.append((name_file, name_catalog))
    print(res_1)

    print('Задание B2')
    """
        "Файл" и "Каталог" связаны соотношением один-ко-многим. 
        Вывести список каталогов с минимальным размером файлов в каждом каталоге, отстортированный по минимальному размеру.
        P.S. размер файлов указан в Мб.
    """
    res_21 = []
    # Список каталогов
    for d in cataloges:
        d_files = list(filter(lambda i: i[2] == d.name_catalog, one_to_many))
        # Если каталог не пустой
        if len(d_files) > 0:
            # Размеры файлов
            d_sizes = [size for _, size, _ in d_files]
            min_size = min(d_sizes)
            res_21.append((d.name_catalog, min_size))
    res_2 = sorted(res_21, key=itemgetter(1))
    print(res_2)

    print('Задание B3')
    """
        "Файл" и "Каталог" связаны соотношением многие-ко-многим. 
        Вывести список всех связанных каталогов и файлов, отстортированный по файлам, сортровка по каталогам произвольная.
    """
    res_31 = []
    for name_file, size, name_catalog in many_to_many:
        res_31.append((name_file, name_catalog))
    res_3 = list(sorted(res_31, key=itemgetter(0)))
    print(res_3)

if __name__ == '__main__':
    main()