def age_valid(i):
    while True:
        age = input(f'Введите возраст посетителя для {i}го билета -')
        if age.isdigit() == True and 0 < int(age) <= 100:
            break
        else:
            print('Неверный ввод')
    return int(age)


while True:
    n = input('Введите количество билетов, но не боллее 1000 шт.- ')
    if n.isdigit() == True and (0 < int(n) <= 1000):
        break
    else:
        print('Неверный ввод')
age_list = []
for j in range(1, int(n) + 1):
    age_list.append(age_valid(j))

price_list = []
for age in age_list:
    if age < 18:
        price_list.append(0)
    elif 18 <= age < 25:
        price_list.append(990)
    else:
        price_list.append(1390)

prise = sum(price_list)
print(f'Общая стоимость за {n} билет{"" if int(n[-1]) == 1 else ("a" if 2 <= int(n[-1]) <= 4 else "ов")} составляет {prise} руб.')
if int(n) > 3:
    print(f'С учетом скидки итоговая стоимость {round(prise * 0.9)} руб.')


