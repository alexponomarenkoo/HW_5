####Task1
# У списку цілих, заповненому випадковими числами обчислити:
# ■ Суму негативних чисел;
# ■ Суму парних чисел;
# ■ Суму непарних чисел;
# ■ Добуток елементів з кратними індексами 3;
# ■ Добуток елементів між мінімальним та максимальним елементом;
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.

# import random
# numbers = [random.randint(-100, 100) for _ in range(10)]
# print("Вихідний список:", numbers)
# sum_negative = sum(x for x in numbers if x < 0)
# print("Сума від'ємних чисел:", sum_negative)
# sum_even = sum(x for x in numbers if x % 2 == 0)
# sum_odd = sum(x for x in numbers if x % 2 != 0)
# print("Сума парних чисел:", sum_even)
# print("Сума непарних чисел:", sum_odd)
# product_indices_3 = 1
# for i, num in enumerate(numbers):
#     if i % 3 == 0:
#         product_indices_3 *= num
# print("Добуток елементів з кратними індексами 3:", product_indices_3)
# min_index, max_index = numbers.index(min(numbers)), numbers.index(max(numbers))
# product_min_max = 1
# for num in numbers[min(min_index, max_index) + 1 : max(min_index, max_index)]:
#     product_min_max *= num
# print("Добуток елементів між мінімальним та максимальним елементом:", product_min_max)
# pos_indices = [i for i, x in enumerate(numbers) if x > 0]
# sum_between_positives = sum(numbers[pos_indices[0] + 1 : pos_indices[-1]])
# print("Сума елементів між першим та останнім позитивними елементами:", sum_between_positives)


####Task2
# Є список цілих, заповнений випадковими числами.
# На підставі даних цього масиву потрібно:
# ■ Створити список цілих, що містить лише парні числа з першого списку;
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.
# import random
# numbers = [random.randint(-100, 100) for _ in range(10)]
# print("Вихідний список:", numbers)
# even_numbers = [x for x in numbers if x % 2 == 0]
# odd_numbers = [x for x in numbers if x % 2 != 0]
# negative_numbers = [x for x in numbers if x < 0]
# positive_numbers = [x for x in numbers if x > 0]
# print("Список парних чисел:", even_numbers)
# print("Список непарних чисел:", odd_numbers)
# print("Список негативних чисел:", negative_numbers)
# print("Список позитивних чисел:", positive_numbers)
