import sys

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.neighbors import KNeighborsClassifier

from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from scipy.io import arff

def plot_confusion_matrix(test_Y, predict_y):
     C = confusion_matrix(test_Y, predict_y)
     A =(((C.T)/(C.sum(axis=1))).T)
     B =(C/C.sum(axis=0))
     plt.figure(figsize=(14, 4))
     labels = [1, -1]
     cmap=sns.light_palette("blue")
     plt.subplot(1, 3, 1)
     sns.heatmap(C, annot=True, cmap=cmap, fmt=".2f", xticklabels=labels, yticklabels=labels)
     plt.xlabel('Predicted')
     plt.ylabel('Actual')
     plt.title("Confusion matrix")
     plt.subplot(1, 3, 2)
     sns.heatmap(B, annot=True, cmap=cmap, fmt=".2f", xticklabels=labels, yticklabels=labels)
     plt.xlabel('Predicted')
     plt.ylabel('Actual')
     plt.title("Precision matrix")
     plt.subplot(1, 3, 3)
     sns.heatmap(A, annot=True, cmap=cmap, fmt=".2f", xticklabels=labels, yticklabels=labels)
     plt.xlabel('Predicted')
     plt.ylabel('Actual')
     plt.title("Recall matrix")
     # plt.show()
     plt.savefig('./output/output_DOS.png')

def main(sys):

     #panda=pd.read_csv("./input/phishing.txt")


     input_file_dataset = sys[1]
     column_result = sys[2]
     split = float(sys[3])
     kNN = int(sys[4])

     print(input_file_dataset)
     print(column_result)
     print(split)
     print(kNN)

     #'./input3/R2L/KDDTrain20R2L.arff'
     data = arff.loadarff(input_file_dataset)

     panda = pd.DataFrame(data[0])

     # print(panda.head())
     # f = open("demofile3.txt", "w")
     # f.write(str(panda.columns))
     # f.close()

     print(panda.columns)
     print(panda.shape)
     print(panda.isnull().sum())

     panda.drop_duplicates(keep=False, inplace=True)
     X= panda.drop(columns=column_result)

     print(X.head())

     Y=panda[column_result]

     print(panda.head())
     print(panda.columns)

     print(panda.shape)

     # counter = 0
     # for index, row in panda.iterrows():
     #     if b'1' == row['xAttack']:
     #          counter = counter +1

     Y=pd.DataFrame(Y)
     print(Y.head())

     Y=Y.astype('int')
     X=X.astype('int')
     train_X,test_X,train_Y,test_Y = train_test_split(X,Y,test_size=split,random_state=2)


     print(train_X.shape)
     print(test_X.shape)
     print(train_Y.shape)
     print(test_Y.shape)

     knn=KNeighborsClassifier(n_neighbors=kNN)
     model_2= knn.fit(train_X,train_Y)

     knn_predict=model_2.predict(test_X)

     accuracy_score(knn_predict,test_Y)

     print(classification_report(test_Y,knn_predict))


     plot_confusion_matrix(test_Y, knn_predict)

     #
     # print("counter is", counter)


if __name__ == "__main__":
     main(sys.argv[0:])