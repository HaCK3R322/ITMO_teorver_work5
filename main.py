import matplotlib.pyplot as plt


def average_sample(data):
    summary = 0
    n = len(data)
    for i in range(n):
        summary += data[i]

    return summary / n


def standard_deviation(data):
    average = average_sample(data)

    n = len(data)
    summary2 = 0
    for i in range(n):
        summary2 += (data[i] - average) ** 2

    return summary2 / n


def work5(data):
    # вариационный ряд
    data.sort()
    print('Вариационный ряд:', data)

    # экстремальные значения
    min_value = data[0]
    max_value = data[-1]
    print('Минимум:', min_value, '\nМаксимум:', max_value)

    # Математическое ожидание
    # так как каждое значение в выборке уникально, мат ожиданием будет средневыборочное
    print('Математическое ожидание:', average_sample(data))

    # Среднеквадратическое отклонение
    print('Среднеквадратическое отклонение:', standard_deviation(data))

    # Эмперическая функция распределения
    def empirical_distribution_function(x):
        n = len(data)
        summary = 0
        for i in range(n):
            if data[i] <= x:
                summary += 1
        return summary / n

    # График эмперической функции распределения
    plt.plot(data, [empirical_distribution_function(x) for x in data])
    plt.title('График эмперической функции распределения')
    plt.show()

    # Гистограмма и полигон частот группированных данных
    # группировка данных

    # количество групп
    k = 10
    # ширина группы
    h = (max_value - min_value) / k
    # границы групп
    borders = [min_value + h * i for i in range(k + 1)]
    # группы
    groups = [[] for _ in range(k)]
    for x in data:
        for i in range(k):
            if borders[i] <= x < borders[i + 1]:
                groups[i].append(x)
                break
    # частоты групп
    frequencies = [len(group) for group in groups]

    # график гистограммы
    plt.bar(borders[:-1], frequencies, width=h)
    plt.title('Гистограмма частот')
    plt.show()
    # график полигона частот
    plt.plot(borders[:-1], frequencies)
    plt.title('Полигон частот')
    plt.show()


if __name__ == '__main__':
    array = [
        0.83,
        0.73,
        -0.48,
        0.00,
        -1.35,
        1.59,
        0.31,
        0.17,
        0.59,
        -0.45,
        1.35,
        1.60,
        -0.30,
        -0.18,
        -0.24,
        -1.73,
        0.51,
        0.03,
        0.26,
        1.70,
    ]

    work5(array)
