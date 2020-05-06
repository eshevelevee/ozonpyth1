def count_words(filename):

    try:
        file = open(filename, encoding='utf-8')
        content = file.read()
    except FileNotFoundError:
        pass
    else:
        words = content.split()
        num_words = len(words)
        print(f"В файле {filename} около {num_words} слов")

filenames = ['expen', 'expenses_analysis_fileswork.py', "exp1"]
for filename in filenames:
    count_words(filename)