heigth = int(input('Укажите ваш рост (см): '))
age = int(input('Укажите ваш возраст: '))
children = int(input('Сколько у вас детей: '))
education = input('Учитесь ли вы сейчас (да,нет): ')

if age < 18 or children >=3 or education == 'да':
    print('Отсрочка от службы')

else:
    if heigth <= 170:
        print('Танковые войска')
    elif heigth <= 185:
        print('Военно-воздушные силы')
    else:
        print('Военно-морские силы')
