def winner(sc1, sc2, time1, time2):
    name_1 = 'Победа команды "Мастера кода"'
    name_2 = 'Победа команды "Волшебники данных"'
    if (sc1 > sc2) or (sc1 == sc2 and time1 < time2):
        return name_1
    elif (sc1 < sc2) or (sc1 == sc2 and time1 > time2):
        return name_2
    else:
        return 'Ничья!'


team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
challenge_result = winner(score_1, score_2, team1_time, team2_time)

print('Использование %s' % '%')
print('Кол-во участников в команде "Мастера кода": %d' % team1_num)
print('Кол-во участников по командам: "Мастера кода" %s, "Волшебники данных" %s' % (team1_num, team2_num))
print()
print('Использование "format()"')
print('Команда "Волшебники данных" решила {} задачи'.format(score_2))
print('Время решения задач: "Мастера кода" {0}сек., "Волшебники данных" {1}сек.'.format(team1_time, team2_time))
print()
print('Использование "f-строк"')
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Было решено {tasks_total} задач, среднее время {time_avg} секунд на задачу')
