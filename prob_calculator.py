# link to replit code: https://replit.com/@MauricioFiorent/boilerplate-probability-calculator#prob_calculator.py

import copy
import random

class Hat:

    def __init__(self, **color):
        self.color = color
        self.contents = []
        key_list = list(self.color.keys())
        value_list = list(self.color.values())
        count = -1
        for item in key_list:
            count += 1
            for i in range(value_list[count]):
                self.contents.append(item)

    def draw(self, arguments):
        if arguments >= len(self.contents):
            return self.contents

        random_list = random.sample(self.contents, arguments)
        for i in random_list:
            self.contents.remove(i)

        return random_list

    def __repr__(self):
        return str(self.contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        appear = 0
        draw_dic = {}
        draw = hat_copy.draw(num_balls_drawn)
        for i in draw:
            if i in draw_dic:
                draw_dic[i] += 1
            else:
                draw_dic[i] = 1

        for i in expected_balls:
            if i in draw_dic and expected_balls.get(i) <= draw_dic.get(i):
                appear += 1

        dic_length = len(expected_balls)

        if appear == dic_length:
            count += 1

    prob = count / num_experiments
    return prob
