#2.	Из заданной строки отобразить только цифры. Использовать библиотеку string.
#Строка - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high.

import string

# Заданная строка
text = "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high."

# Отображение только цифр с использованием библиотеки string
digits = ''.join([char for char in text if char in string.digits])

# Вывод результата
print("Цифры в строке:", digits)