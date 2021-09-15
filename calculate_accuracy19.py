#!/usr/bin/env python
# coding: utf-8




import numpy as np




def calculate_accuracy_per_label(label, conf_matrix, y_train):
    accuracy = []
    group_size_pred=[]
    group_size_test=[]
    group_size_train=[]
    predict_vs_test_size=[]
    group_size_train_dict = {k:y_train.count(k) for k in label}
    for i in range(len(label)):
        if label[i] != 'Unclassified':
            true_result = conf_matrix[i,i]
            all_result_pred = np.sum(conf_matrix,axis=0)[i]
            group_size_pred.append(all_result_pred)
            all_result_test = np.sum(conf_matrix,axis=1)[i]
            print(all_result_pred, all_result_test)
            group_size_test.append(all_result_test)
            group_size_train.append(group_size_train_dict[label[i]])
            
            if all_result_pred == 0:
                accuracy.append(0)
            else:
                accuracy.append(true_result/all_result_pred)
                
            if all_result_test == 0:
                predict_vs_test_size.append(all_result_pred+1)
            else:
                predict_vs_test_size.append(all_result_pred/all_result_test)
                
                
    if 'Unclassified' in label:
        print('Removing Unclassified groups')
        label.remove('Unclassified')
    accuracy_dict = {'labels':label, 'accuracy':accuracy,'predict_vs_test_size': predict_vs_test_size,
                     'group_size_pred':group_size_pred, 'group_size_test':group_size_test, 'group_size_train':group_size_train}
    return accuracy_dict
        

