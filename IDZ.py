#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import math

class SeriesThread(threading.Thread):
    def __init__(self, x, epsilon):
        # Инициализация объекта
        threading.Thread.__init__(self)
        self.x = x
        # Заданная точность для вычислений
        self.epsilon = epsilon
        # Инициализация переменной для хранения суммы ряда
        self.result = 0

    def run(self):
        n = 0
        term = (self.x ** (2 * n)) / math.factorial(2 * n)

        # Вычисление суммы ряда до достижения заданной точности epsilon
        while abs(term) > self.epsilon:
            self.result += term
            n += 1
            term = (self.x ** (2 * n)) / math.factorial(2 * n)

def main():
    x = 1/2
    epsilon = 1e-7

    # Задаем контрольное значение
    control_value = (math.exp(x) + math.exp(-x)) / 2
    series_thread = SeriesThread(x, epsilon)
    series_thread.start()
    series_thread.join()
    series_sum = series_thread.result

    # Сравниваем результат с контрольным значением
    if abs(series_sum - control_value) < epsilon:
        print(f"Сумма ряда: {series_sum}")
        print(f"Контрольное значение: {control_value}")
        print("Результат совпадает с контрольным значением.")
    else:
        print("Результат не совпадает с контрольным значением.")

if __name__ == "__main__":
    main()
