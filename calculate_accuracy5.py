#!/usr/bin/env python
# coding: utf-8




import numpy as np




def calculate_accuracy_per_label(labels, conf_matrix):
    accuracy = []
    group_size=[]
    for i in range(len(labels)):
        if labels[i] != 'Unclassified':
            true_result = conf_matrix[i,i]
            all_result = sum(conf_matrix[:,i])
            group_size.append(all_result)
            if all_result == 0:
                accuracy.append(0)
            else:
                accuracy.append(true_result/all_result)    
    if 'Unclassified' in labels:
        print('Removing Unclassified groups')
        labels.remove('Unclassified')
    accuracy_dict = {'labels':labels,'group_size':group_size, 'accuracy':accuracy}
    return accuracy_dict
        

