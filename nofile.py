file_path = '1.txt'
try:
    file=open(file_path)
except FileNotFoundError:
    print("Что за херня, нет такого файла!")