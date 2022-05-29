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

class Price_Predictor3:
    def __init__(self):
        self.disp = 0      
        self.fuel = 0.0 
        self.fuel_t = 0    
        self.leng = 0.0 
        self.body_t = 0.0  
        self.door = 0
        self.powe = 0.0
        self.wheel=0
        return
        
    def input_params3(self, disp, mil, fuel, hei, wid, body_t, powe, tor, wheel):
        self.disp = disp 
        self.mil = mil
        self.fuel = fuel
        self.hei = hei
        self.wid = wid 
        self.body_t = body_t
        self.powe = powe
        self.tor = tor
        self.wheel = wheel
        return
        
    def xgb_fun3(self):
        df = pd.read_csv('datasets/cleaned_dataset/cleaned_car_data.csv')
        df = df.loc[(df['price']>=3500000) & (df['price']<5000000)]
        X = df[['displacement', 'mileage', 'fuel_capacity', 'height', 'width', 'body_type', 
               'power', 'torque', 'wheelbase']]
        y = df['price']
        # 'displacement', 'mileage', 'fuel_capacity', 'height', 'length', 'width', 'power', 
        data_dmatrix = xgb.DMatrix(data=X,label=y)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        
        xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.1,
                                  learning_rate = 0.1, max_depth = 3, alpha = 1, n_estimators = 600)
        
        params = {"objective":"reg:squarederror",'colsample_bytree': 0.1,'learning_rate': 0.1, 'max_depth': 3, 'alpha': 10}
        cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=5, num_boost_round=700,early_stopping_rounds=50,metrics="rmse", as_pandas=True, seed=0)
        
        xg_reg.fit(X_train,y_train)
        preds = xg_reg.predict(X_test)
        
        return xg_reg, preds, y_test
    
    def predict3(self, xg_reg):
        Y_pred = (xg_reg.predict(np.array([
        self.disp,  
        self.mil,
        self.fuel,
        self.hei,
        self.wid, 
        self.body_t,
        self.powe,
        self.tor,
        self.wheel
        ]).reshape(1, 9))).astype(float)
        return Y_pred
    
    def error_calc(self, y_test, preds):
        
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        return rmse
    
    def plot_imp(self, xg_reg):
        
        xgb.plot_importance(xg_reg)
        plt.figure(figsize = (16, 12))
        plt.show()
        return

    def gain(self, xg_reg):
        gain_param = xg_reg.get_booster().get_score(importance_type= 'gain')
        print(gain_param)

        list_p = np.array(list(gain_param.values()))
        print(np.sort(list_p))
    
    
###############-------END OF USEFUL CODE--------######################

    
# pred = Price_Predictor3()


# In[72]:


# xg_reg, preds, y_test = pred.xgb_fun3()
# print(pred.error_calc(y_test, preds))


# In[79]:


# pred.input_params3(1995, 19.62, 40.0, 1429.0, 1811.0, 5, 187.4, 400, 2810)
# y_pred = pred.predict3(xg_reg)
# print(y_pred)


# In[26]:


# gain_param = xg_reg.get_booster().get_score(importance_type= 'gain')
# gain_param 


# In[27]:


# list_p = np.array(list(gain_param.values()))
# print(np.sort(list_p))


# In[73]:


# xgb.plot_importance(xg_reg)
# plt.figure(figsize = (16, 12))
# plt.show()


# In[ ]:




