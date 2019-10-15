sequences = []
for i in range(2):
    raw_items = input(f"Введите числа для списка {i+1} через разделитель (',' или '/' или ';'): ")
    divider = ','
    if ',' in raw_items:
        pass
    elif '/' in raw_items:
        divider = '/'
    elif ';' in raw_items:
        divider = ';'
    sequence = raw_items.split(divider)
    sequence = [int(item) if item.strip().replace('-', '').isnumeric() else None for item in sequence]
    sequence = list(filter(lambda item: item is not None, sequence))
    sequences.append(sequence)
sequence1, sequence2 = sequences[0], sequences[1]

sequence1 = list(filter(lambda item: item not in sequence2, sequence1)) 
print('Результат вычитания второго списка из первого: ', sequence1)