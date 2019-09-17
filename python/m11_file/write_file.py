with open('lang.txt', 'w') as f:
    f.write('Python\n')
    f.write('C\n')
    f.write('Java\n')

with open('lang.txt', 'a', encoding='utf-8') as f:
    f.write('C++\n')
    f.write('JavaScript\n')
    f.write('梅西\n')