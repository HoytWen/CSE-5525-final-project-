from sklearn.feature_extraction.text import CountVectorizer
import csv
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
data_path = 'V1.4_Training.csv'
with open(data_path, 'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    my_list = list(reader,)

my_id=[]
my_data=[]
my_label=[]
cv = CountVectorizer(min_df=5)
#cv=TfidfVectorizer(min_df=10)
for i in my_list:
    my_id.append(i[0])
    my_data.append(i[1])
    my_label.append(int(i[2]))
cv_fit=cv.fit_transform(my_data)
featuremat=cv_fit.toarray()

test_path='SubtaskB_EvaluationData_labeled.csv'
#test_path='SubtaskB_Trial_Test_Labeled.csv'
with open(test_path, 'r',encoding='utf-8') as ft:
    reader = csv.reader(ft)
    test_list = list(reader,)

test_id=[]
test_data=[]
test_label=[]
for i in test_list:
    test_id.append(i[0])
    test_data.append(i[1])
    test_label.append(int(i[2]))
cv_fit=cv.transform(test_data)
test_featuremat=cv_fit.toarray()

X_train, X_label, Y_train, Y_label = np.array(featuremat), np.array(my_label),np.array(test_featuremat),np.array(test_label)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(Y_train)


# training model use different methods
#logreg = linear_model.LogisticRegression(C=10)
logreg = linear_model.Perceptron(tol=1e-3, random_state=0)
#logreg = LinearSVC(random_state=0, tol=1e-5)
logreg.fit(X_train, X_label)

# prediction
prepro = logreg.predict(Y_train)
#acc=sklearn.metrics.accuracy_score(prepro, Y_label)
acc = sklearn.metrics.f1_score(prepro, Y_label
                                )
print (acc)



