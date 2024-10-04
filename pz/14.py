import re

# Открытие файла для чтения
with open("Dostoevsky.txt", 'r', encoding='utf-8') as file:
    text = file.read()

# Регулярное выражение для поиска фамилий с инициалами
pattern = r'\b([А-ЯЁ][а-яё]+)\s+([А-ЯЁ]\.\s+[А-ЯЁ]\.)\b'

# Поиск всех совпадений
matches = re.findall(pattern, text)

# Вывод результатов
print("Фамилии с инициалами:")
for surname, initials in matches:
    print(f"{surname} {initials}")

