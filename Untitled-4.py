print("=== Запись текста в новый файл ===")
user_text = input("Введите текст для записи в файл: ")

with open('user_input.txt', 'w', encoding='utf-8') as file:
    file.write(user_text)
print("Текст успешно записан в файл 'user_input.txt'")

print("\n=== Добавление текста в файл ===")
additional_text = input("Введите текст для добавления в файл: ")

with open('user_input.txt', 'a', encoding='utf-8') as file:
    file.write('\n' + additional_text)
print("Текст успешно добавлен в файл!")

print("\n=== Итоговое содержимое файла ===")
with open('user_input.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
