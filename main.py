from util import average_sample
from util import standard_deviation


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
