import os
import pyAesCrypt  # type: ignore


# Функция дешифровки.
def decryption(file, password):
    # Задаем размер буфера.
    buffer_size = 512 * 1024

    # Вызываем метод дешифровки.
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # Сообщение о шифровании.
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' дешифрован]")

    # Удаляем исходный файл.
    os.remove(file)


# Функция сканирования директории
def walking_by_dirs(dir, password):
    # Перебор всех поддиректорий в указанной директории.
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # Если находим, то дешифруем.
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # Если находим директорию, то повторяем цикл поиска файлов
        else:
            walking_by_dirs(path, password)


password = input('Введите пароль для дешифровки: ')
walking_by_dirs('путь до директории', password)
