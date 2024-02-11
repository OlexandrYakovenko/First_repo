import time as T

# Отримуємо поточну дату і час у вигляді часової мітки
# seconds = T.time()
# print("Seconds since epoch =", seconds)

# Конвертуємо часову мітку в читабельний формат
# seconds = 1672215379.5045543
# local_time = T.ctime(seconds)
# print("Local time:", local_time)


# #Метод time.sleep() призупиняє виконання поточного потоку коду
# print("\nPrinted immediately.")
# T.sleep(2.4)
# print("Printed after 2.4 seconds.")

# i=0
# for c in "HELLO":
#         print(i*' '+c)
#         i+=1
#         T.sleep(.5)


#Метод time.localtime() приймає часову мітку та повертає struct_time 
# (кортеж, який містить 9 елементів) за локальним часом.
# time=T.time()
# result = T.localtime(time)
# print("\nresult:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)

# #Метод time.gmtime() в якості аргументу приймає часову мітку, і повертає кортеж
# # struct_time по формату UTC.
# result = T.gmtime(time)
# print("\nresult:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)

# Метод time.mktime() приймає в якості аргументу struct_time (кортеж, який містить 9 елементів)
#  і повертає часову мітку.
# (рік, місяць, день, година, хвилини, секунди, тиждень, день року, літній час)
# time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
# seconds = T.mktime(time_tuple)
# print(seconds)

# Метод time.asctime() приймає в якості аргументу кортеж struct_time, і повертає рядок, що його 
# представляє.
# (рік, місяць, день, година, хвилини, секунди, тиждень, день року, літній час)
# t = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
# result = T.asctime(t)
# print("Result:", result)

#Метод time.strftime() приймає в якості аргументу кортеж struct_time і повертає рядок, що його
# представляє, на основі використовуваного коду формату.
# named_tuple = T.localtime() # отримуємо struct_time
# print(named_tuple)
# time_string = T.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
# print(time_string)

# Метод time.strptime() приймає рядок, що представляє час, та повертає struct_time.
# time_string = "14 July, 2023"
# result = T.strptime(time_string, "%d %B, %Y")
# print(result)