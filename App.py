# import python modules

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
# import seaborn as sns
# from IPython.display import clear_output
import sys
# %matplotlib inline
# sns.set_style('darkgrid')

# import the training classes

sys.path.insert(0,"scripts/prediction_models")
from price_pred_1 import Price_Predictor1
from price_pred_2 import Price_Predictor2
from price_pred_3 import Price_Predictor3
from price_pred_4 import Price_Predictor4
from price_pred_5 import Price_Predictor5
from price_pred_6 import Price_Predictor6

pp1 = Price_Predictor1()
pp2 = Price_Predictor2()
pp3 = Price_Predictor3()
pp4 = Price_Predictor4()
pp5 = Price_Predictor5()
pp6 = Price_Predictor6()


# get the variables
budget=int(sys.argv[1])
body_t=int(sys.argv[2])
disp=float(sys.argv[3])
mil=float(sys.argv[5])
fuel=float(sys.argv[6])
fuel_t=int(sys.argv[7])
hei=float(sys.argv[8])
leng=float(sys.argv[9])   
wid=float(sys.argv[10])
doors=int(sys.argv[11])
powe=float(sys.argv[12])
powe=powe*0.986
tor=float(sys.argv[13])
seat_c = int(sys.argv[14])
wheel=float(sys.argv[15])

y_pred_f=0.0

if (budget == 1):
 
    xg_reg1, preds1, y_test1 = pp1.xgb_fun1()
    pp1.input_params1(disp, fuel, fuel_t, leng, body_t, doors, powe, wheel)
    y_pred =pp1.predict1(xg_reg1)
    y_pred_f = float(np.round(y_pred, 2))
    print(y_pred_f)

elif(budget == 2):

    xg_reg2, preds2, y_test2 = pp2.xgb_fun2()
    pp2.input_params2(disp, mil, fuel, hei, wid, body_t, powe, tor, wheel)
    y_pred =pp2.predict2(xg_reg2)
    y_pred_f = float(np.round(y_pred, 2))
    print(y_pred_f)

elif (budget == 3):
 
    xg_reg3, preds3, y_test3 = pp3.xgb_fun3()
    pp3.input_params3(disp, mil, fuel, hei, wid, body_t, powe, tor, wheel)
    y_pred =pp3.predict3(xg_reg3)
    y_pred_f = float(np.round(y_pred, 2))
    print(y_pred_f)

elif (budget == 4):
 
    xg_reg4, preds4, y_test4 = pp4.xgb_fun4()
    pp4.input_params4(disp, mil, fuel, hei, leng, wid, powe, tor, seat_c, wheel)
    y_pred =pp4.predict4(xg_reg4)
    y_pred_f = float(np.round(y_pred, 2))
    print(y_pred_f)

elif (budget == 5):
 
    xg_reg5, preds5, y_test5 = pp5.xgb_fun5()
    pp5.input_params5(disp, mil, fuel, hei, leng, wid, powe, tor)
    y_pred =pp5.predict5(xg_reg5)
    y_pred_f = float(np.round(y_pred, 2))
    print(y_pred_f)

elif (budget == 6):
 
    xg_reg6, preds6, y_test6 = pp6.xgb_fun6()
    pp6.input_params6(disp, mil, fuel, hei, leng, wid, powe, tor, seat_c, wheel)
    y_pred =pp6.predict6(xg_reg6)
    y_pred_f = float(np.round(y_pred, 2))
    print(y_pred_f)