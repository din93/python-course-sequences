sequence = []

sequence_length = input("Введите количество элементов ")
while not sequence_length.isdecimal():
    sequence_length = input("Введите количество элементов ")
    
for i in range(int(sequence_length)):
    number_to_add = input(f"Теперь введите {i+1}-е число ")
    while not number_to_add.strip().replace('-', '').isnumeric():
        number_to_add = input(f"Теперь введите {i+1}-е число ")
    sequence.append(int(number_to_add))

sequence.sort()
print(f'Список введенных вами чисел в порядке возрастания ', sequence)