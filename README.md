# 11_duplicates

## Описание

Скрипт принимает на вход папку, просматривает все файлы в
ней и всех подпапках и сообщает, если находит дубликаты (файлы
с одинаковым именем и размером).

## Использование

Скрипт принимает на вход директорию:

```sh
$ python3.5 ./duplicates.py ./SomeDir
```

Для получения справки можно использовать аргументы -h или --help:

```sh
$ python3.5 ./duplicates.py -h
usage: duplicates.py [-h] dir

Script for search of files duplicates

positional arguments:
  dir         Directory for search

optional arguments:
  -h, --help  show this help message and exit

```

## Пример

Ниже приведен пример использования скрипта и его вывод:
```sh
$ python3.5 ./duplicates.py ./Dir
File File2.txt (size: 36) has duplicates in the following directories:
./Dir/File2.txt
./Dir/Dir2/File2.txt
File File1.txt (size: 31) has duplicates in the following directories:
./Dir/Dir1/File1.txt
./Dir/Dir2/File1.txt
File File1.txt (size: 63) has duplicates in the following directories:
./Dir/Dir3/Dir31/File1.txt
./Dir/Dir3/Dir32/File1.txt

```