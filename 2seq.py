raw_items = input("Введите числа через разделитель (',' или '/' или ';'): ")

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
sequence = set(sequence)

print('Введенные вами числа без повторений: ', sequence)