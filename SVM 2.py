#CLASSIFICATION DENGAN SVC ((SUPPORT VECTOR CLASSIFER)

from sklearn.svm import SVC

model = SVC(random_state=0)
model.fit(X_train, y_train)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_4720\2153253058.py in <module>
      4 
      5 model = SVC(random_state=0)
----> 6 model.fit(X_train, y_train)

NameError: name 'X_train' is not defined
from sklearn.metrics import classification_report

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_4720\136686293.py in <module>
      1 from sklearn.metrics import classification_report
      2 
----> 3 y_pred = model.predict(X_test)
      4 print(classification_report(y_test, y_pred))

NameError: name 'X_test' is not defined
