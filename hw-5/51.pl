% Определение предиката my_sum_list/2
my_sum_list([], 0). % Базовый случай: сумма пустого списка равна 0
my_sum_list([Head|Tail], Sum) :-
    my_sum_list(Tail, TailSum), % Рекурсивный вызов для хвоста списка
    Sum is Head + TailSum.      % Вычисление суммы текущего элемента и суммы хвоста

/** <examples>

?- my_sum_list([1, 2, 3, 4], Sum).
?- my_sum_list([10, 20, 30], Sum).
?- my_sum_list([], Sum).

*/

% Установка начальной цели
:- initialization(main).

% Определение начальной цели
main :-
    format('"The sum list"~n', []),
    my_sum_list([1, 2, 3, 4], Sum),
    format('Sum of [1, 2, 3, 4] is ~w~n', [Sum]).
