# 11_duplicates

## Описание

Скрипт принимает на вход папку, просматривает все файлы в
ней и всех подпапках и сообщает, если находит дубликаты (файлы
с одинаковым именем и размером).

## Использование

Скрипт принимает на вход директорию. Задать ее можно двумя способами:

* явно указать при запуске скрипта: 
```sh
$ python3.5 ./duplicates.py ./SomeDir
```

* запустить скрипт на выполнение командой:
```sh
$ python3.5 ./duplicates.py
```
В этом случае потребуется ввести директорию отдельно:
```sh
$ Enter directory > ./SomeDir
```
При попытке передать скрипту более двух параметров будет выведено сообщение:
```sh
Error: too many parameters are transferred
```

## Пример

Ниже приведен пример использования скрипта и его вывод:
```sh
$ python3.5 ./duplicates.py ./Dir
File File3.txt has duplicates in the following directories:
./Dir/Dir3/File3.txt
./Dir/Dir3/Dir32/File3.txt
File File1.txt has duplicates in the following directories:
./Dir/Dir1/File1.txt
./Dir/Dir2/File1.txt
./Dir/Dir3/File1.txt
File File2.txt has duplicates in the following directories:
./Dir/File2.txt
./Dir/Dir2/File2.txt
```