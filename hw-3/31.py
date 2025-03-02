# "Крестики-нолики" с использованием ООП и процедурной парадигмы

class TicTacToe:
    def __init__(self):
        self.playing_field = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_playing_field(self):
        print("примечание: 'exit' выход из игры")
        print("поле для игры tic-toe -")
        print("нумерация -")
        for i in range(0, 9, 3):
            print(f"     {i+1} | {i+2} | {i+3}     {self.playing_field[i]} | {self.playing_field[i+1]} | {self.playing_field[i+2]}")
            if i < 6:
                print("     ---------     ---------")

    def make_move(self, position):
        if self.playing_field[position] == ' ':
            self.playing_field[position] = self.current_player
            if self.check_winner():
                self.print_playing_field()
                print(f"игрок {self.current_player} выиграл!")
                return True
            if self.is_draw():
                self.print_playing_field()
                print("это ничья!")
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return False
        else:
            print("недопустимый ход, пожалуйста, попробуйте снова.")
            return False

    def check_winner(self):
        # Одномерный массив
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтальные ряды
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикальные ряды
            (0, 4, 8), (2, 4, 6)              # Диагонали
        ]
        for combo in winning_combinations:
            if (self.playing_field[combo[0]] == self.playing_field[combo[1]] ==
                    self.playing_field[combo[2]] != ' '):
                return True
        return False

    def is_draw(self):
        return ' ' not in self.playing_field

def play_game():
    game = TicTacToe()
    while True:
        game.print_playing_field()
        move = input(f"игрок {game.current_player}, выберите ячейку от 1 до 9 : ")
        if move.lower() in ['exit', 'stop', 'стоп', 'выход']:
            print("игра завершена.")
            break
        try:
            move = int(move) - 1
            if move < 0 or move > 8:
                raise ValueError
        except ValueError:
            print("неверный ввод, пожалуйста, введите число от 1 до 9.")
            continue

        if game.make_move(move):
            break

if __name__ == "__main__":
    play_game()
