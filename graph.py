#encoding=utf-8

from __future__ import absolute_import as _absolute_import
from __future__ import division as _division
from __future__ import print_function as _print_function

__author__ = "turingli"
__date__ = "20181224"


"""
Draw a graph with matplotlib, color by degree.

You must have matplotlib for this to work.
"""

import matplotlib.pyplot as plt
import numpy as np

import networkx as nx

class DrawGraph:

    def __init__(self, adj_mat, node_labels, label2color=None, weight_graph=False, direct_graph=False):
        """
        :param adj_mat: 图的连接矩阵，>1代表有边
        :param node_labels: 顶点的标签
        :param label2color: 标签对应的颜色
        :param weight_graph: 是否为加权图
        :param direct_graph: 是否是有向图
        """
        G = nx.Graph()
        edge_list = []
        assert len(adj_mat) == len(node_labels)
        adj_mat = np.array(adj_mat)
        node_num = len(node_labels)
        for i in range(node_num):
            for j in range(node_num):
                if i != j and adj_mat[i,j] > 0:
                    edge_list.append([i,j])
        G.add_edges_from(edge_list)
        # for i in range(node_num):
        #     G.add_node(i, label=node_labels[i])
        # pos = nx.spring_layout(G)
        # pos = nx.circular_layout(G)
        node_label_array = np.array(node_labels)
        label_group = np.unique(node_label_array)
        if label2color is None:
            color_list = np.random.rand(len(label_group))
            label2color = {}
            for i in range(len(label_group)):
                label2color[label_group[i]] = color_list[i]

        node_colors = [label2color[label] for label in node_labels]
        nx.draw(G, cmap=plt.get_cmap('jet'), node_color=node_colors)

        # # nodes
        # for label in label_group:
        #     ix = [v[0] for v in np.where(node_label_array == label)]
        #     colors = [label2color[node_labels[iq]] for iq in ix]
        #     print(ix, label, colors)
        #     nx.draw_networkx_nodes(
        #         G, pos,
        #         nodelist=ix,
        #         node_size=300,
        #         node_color=colors,
        #         cmap=plt.get_cmap('jet'),
        #         alpha=0.8
        #     )
        # node_label_dict = dict(zip(range(node_num), node_labels))
        # nx.draw_networkx_labels(G, pos, node_label_dict, font_size=10)


        # nx.draw_networkx_edges(G, pos,
        #                        edgelist=edge_list,
        #                        width=3, alpha=0.5, edge_color='b')

        plt.axis('off')
        plt.savefig("labels_and_colors.png")  # save as png
        plt.show()  # display

        # # some math labels
        # labels={}
        # labels[0]=r'$a$'
        # labels[1]=r'$b$'
        # labels[2]=r'$c$'
        # labels[3]=r'$d$'
        # labels[4]=r'$\alpha$'
        # labels[5]=r'$\beta$'
        # labels[6]=r'$\gamma$'
        # labels[7]=r'$\delta$'


if __name__  == "__main__":
    adj_mat = [ [1, 1, 1,1], [1, 1, 1,1], [1, 1, 1,1], [1,1,1,1] ]
    node_labels = ["x", "y", "z", "x"]
    DrawGraph(adj_mat, node_labels)

