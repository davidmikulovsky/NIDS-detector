
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis

from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

from scipy.io import arff
import pandas as pd





def plot_confusion_matrix(test_Y, predict_y):
     C = confusion_matrix(test_Y, predict_y)
     A =(((C.T)/(C.sum(axis=1))).T)
     B =(C/C.sum(axis=0))
     plt.figure(figsize=(20,4))
     labels = [1,2]
     cmap=sns.light_palette("green")
     plt.subplot(1, 3, 1)
     sns.heatmap(C, annot=True, cmap=cmap, fmt="d", xticklabels=labels, yticklabels=labels)
     plt.xlabel('Predicted Class')
     plt.ylabel('Original Class')
     plt.title("Confusion matrix")
     plt.subplot(1, 3, 2)
     sns.heatmap(B, annot=True, cmap=cmap, fmt=".2f", xticklabels=labels, yticklabels=labels)
     plt.xlabel('Predicted Class')
     plt.ylabel('Original Class')
     plt.title("Precision matrix")
     plt.subplot(1, 3, 3)
     sns.heatmap(A, annot=True, cmap=cmap, fmt=".2f", xticklabels=labels, yticklabels=labels)
     plt.xlabel('Predicted Class')
     plt.ylabel('Original Class')
     plt.title("Recall matrix")
     #plt.show()
     plt.savefig('books_read_dos3.png')


# panda=pd.read_csv("./input2/phishing.csv")

#data = arff.loadarff('./input3/DOS/KDDTrain20DOS.arff')

#data = arff.loadarff('./input3/DOS/KDDTrain20DOSFS.arff')


#data = arff.loadarff('./input3/R2L/KDDTrain20R2LFS.arff')
data = arff.loadarff('./input3/U2R/KDDTest21DOS.arff')


panda = pd.DataFrame(data[0])
panda.drop_duplicates(keep=False, inplace=True)

# panda = old[['urgent',  'root_shell', 'is_guest_login', 'dst_host_srv_count', 'dst_host_same_src_port_rate', 'xAttack']].copy()


print(panda.head())
print(panda.columns)

print(panda.shape)
#print(panda.isnull().sum())


X= panda.drop(columns='xAttack')
print(X.head())

Y=panda['xAttack']
Y=pd.DataFrame(Y)
print(Y.head())

Y=Y.astype('int')
X=X.astype('int')
train_X,test_X,train_Y,test_Y = train_test_split(X,Y,test_size=0.2,random_state=31)


print(train_X.shape)
print(test_X.shape)
print(train_Y.shape)
print(test_Y.shape)

knn=KNeighborsClassifier(n_neighbors=1)
model_2= knn.fit(train_X,train_Y)

knn_predict=model_2.predict(test_X)

accuracy_score(knn_predict,test_Y)

print(classification_report(test_Y,knn_predict))


plot_confusion_matrix(test_Y, knn_predict)