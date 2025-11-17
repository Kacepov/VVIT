def describe_person(name, age=30):
    print(f"Имя: {name}, Возраст: {age} лет")

describe_person("Анна")
describe_person("Иван", 25)# Передается конкретный возраст
describe_person("Мария", age=35)# Явное указание аргумента

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(7))
print(is_prime(10))
print(is_prime(17))
print(is_prime(1))
print(is_prime(2))

print("Простые числа от 1 до 20:")
for num in range(1, 21):
    if is_prime(num):
        print(num, end=" ")