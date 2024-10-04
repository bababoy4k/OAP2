# Дана строка, содержащая полное имя файла. Выделить из этой строки название последнего каталога (без символов «\»).
# Если файл содержится в корневом каталоге, то вывести символ «\ ».

def extract_last_directory(file_path):
    directories = file_path.split("\\")
    last_directory = directories[-1]

    if last_directory == '':
        return "\\"
    else:
        return last_directory

file_path = input("Введите полное имя файла: ")
last_directory = extract_last_directory(file_path)
print("Название последнего каталога:", last_directory)