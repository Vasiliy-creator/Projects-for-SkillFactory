
def game_core_v3(predict):
    numbers = range(1, 101)
    count = 0
    while True:
        count += 1
        middle_pos = len(numbers) // 2
        higher = len(numbers)
    
        if predict==numbers[middle_pos]:
            break
        # В двух блоках ниже список сокращается до тех элементов, 
        # в которых находится число
        elif predict>numbers[middle_pos]: 
            numbers = numbers[middle_pos:higher] 

        elif predict<numbers[middle_pos]:
            numbers = numbers[:middle_pos]
    return count

import numpy as np
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)



score_game(game_core_v3)





