def read_file_simple(filename='example.txt', read_type='all'):
    """
    Простая функция для чтения файла
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            if read_type == 'all':
                content = file.read()
                print("Содержимое файла:")
                print(content)
            elif read_type == 'line':
                print("Содержимое файла (построчно):")
                for line in file:
                    print(line.rstrip())
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write("Допустим первая строчка\n")
    f.write("Ну написал вторую\n")
    f.write("Ну еще одну\n")
    f.write("А вот и последняя строчка)\n")

print("=== Чтение всего файла ===")
read_file_simple('example.txt', 'all')

print("\n=== Построчное чтение ===")
read_file_simple('example.txt', 'line')