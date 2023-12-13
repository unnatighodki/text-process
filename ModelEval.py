import math
import PorterStemmer
import Preprocess
import NaiveBayes

import pandas as pd
import numpy as np

class ModelEvalution:
    """
    This class is used for model evaluation by defining various metrics from example accuracy, recall, etc

    """

    def __init__(self, y_actual = None, y_pred = None):
        self.y_actual = y_actual
        self.y_pred = y_pred
        
    def new_class_labels(self, y):
        act = sorted(np.unique(y))
        y_new = [0] * len(y)
        act_num_class = list(range(len(np.unique(y))))
        
        for i in range(len(y)):
            for j in range(len(act)):
                if y[i] == act[j]:
                    y_new[i] = act_num_class[j]
        return y_new

    def conf_mat(self):
        y_actual_new = self.new_class_labels(self.y_actual)
        y_pred_new = self.new_class_labels(self.y_pred)
        
        num_class = len(np.unique(y_actual_new))
        conf_mat = np.zeros((num_class,num_class), dtype=int, order='C')

        for i in range(len(y_actual_new)):
            act_class = y_actual_new[i]
            pred_class = y_pred_new[i]
            conf_mat[act_class, pred_class] +=1

        return conf_mat
    
    def dataframe_conf_mat(self,conf_matrix):
        dataframe = pd.DataFrame(conf_matrix)
        # Replace artificial classes with actual class into next function

        actual_classes = sorted(np.unique(self.y_actual))
        dataframe.index, dataframe.columns = actual_classes, actual_classes

        #print(dataframe)
        return dataframe

    def model_accuracy(self,y_actual, y_pred):
        true_prediction = 0
        sample_count = len(y_actual)
        for true,pred in zip(y_actual,y_pred):
            if true == pred:
                true_prediction += 1
        return round(true_prediction/sample_count, 3)

    def class_precision(self,confusion_mat, ind_class):
        # In this case confusion matrix would be dataframe

        true_pred = confusion_mat.iloc[ind_class,ind_class]
        false_pred = np.sum(confusion_mat.iloc[:,ind_class]) - true_pred

        total_pred = true_pred + false_pred # Denominator
        
        return (round(true_pred/total_pred,2) if total_pred != 0 else 0 )

    def class_recall(self, confusion_mat, ind_class):
        # In this case confusion matrix would be dataframe
        true_pred = confusion_mat.iloc[ind_class,ind_class]
        false_negative_pred = np.sum(confusion_mat.iloc[ind_class,:]) - true_pred

        total_pred = true_pred + false_negative_pred # Denominator
    
        return (round(true_pred/total_pred,2) if total_pred != 0 else 0 )

    def f1_score(self, confusion_mat,ind_class):
        # In this case confusion matrix would be dataframe

        recall = self.class_recall(confusion_mat,ind_class)
        precision= self.class_precision(confusion_mat,ind_class)

        return (round(2*((recall*precision)/(recall+precision)),2) if (recall+precision) != 0 else 0 )


if __name__ == "__main__":

    y_actual = [1,-1,0,1,1,0,0,1,-1]
    y_pred= [1,-1,0,0,1,-1,1,1,-1]

    x = ModelEvalution(y_actual,y_pred)

    confusion_matrix = x.conf_mat()
    print(confusion_matrix)

    temp_conf = x.dataframe_conf_mat(confusion_matrix)

    x.model_accuracy(y_actual, y_pred)
    x.class_precision(temp_conf,1)
    x.class_recall(temp_conf,1)

    x.f1_score(temp_conf,1)


        











