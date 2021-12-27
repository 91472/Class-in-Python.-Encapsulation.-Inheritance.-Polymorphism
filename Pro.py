# Урок: Основы объектно-ориентированного программирования. Принципы ООП.
# Задание Pro:
# 1. Выполнить задание уровня light
# 2. Реализовать класс для карточный игры "Игра в дурака" как можно ближе к
# правилам (можно реализовать класс на Ваш выбор, в котором будет представлен
# пройденный на уроке функционал).

# Выполнение задания Lite:
# 1. Выполнить задание уровня light, выполнено:
from Lite import GameFool_v1
import random
import os
from time import sleep


# 2. Реализовать класс для карточный игры "Игра в дурака" как можно ближе к
# правилам (можно реализовать класс на Ваш выбор, в котором будет представлен
# пройденный на уроке функционал).

# Создадим класс GameFool_v2, унаследованный от класса GameFool_v1,
# добавим в новом классе выбор одного из двух подвидов игр:
# - подкидной дурак (thrown_up)
# - переводной дурак (transferable)

class GameFool_v2(GameFool_v1):
    '''
    Дурак (карточная игра). Версия 2.0 – с выбором типа игры ("переводной дурак" (transferable) или "подкидной дурак" (thrown_up),
    с козырями, раздача по 6 карт, колода 36 карт, с «добором» до 6 карт из колоды, только два игрока – компьютер и человек).
    Подробные правила к версии 2.0:
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
    Тип игры "Подкидной дурак" (thrown_up):
    После того, как первая карта покрыта второй игрок (компьютер или человек) могут подкидывать карту равную по старшинству
    одной из имеющихся (вскрытых) "на столе" карте и т.д. каждый раз подкидывая по 1ой карте после покрытия предыдущей
    (до 6 карт, т.е. отбой не более 6 карт или меньше, если не осталось карт на руках). Если нет возможности больше
    подкидывать, то Бито. Если игрок не смог покрыть хотябы одну из кодкинутых к нему карт, то он забирает все.
    Подкидывать сразу несколько карт запрещено, ходить сразу несколькими картами запрещено,
    "докидывать" после того как игрок принял решение "Взять" - запрещено, переводить запрещено.
    Тип игры "Переводной дурак" (transferable):
    После того, как совершен первых ход одним из игроков, второй может перевести одну карту равным достоинством,
    и т.д. по очереди переводить друг другу до 4-х карт (макс.число карт в колоде из 36 карт с одинаковыми достоинствами).
    После того, как принимающий игрок не может перевести он должен либо покрыть все имеющиеся карты, либо взять их.
    Подкидывание запрещено, переводить сразу несколько карт запрещено. Для покрытия игроком-человеком одиночной карты
    специально усложнена комбинация ввода хода на случай, если нужно будет не перевести карту одинакового достоиснтава,
    а покрыть ей (в случае с козырем).
        После того, как сыгран заход, игроки по очереди добирают из оставшейся колоды карту до шести, при условии, если
    у них на руках меньше шести карт. Первым берёт недостающую карту (до шести) заходящий игрок, последним карту
    берет отбивавшийся игрок. После того, как сыгран заход, первым ходит тот, кто отбился, иначе заходящий игрок
    (если отбивающийся игрок не покрыл, «взял»).
    После того, как в колоде не осталось карт, игра продолжается оставшимися на руках картами по тем же правилам
    (за исключением добора карт из колоды) до тех пор, пока один из игроков не израсходует все свои карты.
    Оставшийся с картами игрок считается проигравшим (дураком).
    '''
    def __init__(self, game_quantity, type):
        super().__init__(game_quantity)
        self.type = type  # thrown_up or transferable

    def __str__(self):
        return f'\nКарточная игра "Дурак" версия 2: Тип игры - {self.type}, Количество конов в игре {self.game_N}'

    def print_cards_hand(self, temp_cards_user_l):
        print('\nСейчас на руках у Вас остались карты (козырь - {}):'.format(self.trump))
        [print(i, ' ', self.cards_user[i] if self.cards_user[i] not in temp_cards_user_l else '(..............)') for i in range(len(self.cards_user))]

    def user_input(self):
        while True:
            num_card_user_str = input('\nВаш ход!\nДля перевода введите номер вашей карты из списка.\nЧтобы покрыть несколько карт введите номера ваших карт из списка через запятую, без пробелов (пример формата ввода: 2,0,7,1).\nЧтобы покрыть одиночную карту введите номер вашей карты из списка и через запятую введите 99, без пробелов (пример формата ввода: 2,99).\nЧтобы взять введите 88\n')
            self.num_card_user = int(num_card_user_str.split(',')[0]) if len(num_card_user_str.split(',')) == 1 else [int(i) for i in num_card_user_str.split(',')]
            if self.num_card_user == 88:
                print('\nВы не покрыли (взяли)!')
                self.timer() if len(self.cards_pack) > 0 else sleep(3)
                self.clear()
                self.cards_user.extend(self.temp_cards_computer_l)
                [self.cards_computer.remove(i) for i in self.temp_cards_computer_l]
                self.move_win_user = 0
                self.move_win_computer = 1
                self.first_get_cards('computer')
                break
            elif isinstance(self.num_card_user, int) and (self.num_card_user < len(self.cards_user)) and (self.num_card_user >= 0) and (self.cards_user[self.num_card_user] not in self.temp_cards_user_l) and (self.cards_user[self.num_card_user][1] == self.temp_cards_computer_l[-1][1]):
                if (len(self.cards_computer) - len(self.temp_cards_computer_l)) >= len(self.temp_cards_user + self.temp_cards_computer)+1:
                    self.temp_cards_user.append(self.num_card_user)
                    self.temp_cards_user_l = [self.cards_user[self.num_card_user] for self.num_card_user in self.temp_cards_user]
                    print(f'\nВы сходили:       {self.temp_cards_user_l[-1]}' if len(self.temp_cards_user_l + self.temp_cards_computer) == 1 else f'\nВы перевели:       {self.temp_cards_user_l[-1]}')
                    break
                else:
                    print('\nУ Компьютера осталось карт меньше, чем вы хотите перевести! Покройте или возьмите!')
            elif isinstance(self.num_card_user, list) and all(
                    [(i < len(self.cards_user) and i >= 0) for i in self.num_card_user]) and all(
                    [self.cards_user[i] not in self.temp_cards_user_l for i in self.num_card_user]) and len(self.num_card_user) == len(
                    set(self.num_card_user)) and len(self.num_card_user) == len(self.temp_cards_user_l + self.temp_cards_computer_l):
                all_cards = self.temp_cards_user_l + self.temp_cards_computer_l
                count = 99
                for x, i in enumerate(self.num_card_user):
                    for j in all_cards:
                        if (self.cards_user[i][0] == j[0] and self.seniority_cards.index(
                                self.cards_user[i][1]) > self.seniority_cards.index(j[1])) or (
                                self.cards_user[i][0] != j[0] and self.cards_user[i][0] == self.trump[0]):
                            count = x
                if len(self.num_card_user) != count + 1:
                    print('\nНеверный ввод, попробуйте еще раз!')
                elif len(self.num_card_user) == count + 1:
                    print(f'\nНеобходимо было покрыть: {all_cards}\nВы сходили:            {[self.cards_user[i] for i in self.num_card_user]}')
                    print('\nБито!')
                    self.timer() if len(self.cards_pack) > 0 else sleep(3)
                    self.clear()
                    [self.cards_computer.remove(i) for i in self.temp_cards_computer_l]
                    [self.cards_user.remove(i) for i in (self.temp_cards_user_l + [self.cards_user[i] for i in self.num_card_user])]
                    self.move_win_user = 1
                    self.move_win_computer = 0
                    self.first_get_cards('computer')
                    self.num_card_user = 88
                    break

            elif (isinstance(self.num_card_user, list) and len(self.num_card_user) == 2) and ((self.num_card_user[0] < len(self.cards_user) and self.num_card_user[0] >= 0) or (self.num_card_user[1] < len(self.cards_user) and self.num_card_user[1] >= 0)) and (self.num_card_user[0] == 99 or self.num_card_user[1] == 99) and len(self.temp_cards_user_l + self.temp_cards_computer_l) == 1:
                all_cards = self.temp_cards_user_l + self.temp_cards_computer_l
                i = self.num_card_user[0] if self.num_card_user[0] < self.num_card_user[1] else self.num_card_user[1]
                if (self.cards_user[i][0] == all_cards[0][0] and self.seniority_cards.index(self.cards_user[i][1]) > self.seniority_cards.index(all_cards[0][1])) or (self.cards_user[i][0] != all_cards[0][0] and self.cards_user[i][0] == self.trump[0]):
                    print(f'\nВы сходили:     {self.cards_user[i]}\nБито!')
                    self.timer() if len(self.cards_pack) > 0 else sleep(3)
                    self.clear()
                    self.cards_computer.remove(self.temp_cards_computer_l[0])
                    self.cards_user.remove(self.cards_user[i])
                    self.move_win_user = 1
                    self.move_win_computer = 0
                    self.first_get_cards('computer')
                    self.num_card_user = 88
                    break
                else:
                    print('\nНеверный ввод, попробуйте еще раз!')
            else:
                print('\nНеверный ввод, попробуйте еще раз!')

    def computer_input(self):
        for num_card_computer in range(len(self.cards_computer)):
            if (num_card_computer not in self.temp_cards_computer) and (self.cards_computer[num_card_computer][1] == self.temp_cards_user_l[-1][1]) and ((len(self.cards_user) - len(self.temp_cards_user_l)) >= len(self.temp_cards_computer + self.temp_cards_user)+1):
                self.temp_cards_computer.append(num_card_computer)
                self.temp_cards_computer_l = [self.cards_computer[num_card_computer] for num_card_computer in self.temp_cards_computer]
                print('\nКомпьютер перевел Вам: ', self.temp_cards_computer_l[-1], f'\n\nПереведите, покройте или возьмите: {self.temp_cards_user_l + self.temp_cards_computer_l}' if len(self.temp_cards_user_l + self.temp_cards_computer_l) < 4 else f'\n\nПокройте или возьмите: {self.temp_cards_user_l + self.temp_cards_computer_l}')
                self.print_cards_hand(self.temp_cards_user_l)
                self.user_input()
                break

            elif num_card_computer == len(self.cards_computer) - 1:
                self.temp_cards_computer_l = [self.cards_computer[num_card_computer] for num_card_computer in self.temp_cards_computer]
                all_cards = self.temp_cards_user_l + self.temp_cards_computer_l
                temp_cards_computer_l1 = []
                for j in all_cards:
                    temp_1 = []
                    temp_2 = []
                    for num_card_computer in range(len(self.cards_computer)):
                        if num_card_computer not in self.temp_cards_computer:
                            if self.cards_computer[num_card_computer][0] == j[0] and self.seniority_cards.index(
                                    self.cards_computer[num_card_computer][1]) > self.seniority_cards.index(j[1]):
                                temp_1.append(num_card_computer)
                            elif self.cards_computer[num_card_computer][0] != j[0] and \
                                    self.cards_computer[num_card_computer][0] == self.trump[0]:
                                temp_2.append(num_card_computer)
                    if len(temp_1) != 0:
                        min_index = min([self.seniority_cards.index(self.cards_computer[i][1]) for i in temp_1])
                        for i in temp_1:
                            if self.cards_computer[i][1] == self.seniority_cards[min_index]:
                                num_card_computer = i
                                self.temp_cards_computer.append(num_card_computer)
                                temp_cards_computer_l1.append(self.cards_computer[num_card_computer])

                    elif len(temp_2) != 0:
                        min_index = min([self.seniority_cards.index(self.cards_computer[i][1]) for i in temp_2])
                        for i in temp_2:
                            if self.cards_computer[i][1] == self.seniority_cards[min_index]:
                                num_card_computer = i
                        self.temp_cards_computer.append(num_card_computer)
                        temp_cards_computer_l1.append(self.cards_computer[num_card_computer])

                    else:
                        self.cards_computer.extend(self.temp_cards_user_l)
                        [self.cards_user.remove(i) for i in self.temp_cards_user_l]
                        print('\nКомпьютер не покрыл (взял)!  ')
                        self.timer() if len(self.cards_pack) > 0 else sleep(3)
                        self.clear()
                        self.move_win_user = 1
                        self.move_win_computer = 0
                        self.first_get_cards('user')
                        self.num_card_user = 88
                        break
                if len(all_cards) == len(temp_cards_computer_l1):
                    print(f'\nНеобходимо было покрыть: {all_cards}')
                    print('\nКомпьютер сходил:      ', temp_cards_computer_l1, '\nКарты покрыты, Бито!')
                    [self.cards_user.remove(i) for i in self.temp_cards_user_l]
                    [self.cards_computer.remove(i) for i in (self.temp_cards_computer_l + temp_cards_computer_l1)]
                    self.timer() if len(self.cards_pack) > 0 else sleep(3)
                    self.clear()
                    self.move_win_user = 0
                    self.move_win_computer = 1
                    self.first_get_cards('user')
                    self.num_card_user = 88
                    break

    def user_move(self):
        if self.type == 'transferable':
            self.temp_cards_user = []
            self.temp_cards_computer = []
            while True:
                self.num_card_user = int(input('\nВаш ход, введите номер вашей карты из списка: '))
                if self.num_card_user >= len(self.cards_user) or self.num_card_user < 0:
                    print('\nНеверный ход, попробуйте еще раз!')
                else:
                    self.temp_cards_user.append(self.num_card_user)
                    self.temp_cards_user_l = [self.cards_user[self.num_card_user] for self.num_card_user in
                                              self.temp_cards_user]
                    print(f'\nВы сходили:       {self.temp_cards_user_l[-1]}' if len(
                        self.temp_cards_user_l + self.temp_cards_computer) == 1 else f'\nВы перевели:       {self.temp_cards_user_l[-1]}')
                    break
            while self.num_card_user != 88:
                self.computer_input()
        elif self.type == 'thrown_up':
            temp_cards_user = []
            temp_cards_computer = []
            while True:
                num_card_user = int(input('\nВаш ход, введите номер вашей карты из списка: '))
                if num_card_user >= len(self.cards_user) or num_card_user < 0:
                    print('\nНеверный ход, попробуйте еще раз!')
                else:
                    break
            while num_card_user != 88:
                temp_cards_user.append(num_card_user)
                temp_cards_user_l = [self.cards_user[num_card_user] for num_card_user in temp_cards_user]
                print('\nВы сходили:       ', temp_cards_user_l[-1])
                temp_1 = []
                temp_2 = []
                for num_card_computer in range(len(self.cards_computer)):
                    if num_card_computer not in temp_cards_computer:
                        if self.cards_computer[num_card_computer][0] == self.cards_user[num_card_user][
                            0] and self.seniority_cards.index(
                                self.cards_computer[num_card_computer][1]) > self.seniority_cards.index(
                                self.cards_user[num_card_user][1]):
                            temp_1.append(num_card_computer)
                        elif self.cards_computer[num_card_computer][0] != self.cards_user[num_card_user][0] and \
                                self.cards_computer[num_card_computer][0] == self.trump[0]:
                            temp_2.append(num_card_computer)
                if len(temp_1) != 0:
                    min_index = min([self.seniority_cards.index(self.cards_computer[i][1]) for i in temp_1])
                    for i in temp_1:
                        if self.cards_computer[i][1] == self.seniority_cards[min_index]:
                            num_card_computer = i
                            temp_cards_computer.append(num_card_computer)
                            temp_cards_computer_l = [self.cards_computer[num_card_computer] for num_card_computer in
                                                     temp_cards_computer]
                    print('\nКомпьютер сходил: ', temp_cards_computer_l[-1],
                          f'\n\nВсе ходы Компьютера: {temp_cards_computer_l} \nВаши предыдущие ходы: {temp_cards_user_l}' if len(
                              temp_cards_computer) > 1 else '', '\n\nВаши карты Покрыты!  ')
                    if len(temp_cards_computer_l) == 6:
                        print('\nПокрыто 6 карт! Отбой не более 6 карт! Бито!')
                        self.timer() if len(self.cards_pack) > 0 else sleep(3)
                        self.clear()
                        [self.cards_computer.remove(i) for i in temp_cards_computer_l]
                        [self.cards_user.remove(i) for i in temp_cards_user_l]
                        self.move_win_user = 0
                        self.move_win_computer = 1
                        self.first_get_cards('user')
                        break
                    while True:
                        if (self.cards_user == temp_cards_user_l) and (len(self.cards_user) == 1):
                            num_card_user = 88
                        else:
                            self.print_cards_hand(temp_cards_user_l)
                            num_card_user = int(input(
                                '\nПодкиньте карту (введите номер карты из вашего списка) или введите 88 для "Отбоя": '))
                        if num_card_user == 88:
                            print('Бито!')
                            self.timer() if len(self.cards_pack) > 0 else sleep(3)
                            self.clear()
                            [self.cards_computer.remove(i) for i in temp_cards_computer_l]
                            [self.cards_user.remove(i) for i in temp_cards_user_l]
                            self.move_win_user = 0
                            self.move_win_computer = 1
                            self.first_get_cards('user')
                            break
                        elif (num_card_user < len(self.cards_user) and num_card_user >= 0) and (
                                self.cards_user[num_card_user] not in temp_cards_user_l) and (
                                self.cards_user[num_card_user][1] in [i[1] for i in temp_cards_computer_l] or
                                self.cards_user[num_card_user][1] in [i[1] for i in temp_cards_user_l]):
                            break
                        else:
                            print('\nНеверный ход, попробуйте еще раз!')
                elif len(temp_2) != 0:
                    min_index = min([self.seniority_cards.index(self.cards_computer[i][1]) for i in temp_2])
                    for i in temp_2:
                        if self.cards_computer[i][1] == self.seniority_cards[min_index]:
                            num_card_computer = i
                    temp_cards_computer.append(num_card_computer)
                    temp_cards_computer_l = [self.cards_computer[num_card_computer] for num_card_computer in
                                             temp_cards_computer]
                    print('\nКомпьютер сходил: ', temp_cards_computer_l[-1],
                          f'\n\nВсе ходы Компьютера: {temp_cards_computer_l} \nВаши предыдущие ходы: {temp_cards_user_l}' if len(
                              temp_cards_computer) > 1 else '', '\n\nВаши карты Покрыты!  ')
                    if len(temp_cards_computer_l) == 6:
                        print('\nПокрыто 6 карт! Отбой не более 6 карт! Бито!')
                        self.timer() if len(self.cards_pack) > 0 else sleep(3)
                        self.clear()
                        [self.cards_computer.remove(i) for i in temp_cards_computer_l]
                        [self.cards_user.remove(i) for i in temp_cards_user_l]
                        self.move_win_user = 0
                        self.move_win_computer = 1
                        self.first_get_cards('user')
                        break
                    while True:
                        if (self.cards_user == temp_cards_user_l) and (len(self.cards_user) == 1):
                            num_card_user = 88
                        else:
                            self.print_cards_hand(temp_cards_user_l)
                            num_card_user = int(input(
                                '\nПодкиньте карту (введите номер карты из вашего списка) или введите 88 для "Отбоя": '))
                        if num_card_user == 88:
                            print('Бито!')
                            self.timer() if len(self.cards_pack) > 0 else sleep(3)
                            self.clear()
                            [self.cards_computer.remove(i) for i in temp_cards_computer_l]
                            [self.cards_user.remove(i) for i in temp_cards_user_l]
                            self.move_win_user = 0
                            self.move_win_computer = 1
                            self.first_get_cards('user')
                            break
                        elif (num_card_user < len(self.cards_user) and num_card_user >= 0) and (
                                self.cards_user[num_card_user] not in temp_cards_user_l) and (
                                self.cards_user[num_card_user][1] in [i[1] for i in temp_cards_computer_l] or
                                self.cards_user[num_card_user][1] in [i[1] for i in temp_cards_user_l]):
                            break
                        else:
                            print('\nНеверный ход, попробуйте еще раз!')
                else:
                    self.cards_computer.extend(temp_cards_user_l)
                    [self.cards_user.remove(i) for i in temp_cards_user_l]
                    print('\nКомпьютер не покрыл (взял)!  ')
                    self.timer() if len(self.cards_pack) > 0 else sleep(3)
                    self.clear()
                    self.move_win_user = 1
                    self.move_win_computer = 0
                    self.first_get_cards('user')
                    break

    def computer_move(self):
        if self.type == 'transferable':
            self.temp_cards_user = []
            self.temp_cards_computer = []
            self.temp_cards_user_l = []
            self.temp_cards_computer_l = []
            # num_card_user = 0
            num_card_computer = random.randint(0, len(self.cards_computer) - 1)
            self.temp_cards_computer.append(num_card_computer)
            self.temp_cards_computer_l = [self.cards_computer[num_card_computer] for num_card_computer in
                                          self.temp_cards_computer]
            print('\nКомпьютер сходил:    ', self.temp_cards_computer_l[-1])
            self.user_input()
            if self.num_card_user != 88:
                self.computer_input()
        elif self.type == 'thrown_up':
            temp_cards_user = []
            temp_cards_computer = []
            temp_cards_user_l = []
            temp_cards_computer_l = []
            num_card_user = 0
            while num_card_user != 99:
                if len(temp_cards_user_l) == 6:
                    print('\nПокрыто 6 карт! Отбой не более 6 карт! Бито!')
                    self.timer() if len(self.cards_pack) > 0 else sleep(3)
                    self.clear()
                    [self.cards_computer.remove(i) for i in temp_cards_computer_l]
                    [self.cards_user.remove(i) for i in temp_cards_user_l]
                    self.move_win_user = 1
                    self.move_win_computer = 0
                    self.first_get_cards('computer')
                    break
                if len(temp_cards_computer) == 0:
                    num_card_computer = random.randint(0, len(self.cards_computer) - 1)
                elif len(temp_cards_computer) != 0:
                    check_in = 0
                    for num_card_computer in range(len(self.cards_computer)):
                        if (self.cards_computer[num_card_computer] not in temp_cards_computer_l) and (
                                self.cards_computer[num_card_computer][1] in [i[1] for i in temp_cards_user_l] or
                                self.cards_computer[num_card_computer][1] in [i[1] for i in temp_cards_computer_l]) and (len(temp_cards_user_l) != len(self.cards_user)):
                            check_in = 1
                            break
                    if check_in == 0:
                        print('\nКомпьютер не может подкинуть! Бито!')
                        self.timer() if len(self.cards_pack) > 0 else sleep(3)
                        self.clear()
                        [self.cards_computer.remove(i) for i in temp_cards_computer_l]
                        [self.cards_user.remove(i) for i in temp_cards_user_l]
                        self.move_win_user = 1
                        self.move_win_computer = 0
                        self.first_get_cards('computer')
                        break
                temp_cards_computer.append(num_card_computer)
                temp_cards_computer_l = [self.cards_computer[num_card_computer] for num_card_computer in
                                         temp_cards_computer]
                print('\nКомпьютер сходил:    ', temp_cards_computer_l[-1])
                if len(temp_cards_computer) > 1:
                    print('\nВсе ходы Компьютера:   ', temp_cards_computer_l)
                    print('Ваши предыдущие ходы: ', temp_cards_user_l, ' (ожидается Ваш ход...)', sep='')
                while True:
                    if len(temp_cards_computer) > 1:
                        self.print_cards_hand(temp_cards_user_l)
                    num_card_user = int(
                        input('\nВаш ход, введите номер вашей карты чтобы покрыть или введите 99 чтобы взять: '))
                    if num_card_user == 99:
                        print('\nВы не покрыли (взяли)!  ')
                        self.timer() if len(self.cards_pack) > 0 else sleep(3)
                        self.clear()
                        self.cards_user.extend(temp_cards_computer_l)
                        [self.cards_computer.remove(i) for i in temp_cards_computer_l]
                        self.move_win_user = 0
                        self.move_win_computer = 1
                        self.first_get_cards('computer')
                        break
                    elif num_card_user >= len(self.cards_user) or num_card_user < 0:
                        print('\nНеверный ход, попробуйте еще раз!')
                    elif (self.cards_user[num_card_user][0] == self.cards_computer[num_card_computer][
                        0] and self.seniority_cards.index(
                            self.cards_user[num_card_user][1]) > self.seniority_cards.index(
                            self.cards_computer[num_card_computer][1])) or (
                            self.cards_user[num_card_user][0] != self.cards_computer[num_card_computer][0] and
                            self.cards_user[num_card_user][0] == self.trump[0]):
                        temp_cards_user.append(num_card_user)
                        temp_cards_user_l = [self.cards_user[num_card_user] for num_card_user in temp_cards_user]
                        print('\nВы сходили: ', temp_cards_user_l[-1])
                        print('\nКарты Компьютера Покрыты! Ожидание подкидывания Компьютером...')
                        break
                    else:
                        print('\nНеверный ход, попробуйте еще раз!')


if __name__ == '__main__':
    game = GameFool_v2(1, 'thrown_up') # thrown_up or transferable
    print(game)
    game.play_cards()
