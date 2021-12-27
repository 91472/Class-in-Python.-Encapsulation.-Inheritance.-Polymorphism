# Урок: Основы объектно-ориентированного программирования. Принципы ООП.
# Задание Lite:
#1. Реализовать класс для карточный игры "Игра в дурака" в простейшем виде(без козырей, можно без "добора" карт и т.д.).
#2. Структура класса может быть на Ваше усмотрение.
#3. Можно реализовать следующие методы: инициализация игры (раздача карт себе и компьютеру), ход Ваш, ход компьютера.


# Выполнение задания Ultra Lite:
import random
import os
from time import sleep

class GameFool_v1:
    '''
    Дурак (карточная игра). Версия 1.0 – «Простой дурак» (без «переводного», без «подкидного», с козырями,
    раздача по 6 карт, колода 36 карт, с «добором» до 6 карт из колоды, только два игрока – компьютер и человек).
    Подробные правила к версии 1.0 - «Простой дурак»:
    В игре используется колода из 36 карт.
    Участвуют два игрока – компьютер и человек.
    Перед началом кона карты необходимо перетасовать (перемешать)
    Старшинство карт (от меньшего достоинства к большему): 6, 7, 8, 9, 10, В, Д, К, Т.
    Название мастей: Червы (черви), Бубны (буби), Трефы (крести), Пики.
    Начало игры:
    Каждому раздаётся по 6 карт, и следующая (13-я) из колоды карта открывается и её  масть устанавливает козырь
    для данной игры,  остальная колода кладётся сверху так, чтобы козырная карта была всем видна.
    Цель игры — избавиться от всех карт. Последний игрок, не избавившийся от карт, остаётся в «дураках».
    Отбитые карты идут в «отбой» («биту») и складываются на столе рубашкой вверх.
    Ход игры:
    Игру начинает тот, у кого выпало большее число на брошенной кости, в последующий кон первым начинает выигравший.
    Игроки скрывают свои карты от других игроков.
    В ходе игры заходящий игрок ходит любой из имеющихся у него картой, а отбивающийся игрок (игрок, под которого
    сделан заход) должен либо побить её, либо взять. Чтобы побить (покрыть) карту, нужно из имеющихся на руках карт
    положить на неё старшую карту той же масти, либо козыря, если битая карта не козырь. Если битая карта — козырь,
    то побить её можно только старшим козырем.
    После того, как сыгран заход, игроки по очереди добирают из оставшейся колоды карту до шести, при условии, если
    у них на руках меньше шести карт. Первым берёт недостающую карту (до шести) заходящий игрок, последним карту
    берет отбивавшийся игрок. После того, как сыгран заход, первым ходит тот, кто отбился, иначе заходящий игрок
    (если отбивающийся игрок не покрыл, «взял»).
    После того, как в колоде не осталось карт, игра продолжается оставшимися на руках картами по тем же правилам
    (за исключением добора карт из колоды) до тех пор, пока один из игроков не израсходует все свои карты.
    Оставшийся с картами игрок считается проигравшим (дураком).
    '''

    def __init__(self, game_quantity):
        self.game_N = game_quantity
        self.round_win_user = -1
        self.round_win_computer = -1
        self.counter_drawn_game = 0
        self.counter_win_computer = 0
        self.counter_win_user = 0
        self.move_win_user = -1
        self.move_win_computer = -1

    def __str__(self):
        return f'\nКарточная игра "Дурак" версия 1 (простейший вид), количество конов в игре {self.game_N}'

    def clear(self):
        print('\n' * 100)  # для "очистки" экрана терминала IDE PyCharm (имитация)
        def cls():
            os.system('cls||clear')  # для очистки экрана терминала ОС Windows, MAC, Linux (реальная очистка)
        cls()

    def timer(self):
        print('\n\nИдет раздача карт', end='')
        for i in range(7):
            sleep(1)
            print('.', end='')

    def print_cards(self):
        print('\rВаши карты (козырь - {}):'.format(self.trump))
        [print(i, ' ', self.cards_user[i]) for i in range(len(self.cards_user))]
        # print('Карты компьютера: ', self.cards_computer)

    def first_get_cards(self, who):
        if who == 'user':
            if len(self.cards_user) < 6 and len(self.cards_pack) > 0:
                dl = 6 - len(self.cards_user)
                if len(self.cards_pack) >= dl:
                    self.cards_user.extend(self.cards_pack[0:dl])
                    del self.cards_pack[:dl]
                else:
                    self.cards_user.extend(self.cards_pack[0:len(self.cards_pack)])
                    del self.cards_pack[:len(self.cards_pack)]
            if len(self.cards_computer) < 6 and len(self.cards_pack) > 0:
                dl = 6 - len(self.cards_computer)
                if len(self.cards_pack) >= dl:
                    self.cards_computer.extend(self.cards_pack[0:dl])
                    del self.cards_pack[:dl]
                else:
                    self.cards_computer.extend(self.cards_pack[0:len(self.cards_pack)])
                    del self.cards_pack[:len(self.cards_pack)]
        elif who == 'computer':
            if len(self.cards_computer) < 6 and len(self.cards_pack) > 0:
                dl = 6 - len(self.cards_computer)
                if len(self.cards_pack) >= dl:
                    self.cards_computer.extend(self.cards_pack[0:dl])
                    del self.cards_pack[:dl]
                else:
                    self.cards_computer.extend(self.cards_pack[0:len(self.cards_pack)])
                    del self.cards_pack[:len(self.cards_pack)]
            if len(self.cards_user) < 6 and len(self.cards_pack) > 0:
                dl = 6 - len(self.cards_user)
                if len(self.cards_pack) >= dl:
                    self.cards_user.extend(self.cards_pack[0:dl])
                    del self.cards_pack[:dl]
                else:
                    self.cards_user.extend(self.cards_pack[0:len(self.cards_pack)])
                    del self.cards_pack[:len(self.cards_pack)]
        if len(self.cards_pack) == 9 or len(self.cards_pack) == 8:
            print('\rВНИМАНИЕ! В колоде осталось менее 10 карт!')
        if len(self.cards_pack) == 0:
            print('\rВНИМАНИЕ! В колоде не осталось карт!')
        if len(self.cards_pack) == 0 and len(self.cards_computer) == 0 and len(self.cards_user) == 0:
            print('\rКон №{} завершен, ничья!'.format(self.counter_games))
            self.round_win_user = 1
            self.round_win_computer = 1
            self.counter_drawn_game += 1
        elif len(self.cards_pack) == 0 and len(self.cards_computer) == 0:
            print('\rКон №{} завершен, выиграл Компьютер!'.format(self.counter_games))
            self.round_win_user = 0
            self.round_win_computer = 1
            self.counter_win_computer += 1
        elif len(self.cards_pack) == 0 and len(self.cards_user) == 0:
            print('\rКон №{} завершен, Вы выиграли!'.format(self.counter_games))
            self.round_win_user = 1
            self.round_win_computer = 0
            self.counter_win_user += 1
        else:
            self.print_cards()

    def user_move(self):
        while True:
            num_card_user = int(input('\nВаш ход, введите номер вашей карты из списка: '))
            if num_card_user >= len(self.cards_user) or num_card_user < 0:
                print('\nНеверный ход, попробуйте еще раз!')
            else:
                break
        print('\nВы сходили: ', self.cards_user[num_card_user])
        temp_1 = []
        temp_2 = []
        for num_card_computer in range(len(self.cards_computer)):
            if self.cards_computer[num_card_computer][0] == self.cards_user[num_card_user][0] and self.seniority_cards.index(self.cards_computer[num_card_computer][1]) > self.seniority_cards.index(self.cards_user[num_card_user][1]):
                temp_1.append(num_card_computer)
            elif self.cards_computer[num_card_computer][0] != self.cards_user[num_card_user][0] and \
                    self.cards_computer[num_card_computer][0] == self.trump[0]:
                temp_2.append(num_card_computer)
        if len(temp_1) != 0:
            min_index = min([self.seniority_cards.index(self.cards_computer[i][1]) for i in temp_1])
            for i in temp_1:
                if self.cards_computer[i][1] == self.seniority_cards[min_index]:
                    num_card_computer = i
            print('\nКомпьютер сходил: ', self.cards_computer[num_card_computer], '\nБито!  ', end='')
            self.timer() if len(self.cards_pack) > 0 else sleep(3)
            self.clear()
            del self.cards_computer[num_card_computer]
            del self.cards_user[num_card_user]
            self.move_win_user = 0
            self.move_win_computer = 1
            self.first_get_cards('user')
        elif len(temp_2) != 0:
            min_index = min([self.seniority_cards.index(self.cards_computer[i][1]) for i in temp_2])
            for i in temp_2:
                if self.cards_computer[i][1] == self.seniority_cards[min_index]:
                    num_card_computer = i
            print('\nКомпьютер сходил: ', self.cards_computer[num_card_computer], '\nБито!  ', end='')
            self.timer() if len(self.cards_pack) > 0 else sleep(3)
            self.clear()
            del self.cards_computer[num_card_computer]
            del self.cards_user[num_card_user]
            self.move_win_user = 0
            self.move_win_computer = 1
            self.first_get_cards('user')
        else:
            self.cards_computer.append(self.cards_user[num_card_user])
            del self.cards_user[num_card_user]
            print('\nКомпьютер не покрыл (взял)!  ', end='')
            self.timer() if len(self.cards_pack) > 0 else sleep(3)
            self.clear()
            self.move_win_user = 1
            self.move_win_computer = 0
            self.first_get_cards('user')

    def computer_move(self):
        num_card_computer = random.randint(0, len(self.cards_computer) - 1)
        print('\nКомпьютер сходил: ', self.cards_computer[num_card_computer])
        while True:
            num_card_user = int(input('\nВаш ход, введите номер вашей карты чтобы покрыть или введите 99 чтобы взять: '))
            if num_card_user == 99:
                print('\nВы не покрыли (взяли)!  ', end='')
                self.timer() if len(self.cards_pack) > 0 else sleep(3)
                self.clear()
                self.cards_user.append(self.cards_computer[num_card_computer])
                del self.cards_computer[num_card_computer]
                self.move_win_user = 0
                self.move_win_computer = 1
                self.first_get_cards('computer')
                break
            elif num_card_user >= len(self.cards_user) or num_card_user < 0:
                print('\nНеверный ход, попробуйте еще раз!')
            elif (self.cards_user[num_card_user][0] == self.cards_computer[num_card_computer][0] and self.seniority_cards.index(self.cards_user[num_card_user][1]) > self.seniority_cards.index(self.cards_computer[num_card_computer][1])) or (self.cards_user[num_card_user][0] != self.cards_computer[num_card_computer][0] and self.cards_user[num_card_user][0] == self.trump[0]):
                del self.cards_computer[num_card_computer]
                print('\nВы сходили: ', self.cards_user[num_card_user])
                del self.cards_user[num_card_user]
                self.move_win_user = 1
                self.move_win_computer = 0
                print('\nБито!  ', end = '')
                self.timer() if len(self.cards_pack) > 0 else sleep(3)
                self.clear()
                self.first_get_cards('computer')
                break
            else:
                print('\nНеверный ход, попробуйте еще раз!')

    def play_cards(self):  # ход игры
        self.seniority_cards = [6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз']
        for self.counter_games in range(1, self.game_N+1):
            self.cards_pack = [('Черви', 6), ('Черви', 7), ('Черви', 8), ('Черви', 9), ('Черви', 10), ('Черви', 'Валет'),
                          ('Черви', 'Дама'), ('Черви', 'Король'), ('Черви', 'Туз'),
                          ('Буби', 6), ('Буби', 7), ('Буби', 8), ('Буби', 9), ('Буби', 10), ('Буби', 'Валет'),
                          ('Буби', 'Дама'), ('Буби', 'Король'), ('Буби', 'Туз'),
                          ('Крести', 6), ('Крести', 7), ('Крести', 8), ('Крести', 9), ('Крести', 10),
                          ('Крести', 'Валет'), ('Крести', 'Дама'), ('Крести', 'Король'), ('Крести', 'Туз'),
                          ('Пики', 6), ('Пики', 7), ('Пики', 8), ('Пики', 9), ('Пики', 10), ('Пики', 'Валет'),
                          ('Пики', 'Дама'), ('Пики', 'Король'), ('Пики', 'Туз')
                          ]  # создание колоды из 36 карт в виде списка
            print('*'*60, '\nНачало игры, кон №{}, перетасовка карт в колоде завершена.\n'.format(self.counter_games), '*'*60, sep='')
            random.shuffle(self.cards_pack)  # перетасовка колоды перед началом каждого кона
            #print(self.cards_pack)
            print('Первая раздача карт: 6 карт компьютеру и 6 карт вам, 13-ая карта - козырь, кладем под оставшуюся колоду.')
            self.cards_user = self.cards_pack[0:6]
            del self.cards_pack[0:6]
            self.cards_computer = self.cards_pack[0:6]
            del self.cards_pack[0:6]
            self.trump = self.cards_pack[0]
            self.cards_pack.append(self.cards_pack[0])
            del self.cards_pack[0]

            self.print_cards()

            def dice():
                dice_computer = 0
                dice_user = 0
                while dice_user == dice_computer:
                    dice_user = random.choice(range(1, 7))
                    dice_computer = random.choice(range(1, 7))
                    print('Компьютер бросил кость и выпало число: ', dice_computer)
                    print('Вы бросили кость и выпало число: ', dice_user)
                    print('У вас выпало больше, вы ходите первым!' if dice_user > dice_computer else 'У компьютера выпало больше, он ходит первым!' if dice_user < dice_computer else 'Бросайте снова!')
                return dice_user, dice_computer

            if self.counter_games == 1 or (self.round_win_user == 1 and self.round_win_computer == 1):
                dice_user, dice_computer = dice()
                if dice_user > dice_computer:  # ход игрока
                    self.user_move()
                elif dice_user < dice_computer: # ход компьютера
                    self.computer_move()
            elif self.round_win_user == 1 and self.round_win_computer == 0:
                self.user_move()
            elif self.round_win_user == 0 and self.round_win_computer == 1:
                self.computer_move()

            while len(self.cards_pack) != 0 or (len(self.cards_computer) != 0 and len(self.cards_user) != 0):
                if self.move_win_user == 1 and self.move_win_computer == 0:
                    self.user_move()
                elif self.move_win_user == 0 and self.move_win_computer == 1:
                    self.computer_move()
            print('\rОсталось карт в колоде: ', len(self.cards_pack), '   Осталось карт у Вас: ', len(self.cards_user), '   Осталось карт у Компьютера: ', len(self.cards_computer))

        print('\rВсего сыграно {} раз, из них {} ничья, {} выиграли Вы, {} выиграл Компьютер'.format(self.game_N, self.counter_drawn_game, self.counter_win_user, self.counter_win_computer))
        if self.counter_win_computer < self.counter_win_user:
            print('\rВ общем зачете победили Вы!')
        elif self.counter_win_computer > self.counter_win_user:
            print('\rВ общем зачете победил Компьютер!')
        elif self.counter_win_computer == self.counter_win_user:
            print('\rВ общем зачете Ничья!')


if __name__ == '__main__':
    game = GameFool_v1(2)
    print(game)
    game.play_cards()
