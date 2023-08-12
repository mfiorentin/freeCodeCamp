# link to replit code: https://replit.com/@MauricioFiorent/boilerplate-mean-variance-standard-deviation-calculator#mean_var_std.py

import numpy as np
import copy

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    else:

        numb_list = copy.deepcopy(list)
        final_dic = {}

        #transforming the list into a 3x3 array:

        list_array = np.array(numb_list)
        array_3x3 = list_array.reshape(3, 3)

        #calculating the mean:

        mean_axis_1 = np.mean(array_3x3, axis=0).tolist()
        mean_axis_2 = np.mean(array_3x3, axis=1).tolist()
        mean_flat = np.mean(array_3x3).tolist()
        final_dic["mean"] = [mean_axis_1, mean_axis_2, mean_flat]

        #calculation the variance:

        var_1 = np.var(array_3x3, axis=0).tolist()
        var_2 = np.var(array_3x3, axis=1).tolist()
        var_flat = np.var(array_3x3).tolist()
        final_dic["variance"] = [var_1, var_2, var_flat]

        #calculating the standard deviation:

        std_1 = np.std(array_3x3, axis=0).tolist()
        std_2 = np.std(array_3x3, axis=1).tolist()
        std_flat = np.std(array_3x3).tolist()
        final_dic["standard deviation"] = [std_1, std_2, std_flat]

        #calculating max value:

        max_1 = np.max(array_3x3, axis=0).tolist()
        max_2 = np.max(array_3x3, axis=1).tolist()
        max_flat = np.max(array_3x3).tolist()
        final_dic["max"] = [max_1, max_2, max_flat]

        #calculating min value:

        min_1 = np.min(array_3x3, axis=0).tolist()
        min_2 = np.min(array_3x3, axis=1).tolist()
        min_flat = np.min(array_3x3).tolist()
        final_dic["min"] = [min_1, min_2, min_flat]

        #calculating sum value:

        sum_1 = np.sum(array_3x3, axis=0).tolist()
        sum_2 = np.sum(array_3x3, axis=1).tolist()
        sum_flat = np.sum(array_3x3).tolist()
        final_dic["sum"] = [sum_1, sum_2, sum_flat]

        return final_dic
