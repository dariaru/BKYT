import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *

class TddTest(unittest.TestCase):
    def test_1(self):
        one_to_many = [(e.name_file, e.size, d.name_catalog)
                       for d in cataloges
                       for e in files
                       if e.catalog_id == d.id]
        self.assertEqual(first_task(one_to_many), [('image.pdf', 'Папка1'), ('image.jpg', 'Папка2'), ('image0.jpg', 'Папка2')])

    def test_2(self):
        one_to_many = [(e.name_file, e.size, d.name_catalog)
                       for d in cataloges
                       for e in files
                       if e.catalog_id == d.id]
        self.assertEqual(second_task(one_to_many), [('Рабочий стол', 1.3), ('Папка2', 1.7), ('Папка1', 2.1), ('Панель управления', 4.5)])

    def test_3(self):
        many_to_many_temp = [(d.name_catalog, ed.file_id, ed.catalog_id)
                             for d in cataloges
                             for ed in directory_files
                             if d.id == ed.catalog_id]

        many_to_many = [(e.name_file, e.size, cat_name)
                        for cat_name, file_id, catalog_id in many_to_many_temp
                        for e in files if e.id == file_id]

        self.assertEqual(third_task(many_to_many),
                         [('dz1_oop.jpg', 'Папка1'), ('image.jpg', 'Папка2'), ('image.pdf', 'Папка1'), ('image0.jpg', 'Папка2'),
                          ('my_work.pdf', 'Рабочий стол'), ('photo.pdf', 'Панель управления')])


if __name__=='__main__':
    unittest.main()