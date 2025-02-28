from random import randint

# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Генерирует количество очков атаки."""
    warrior_point = randint(8, 10)
    mage_point = randint(8, 15)
    healer_point = randint(2, 4)
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный {warrior_point}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный {mage_point}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику равный {healer_point}')
    return (f'{char_name} не применил специальное умение')


def defence(char_name: str, char_class: str) -> str:
    """Генерирует количество очков защиты."""
    warrior_damage = randint(15, 20)
    mage_damage = randint(8, 12)
    healer_damage = randint(12, 15)
    if char_class == 'warrior':
        return (f'{char_name} блокировал {warrior_damage} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {mage_damage} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {healer_damage} урона')
    return (f'{char_name} не применил специальное умение')


def special(char_name: str, char_class: str) -> str:
    """Возвращает сообщение о применении специального умения."""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение'
                f' «Выносливость {105}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {45}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {40}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name: str, char_class: str) -> str:
    """Запускает цикл тренировки навыков персонажа."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(f'{char_name} введи одну из команд: attack — чтобы '
          'атаковать противника, defence — чтобы '
          'блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Позволяет игроку выбрать тип игрового персонажа."""
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, за которого '
            'хочешь играть: Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print(
                'Воитель — дерзкий воин ближнего боя. '
                'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print(
                'Маг — находчивый воин дальнего боя. '
                'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print(
                'Лекарь — могущественный заклинатель. '
                'Черпает силы из природы, веры и духов.')
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, или любую '
            'другую кнопку, чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    """Главная функция. Она запускает игру."""
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
