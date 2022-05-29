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

class Price_Predictor1:
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
        
    def input_params1(self, disp, fuel, fuel_t, leng, body_t, door, powe, wheel):
        self.disp = disp  
        self.fuel = fuel
        self.fuel_t = fuel_t
        self.leng = leng 
        self.body_t = body_t
        self.door = door
        self.powe = powe
        self.wheel = wheel
        return
        
    def xgb_fun1(self):
        df = pd.read_csv('datasets/cleaned_dataset/cleaned_car_data.csv')
        df = df[df['price']<1000000]
        X = df[['displacement', 'fuel_capacity', 'fuel_type', 'length', 'body_type', 
                'doors', 'power', 'wheelbase']]
        y = df['price']
        # 'displacement', 'mileage', 'fuel_capacity', 'height', 'length', 'width', 'power', 
        data_dmatrix = xgb.DMatrix(data=X,label=y)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        
        xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3,
                                  learning_rate = 0.1, max_depth = 4, alpha = 10, n_estimators = 150)
        
        params = {"objective":"reg:squarederror",'colsample_bytree': 0.1,'learning_rate': 0.1, 'max_depth': 3, 'alpha': 10}
        cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=5, num_boost_round=700,early_stopping_rounds=50,metrics="rmse", as_pandas=True, seed=0)
        
        xg_reg.fit(X_train,y_train)
        preds = xg_reg.predict(X_test)
        
        return xg_reg, preds, y_test
    
    def predict1(self, xg_reg):
        Y_pred = (xg_reg.predict(np.array([
        self.disp,     
        self.fuel, 
        self.fuel_t,    
        self.leng,
        self.body_t,
        self.door,
        self.powe,
        self.wheel
        ]).reshape(1, 8))).astype(float)
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


# In[1104]:


# pred = Price_Predictor1()


# In[1105]:


# xg_reg, preds, y_test = pred.xgb_fun1()
# print(pred.error_calc(y_test, preds))


# In[1107]:


# pred.input_params1(999, 28.0, 1, 3429.0, 1, 5, 67.07, 2348)
# y_pred = pred.predict1(xg_reg)
# print(y_pred)


# In[ ]:





# In[19]:


# def xgb_fun() :
#     xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.5, learning_rate = 0.1,
#                 max_depth = 3, alpha = 2, n_estimators = 3200)

#     params = {"objective":"reg:squarederror",'colsample_bytree': 0.9,'learning_rate': 0.1,
#                 'max_depth': 2, 'alpha': 10}


#     cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=5,
#                     num_boost_round=700,early_stopping_rounds=50,metrics="rmse", as_pandas=True, seed=123)

#     xg_reg.fit(X_train,y_train)
#     preds = xg_reg.predict(X_test)
#     return xg_reg


# In[2]:


# df = pd.read_csv('datasets/cleaned_dataset/cleaned_car_data.csv')


# In[3]:


# X = df[['displacement', 'mileage', 'fuel_capacity', 'height', 'length', 'width', 'power', 'torque']]
# y = df['price']
# # , 'wheelbase'


# In[4]:


# data_dmatrix = xgb.DMatrix(data=X,label=y)


# In[5]:


# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)


# In[1099]:


# xg_reg = xgb_fun()

# xg_reg.get_booster().get_score(importance_type= 'gain')


# In[1100]:


# a= np.array([117286240256.0,117242363904.0,63769423872.0,36270477312.0,78674208.0,70447013888.0,209886085120.0,108671131648.0,42502680576.0,26573662208.0,335653371904.0,49569976320.0,5582825984.0,78811676672.0])
# print(np.sort(a))


# In[1102]:





# In[21]:


# Y_pred = xg_reg.predict(np.array([1998, 14.82, 68.0, 1467.0, 4963.0, 1868.0, 251.43, 350]).reshape(1, 8))


# In[22]:


# print(Y_pred)


# In[ ]:


# class Price_Predictor:
#     def __init__(self):
#         self.disp = 0
#         self.mil = 0.0      
#         self.fuel = 0.0 
#         self.hei = 0.0 
#         self.wid = 0.0     
#         self.leng = 0.0     
#         self.powe = 0.0
#         self.tor = 0.0
#         self.seat = 0
#         self.door = 0
#         return
        
#     def input_params(self, disp, mil, fuel, hei, wid, leng, powe, tor, seat, door):
#         self.disp = disp
#         self.mil = mil   
#         self.fuel = fuel
#         self.hei = hei 
#         self.wid = wid  
#         self.leng = leng 
#         self.powe = powe
#         self.tor = tor 
#         self.seat = seat
#         self.door = door
#         return
    
    # self.cyl,
    #     self.mil,      
    #     self.fuel, 
    #     self.fuel_t,
    #     self.hei,
    #     self.wid,     
    #     self.leng,
    #     self.body_t,
    #     self.door,
    #     self.powe,
    #     self.tor,
    #     self.seat,
    #     self.wheel
    
    # 'displacement', 'cylinders', 'mileage', 'fuel_capacity', 'fuel_type', 'height', 'length', 'width', 'body_type', 'doors', 'power', 'torque', 'seating_capacity', 'wheelbase'


# In[ ]:




