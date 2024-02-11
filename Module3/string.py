S='This is very long string. \\ It has several sentences an\n seven even the new line symbol \t:-)'
# print(len(S))
se="se"

# Екрановані послідовності
# S = "s\npajd\ta\nbbb"
# print(S)
# Невідформатовані рядки (ігнорують екранування)
# S = r"C:\temp\new"
# print(S)

# Пошук підрядків. Повертає номер першого входження або -1
# print(S.find(se))
# # Пошук з кінця
# print(S.rfind(se))

# Пошук підрядка. Якщо його немає - вибиває ValueError
# print(S.index(se))
# # Аналогічно з кінця
# print(S.rindex(se))

# # Заміна шаблону
# print(S.replace('e', '3'))
# # Розбиття рядків
# print(S.split(' '))

# #Чи складається рядок з:
# # цифр
# print(S.isdigit())
# # літер
# print(S.isalpha())
# # цифр або літер
# print(S.isalnum())
# # з літер нижнього регістру
# print(S.islower())
# # з літер верхнього регістру
# print(S.isupper())
# # Пробілів та невидимих символів
# print(S.isspace())
# # слів, що починаються з великої літери
# print(S.istitle())

# # Зробити усі слова великими літерами
# print(S.upper())
# # Зробити усі слова маленькими
# print(S.lower())
# # Чи починається рядок з
# print(S.startswith(se))
# # Чи закінчується рядок на
# print(S.endswith(se))
# # Рядок зі списку
# print(S.join(['This',"is","the","code"]))
# # ASCII номер символа
# print(ord('a'))
# # символ з числа
# print(chr(97))
# # Рядок з великої літери
# print(S.capitalize())
# # Замінює табуляцію на пробіли (8 за промовчанням)
# print(S.expandtabs(4))# python way
# # Видалення пробілів перед рядком
# print(S.lstrip())
# # після рядка
# print(S.rstrip())
# # обабіч рядка
# print(S.strip())
# # Змінює реєстр __УСІХ__ символів
# print(S.swapcase())
# # Кожне слово з великої літери
# print(S.title())