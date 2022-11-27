from random import choice


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


def bi_search(a, array):
    left, right = 0, len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle] < a:
            left = middle + 1
        else:
            right = middle
    return left


def check_input():
    while True:
        flag = True
        str1 = input('Введите строку чисел (не повторяющихся) разделенных пробелами: ').split()

        for c in str1:                      # проверка что это числа
            if c.lstrip('-').isdigit() == False:
                flag = False
                print("Не удовлетворяет условию ввода: неверные символы")
                break

        if len(set(str1)) != len(str1):      # проверка что нет повторений
            flag = False
            print("Не удовлетворяет условию ввода: есть повторы чисел")

        if flag == False:
            continue
        break
    return str1


array = [int(i) for i in check_input()]
array = quicksort(array)
while True:
    num = input('Введите число: ').strip()
    if num.lstrip('-').isdigit() == False:
        print('Ввод не соответствует условию')
        continue
    num = int(num)
    break

if num > array[-1] or num < array[0]:
    print('Число выходит за пределы массива')
else:
    ind = bi_search(num, array)-1
    print('Номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу: ',
          ind, ', это число:', array[ind])

