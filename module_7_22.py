def custom_write(file_name, strings):
    strings_positions = {}

    file_name = file_name
    file = open(file_name, "a",encoding= "utf-8")
    for i in range(len(strings)):
        a2 = (str(file.tell()))


        file.write(strings[i] + "/n")


        a1 = (str(i+1))
        a= (a1, a2)
        strings_positions[a] = strings[i]

    file.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)