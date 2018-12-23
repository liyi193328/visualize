#encoding=utf-8

from __future__ import absolute_import as _absolute_import
from __future__ import division as _division
from __future__ import print_function as _print_function

__author__ = "turingli"
__date__ = "20181223"

import fire
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

def multi_scatter(exp_cluster_list, cluster_type_list, color_list=None):
    """
    :param exp_cluster_list: 实验聚类结果list
    :param cluster_type_list: 类别名字结果
    :param color_list: 类别颜色列表，传入ax.scatter
    :return:
    """
    exp_num = len(exp_cluster_list) #对比实验个数
    cluster_type_num = len(cluster_type_list) #类别个数
    if color_list is None:
        color_list = np.random.rand(cluster_type_num)
    type2color = dict(zip(cluster_type_list, color_list))
    fig, ax_list = plt.subplots(1, exp_num)
    if exp_num == 1:
        ax_list = [ax_list]
    fig.subplots_adjust(hspace=0.3)

    for i in range(exp_num):
        ax = ax_list[i]

        cluster = exp_cluster_list[i]
        X, Y, cluster_result, name = np.array(cluster["X"]), np.array(cluster["Y"]), \
                               np.array( cluster["cluster"] ), cluster["name"]
        for g in cluster_type_list:
            ix = np.where(cluster_result == g)
            x, y = X[ix], Y[ix]
            ax.scatter(x, y, type2color[g])
        ax.set_title(name)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.set_xticks([])
        ax.set_yticks([])
    fig.legend(cluster_type_list, loc="upper right", title="Cell Types")
    plt.show()

if __name__ == "__main__":
    cluster_list = [
        {"X": [1,2,3], "Y":[2,3,4], "cluster":["l", "y", "y"], "name": "exp1"},
        {"X":[4, 7, 8], "Y": [1, 3, 5], "cluster":["y", "l", "l"], "name": "exp2"}
    ]
    cluster_type_list = ["l", "y"]
    multi_scatter(cluster_list, cluster_type_list)