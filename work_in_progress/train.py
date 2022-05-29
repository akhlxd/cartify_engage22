import pandas as pd
import numpy as np
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score, roc_auc_score, make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
# import matplotlib.pyplot as plt
# import seaborn as sns
# from IPython.display import clear_output
import sys
# %matplotlib inline

class Train :
    def __init__():{}
    sys.path.insert(0,"scripts/prediction_models")

    def pred1():
        from price_pred_1 import Price_Predictor1
        xg_re1, preds1, y_test1 = pp1.xgb_fun1()
        pp1 = Price_Predictor1()
        return pp1, xg_re1, preds1, y_test1
    
    def pred2():
        from price_pred_2 import Price_Predictor2
        pp2 = Price_Predictor2()
        xg_re2, preds2, y_test2 = pp2.xgb_fun2()
        return pp2, xg_re2, preds2, y_test2


    def pred3():
        from price_pred_3 import Price_Predictor3
        pp3 = Price_Predictor3()
        xg_re3, preds3, y_test3 = pp3.xgb_fun3()
        return pp3, xg_re3, preds3, y_test3


    def pred4():
        from price_pred_4 import Price_Predictor4
        pp4 = Price_Predictor4()
        xg_re4, preds4, y_test4 = pp4.xgb_fun4()
        return pp4, xg_re4, preds4, y_test4


    def pred5():
        from price_pred_5 import Price_Predictor5
        pp5 = Price_Predictor5()
        xg_re5, preds5, y_test5 = pp5.xgb_fun5()
        return pp5, xg_re5, preds5, y_test5


    def pred6():
        from price_pred_6 import Price_Predictor6
        pp6 = Price_Predictor6()
        xg_re6, preds6, y_test6 = pp6.xgb_fun6()
        return pp6, xg_re6, preds6, y_test6

train = Train()
pp1, xg_re1, preds1, y_test1=train.pred1()
pp2, xg_re2, preds2, y_test2=train.pred2()
pp3, xg_re3, preds3, y_test3=train.pred3()
pp4, xg_re4, preds4, y_test4=train.pred4()
pp5, xg_re5, preds5, y_test5=train.pred5()
pp6, xg_re6, preds6, y_test6=train.pred6()