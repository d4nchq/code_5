#введення розміру масиву.
n = int(input("n = "))
print(f"Введіть {n} елементів масиву:")

#введення масиву користувачем.
arr = [float(input()) for _ in range(n)]

#виведення початкового масиву.
print("Початковий масив:", arr)

#знаходження мінімального від'ємного елемента.
negative_elements = [x for x in arr if x < 0]  #відфільтровуємо лише від'ємні елементи.

if negative_elements:  #перевірка, чи є від'ємні елементи в масиві.
    min_negative = min(negative_elements)
    print("Мінімальний від'ємний елемент:", min_negative)
else:
    print("В масиві немає від'ємних елементів.")
