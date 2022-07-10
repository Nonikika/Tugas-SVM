#HYPERPARAMETER TUNING DENGAN GRIDSEARCHCV

from sklearn.model_selection import GridSearchCV

parameters = {
        'kernel' : ['rbf', 'poly', 'sigmoid']
        'C' : [0.5, 1, 10, , 100],
        'gamma' : ['scale', 1, 0.1, 0.001]
}

grid_search = GridSearchCV(estimator=SVC(random_state=0),
                           param_grid=parameters,
                           n_jobs=6
                           verbose=1
                           scoring='accuracy')

grid_search.fit(X_train, y_train)
  File "C:\Users\dell\AppData\Local\Temp\ipykernel_8148\2023502528.py", line 7
    'C' : [0.5, 1, 10, , 100],
    ^
SyntaxError: invalid syntax
print(f'Best Score: {grid_search.best_score_}')

best_params = grid_search.best_estimator_.get_paramms()
print(f'Best Paramseters : ')
for param in parameters :
    print(f'\t{param} : {best_params[param]}')
    
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_8148\2685046144.py in <module>
----> 1 print(f'Best Score: {grid_search.best_score_}')
      2 
      3 best_params = grid_search.best_estimator_.get_paramms()
      4 print(f'Best Paramseters : ')
      5 for param in parameters :

NameError: name 'grid_search' is not defined
 
