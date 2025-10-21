def twoSum(nums, target):
    # Создаем словарь для хранения ранее встреченных чисел и их индексов
    num_to_index = {}

    # Проходим по массиву nums
    for index, num in enumerate(nums):
        # Вычисляем число, которое нужно найти, чтобы сумма дала target
        complement = target - num

        # Если оно уже есть в словаре — решение найдено
        if complement in num_to_index:
            return [num_to_index[complement], index]

        # Если нет — сохраняем текущий элемент в словарь
        num_to_index[num] = index


print(twoSum([2, 7, 11, 15], 9))     # [0, 1]
print(twoSum([3, 2, 4], 6))          # [1, 2]
print(twoSum([3, 3], 6))             # [0, 1]

