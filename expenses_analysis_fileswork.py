file_finances_input = str(input("Введите название файла с тратами: "))
with open(file_finances_input, 'r') as file:
    expenses_list_temp = file.read().rstrip().split('\n')
    expenses_list = [float(e) for e in expenses_list_temp]  # переводим элементы листа в флоат

# считаем данные для отчета и формируем строки для записи в файл
report_total = ("Всего вы совершили " + str(len(expenses_list)) + " покупок.\n")
report_sum = ("Всего вы потратили " + str(sum(expenses_list)) + '\n')
report_avg = ("В среднем одна покупка " + str(sum(expenses_list) / len(expenses_list)) + '\n')
report_max = ("Самая крупная покупка " + str(max(expenses_list)) + '\n')

with open('expenses_analysis.txt', 'w') as file:
    file.write(report_total)
    file.write(report_sum)
    file.write(report_avg)
    file.write(report_max)
