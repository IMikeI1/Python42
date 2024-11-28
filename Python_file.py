import os
import shutil

# функция open (file, mode, encoding) - открывает файл
# file - путь к файлу (абсолютный или относительный скрипта)
# mode - режим открытия файла
# encoding - кодировка

# основные режимы: r - чтение, w - запись пересозданием файла, а - добавление в конец файла

myfile = open(file='myfile.txt', mode='w', encoding='utf-8')
print(type(myfile))
# write - запись в файла
myfile.write("Phyton\n")
my_list = ['alena', 'elena']
for item in my_list:
    myfile.write(item.strip(',! ')+'\n')
text = "Forever!!!"
myfile.write(text)
# после завершения работы файла
myfile.close()
# открытие файла в режими добовления в конец файла
myfile = open(file='myfile.txt', mode='a', encoding='utf-8')
myfile.write("Phyton\n")
myfile.close()
открытие файла
myfile = open(file='myfile.txt', mode='r', encoding='utf-8')
text_from_file = myfile.read()
print(text_from_file)
text_rows = text_from_file.split('\n')
print(text_rows)
myfile.seek(0)
text_lines = myfile.readline()
print(text_lines[0], text_lines[1])

mylist = ['alex', 'ivanov']
print(*mylist, sep='\n')


file_name = 'myfilenem.txt'
if os.path.exists(file_name):

  with open(file=file_name, mode='r', encoding='utf-8') as my_file:
    text_from_f = my_file.read()
else:
    with open(file=file_name, mode='w', encoding='utf-8') as my_file:
        text_from_f = my_file.read()
        pass
# rename file
filename_new = f"new_{file_name}"
if os.path.exists(file_name):
    if not os.path.exists(filename_new):
    os.rename(file_name, filename_new)
    print(f'Файл {file_name} --> {filename_new} '  )
else:
    print(f'Файл{filename_new} удален!' )

dir_name = 'files'
if not os.path.exists(dir_name):
    os.makedirs(dir_name, exist_ok=)





