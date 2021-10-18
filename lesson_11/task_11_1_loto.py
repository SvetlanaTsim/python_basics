import random
import itertools

class LotoCard:
    def __init__(self, name):
        self.name = name
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._numbers = random.sample(range(1, self._MAX_NUMBER), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def __str__(self):
        return f'{self.name}:\n{"-" * 22}\n' + '\n'.join([' '.join(map(str, line)) for line in self._card]) + \
               f'\n{"-" * 22}'

    def has_number(self, number):
        for line in self._card:
            num_count = line.count(number)
            if num_count > 0:
                return True
        else:
            return False

    def try_stroke(self, number):
        if self.has_number(number) == True:
            for line in self._card:
                for index, item in enumerate(line):
                    if isinstance(item, int) and item == number:
                        line[index] = '-'
                        self._numbers_stroked = self._numbers_stroked + 1


class LotoGame:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.beg = [num for num in range(1, self.player._MAX_NUMBER + 1)]
        random.shuffle(self.beg)

    def game_start(self):
        keg_count = self.player._MAX_NUMBER
        # чтобы дальше использовать next()
        iterator = itertools.takewhile(lambda x: x, self.beg)
        while True:
            new_keg = next(iterator)
            keg_count = keg_count - 1
            print(f'Новый бочонок: {new_keg} (осталось {keg_count})')
            print(self.player)
            print(self.computer)
            #computer
            self.computer.try_stroke(new_keg)
            if self.computer._numbers_stroked == self.computer._MAX_NUMBER_IN_CARD:
                print(f'Компьютер {self.computer.name} выиграл!')
                break
            #player
            player_answer = input('Зачеркнуть цифру? (y/n) ')
            real_answer = self.player.has_number(new_keg)

            if player_answer == 'y' and real_answer == True:
                self.player.try_stroke(new_keg)
                if self.player._numbers_stroked == self.player._MAX_NUMBER_IN_CARD:
                    print(f'Игрок {self.player.name} выиграл!')
                    break
            elif (player_answer == 'y' and real_answer == False) or (player_answer == 'n' and real_answer == True):
                print(f'Игрок {self.player.name} проиграл!')
                break
            elif player_answer == 'n' and real_answer == False:
                pass
            else:
                print(f'Нужно было вводить y или n. Игрок {self.player.name} проиграл!')
                break


human = LotoCard('Svetlana')
computer = LotoCard('R2D2')
game_1 = LotoGame(human, computer)
game_1.game_start()
