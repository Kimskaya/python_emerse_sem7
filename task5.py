# Создайте функцию для сортировки 
# файлов по директориям: видео, 
# изображения, текст и т.п. Каждая группа 
# включает файлы с несколькими расширениями. 
# В исходной папке должны остаться только те 
# файлы, которые не подошли для сортировки.

import os
import pathlib

__all__ = ['sort_files']


def sort_files(path):
    os.chdir(path)
    files = os.listdir()
    ext = {}
    for i in files:
        *_, extention = i.split(".")
        ext[extention] = ext.get(extention, []) + [i]
    for key, value in ext.items():
        os.mkdir(key)
        for i in value:
            os.replace(i, f"{key}\\{i}")

if __name__=="__main__":
    sort_files(r'C:\Users\zhdanovы\Desktop\Погружение в Питон\семинар 7\test')
