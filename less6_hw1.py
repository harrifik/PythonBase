# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

import time


class TrafficLight:
    def __init__(self):
        self._color = 'red'

    def running(self):
        self._color = 'red'
        print('Красный свет!')
        time.sleep(7)

        self._color = 'yellow'
        print('Желтый свет!')
        time.sleep(5)

        self._color == 'green'
        print('Зеленый свет.')
        time.sleep(5)


my_TrafficLight = TrafficLight()
my_TrafficLight.running()
