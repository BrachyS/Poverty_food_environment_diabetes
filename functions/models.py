import warnings
warnings.filterwarnings('ignore')

def gridsearch_models(X, y, regressor,params):
    '''Conduct GridsearchCV to find best parameters, and
     fit the model with best parameters'''

    # Split data into train and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=5)
    fitted = regressor.fit(X_train, y_train)
    model = GridSearchCV(fitted,params)
    model.fit(X_train, y_train)
    best_params = model.best_estimator_.get_params()
    print('Best parameters:', best_params) # print best parameters

    # Fit model with best params
    regressor.set_params(**best_params)
    best_model = regressor.fit(X_train,y_train)
    print('Cross validation scores:',cross_val_score(model, X_train, y_train)) # print cross validation scores

    # Print model score (e.g.,R-squared) for train and test data set
    print('Training data R-squared for best model:', round(model.score(X_train, y_train),2))
    print('Testing data R-squared for best model:', round(model.score(X_test, y_test),2))

    return best_model

