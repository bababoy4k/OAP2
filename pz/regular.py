# Найдите все натуральные числа (возможно, окружённые буквами); 

re1 = '\d+' 

# Найдите все «слова», написанные капсом (то есть строго заглавными), возможно внутри настоящих слов (аааБББввв); 

re2 = '[A-ZА-ЯЁ]+' 

# Найдите слова, в которых есть русская буква, а за ней цифра; 

re3 = '[А-ЯЁа-яё]\d' 
 
# Найдите все слова, начинающиеся с русской или латинской большой буквы (\b — граница слова); 

re4 = '\b[А-ЯЁA-Z]\w+' 

# Найдите слова, которые начинаются на гласную (\b — граница слова); 

re5 = '\b[АОУЭЯЁЮИЕаоуэяёюиеAEIOUYaeiouy]\w+' 

# Найдите все натуральные числа, не находящиеся на границе слова; 

re6 = '\B\d+\B' 
 
# Найдите строчки, в которых есть символ * (. — это точно не конец строки!); 

re7 = '.*\*.*' 

# Найдите строчки, в которых есть открывающая и когда-нибудь потом закрывающая скобки; 

re8 = '.*\(.*\).*' 

# ??? Выделите одним махом весь кусок оглавления (в конце примера, вместе с тегами); 

re9 = '<\w.*?</\w.*>;' 
 
# ??? Выделите одним махом только текстовую часть оглавления, без тегов; 

re10 = '<.*?>(.*?)</.*?>;' 

# ??? Найдите пустые строчки; 

re11 = '\n()\n' 

# Найти все теги, не включая их содержимое. 

re12 = '</?\w.*?>'