#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree



clf = AdaBoostClassifier(base_estimator=RandomForestClassifier(max_depth=4, random_state=3,n_jobs = 2), n_estimators=4, learning_rate=1.0, algorithm='SAMME.R', random_state=None)

#clf = RandomForestClassifier(max_depth=3, random_state=1,n_jobs = 3)

#clf=KNeighborsClassifier(n_neighbors=3)
#clf = GaussianNB()
#clf = SVC(C=1, kernel='linear')
#clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
prediction = clf.predict(features_test)

print accuracy_score(labels_test,prediction)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass





