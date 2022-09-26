def open_file():
    with open('data.txt', 'r', encoding='utf8') as file:
        cook_book = {}
        for line in file:
            line = line.strip()
            cook_book.update({line: []})
            k = int(file.readline().strip())
            for _ in range(k):
                lst = file.readline().strip().split(' | ')
                dict = {'ingredient_name': lst[0], 'quantity': lst[1], 'measure': lst[2]}
                cook_book[line].append(dict)
            file.readline()
    return cook_book



def view_cook_book():
    for key, value in open_file().items():
        print(f'\n {key}')
        for dct in value:
            print(f"    {dct['ingredient_name'] + ' - ' + dct['quantity'] + ' ' + dct['measure']}")



def view_shopping_list(s_l):
    print('\nДля приготовления этих блюд пондобится:\n')
    index = 1
    for key, values in s_l.items():
        print(f"   {index}. {key} {values['quantity']} {values['measure']}")
        index += 1
    print('\n  Что-то из этого перечня можно будет найти на кухне, а остальное придется купить в магазине)))\n')

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for ingred in dishes:
        for ingr in open_file()[ingred]:
        # for ingr in cook_book[ingred]:
            name_ingr = ingr.pop('ingredient_name')
            ingr['quantity'] = int(ingr['quantity']) * int(person_count)
            if name_ingr in shopping_list:
                ingr['quantity'] += shopping_list[name_ingr]['quantity']
            shopping_list.update({name_ingr: ingr})
    view_shopping_list(shopping_list)



def input_ingredients():
    try:
        lst = list(input('Введите через запятую желаемые блюда: ').split(', '))
        persons = int(input('Введите количество персон: '))
        get_shop_list_by_dishes(lst, persons)
    except Exception:
        print('Кажется Вы где-то ошиблись с вводом. Перепроверьте и введите заново, но без ошибок')




def very_main():
    print('\n\nДобро пожаловать в список рецептов!'.upper())
    print('\n\nВам необходимо ввести номер действия, чтобы программа выполнила нужное действие: '
          '\n\n   1. Вывод рецептов.'
          '\n   2. Ввод нужных рецептов и количества человек. Программа вернет список необходимых ингредиентов.'
          '\n   9. Вывод этой справки.')
    while True:
        prog = str(input('\n=========================================================================================='
                         '\n\n  номер действия: '.upper()))
        if prog == '1':
            view_cook_book()
        elif prog == '2':
            input_ingredients()
        elif prog == '9':
            print('\n\nВам необходимо ввести номер действия, чтобы программа выполнила нужное действие: '
                  '\n\n   1. Вывод рецептов.'
                  '\n   2. Ввод нужных рецептов и количества человек. Программа вернет список необходимых ингредиентов.'
                  '\n   9. Вывод этой справки.'
                  '\n   0. Выйти из программы.')
        elif prog == '0':
            print('\n   Досвидания!'.upper())
            break

if __name__ == '__main__':
    very_main()