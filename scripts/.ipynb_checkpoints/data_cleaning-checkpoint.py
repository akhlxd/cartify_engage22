#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style('darkgrid')

class Cleaner:
    
    def __init__(self):{}
    
    def cleaner(self):
        
        df.self = pd.read_csv('../datasets/raw_datasets/cars_engage_2022.csv', index_col=0)

        df.self = df.self[df.self['Cylinders'].notna()]
        df.self = df.self[df.self['ARAI_Certified_Mileage'].notna()]
        df.self = df.self[df.self['Displacement'].notna()]
        df.self = df.self[df.self['Fuel_System'].notna()]
        df.self = df.self[df.self['Wheelbase'].notna()]
        df.self = df.self[df.self['Width'].notna()]
        df.self = df.self[df.self['Fuel_Tank_Capacity'].notna()]
        df.self = df.self[df.self['Wheelbase'].notna()]

        df.self.loc[(df.self['Model'].str[:4]).eq('Merc'), 'Make'] = 'Mercedes'
        df.self.loc[(df.self['Model'].str[:3]).eq('Go+'), 'Make'] = 'Datsun'
        df.self.loc[(df.self['Model'].str[:4]).eq('Roll'), 'Make'] = 'Rolls-Royce'

        df.self.loc[(df.self['Model'].str[:4]).eq('Merc'), 'Model'] = df.self['Model'].str[9:]
        df.self.loc[(df.self['Model'].str[:3]).eq('Go+'), 'Model'] = 'Datsun'
        df.self.loc[(df.self['Model'].str[:4]).eq('Roll'), 'Model'] = df.self['Model'].str[12:]

        df.self['Ex-Showroom_Price'] = df.self['Ex-Showroom_Price'].str.replace('Rs. ','',regex=False)
        df.self['Ex-Showroom_Price'] = df.self['Ex-Showroom_Price'].str.replace(',','',regex=False)
        df.self['Ex-Showroom_Price'] = df.self['Ex-Showroom_Price'].astype(int)

        df.self['Wheelbase'] = df.self['Wheelbase'].str.replace(' mm','',regex=False)
        df.self['Wheelbase'] = df.self['Wheelbase'].astype(int)

        df.self.insert(4, "Car", df.self.Make + ' ' + df.self.Model + ' ' + df.self.Variant, False)

        df.self.loc[(df.self['Car']) == ('Mahindra Alturas G4 2Wd At'), 'Body_Type'] = 'SUV'
        df.self.loc[(df.self['Car']) == ('Maserati Ghibli Gransport'), 'Body_Type'] = 'Sedan, Crossover'
        df.self.loc[(df.self['Car']) == ('Maserati Ghibli Granlusso'), 'Body_Type'] = 'Sedan, Crossover'
        df.self.loc[(df.self['Car']) == ('Porsche Cayenne Coupe Base'), 'Body_Type'] = 'Sedan, Coupe'
        df.self.loc[(df.self['Car']) == ('Porsche Cayenne Coupe Turbo'), 'Body_Type'] = 'Sedan, Coupe'
        df.self.loc[(df.self['Car']) == ('Maserati Ghibli Diesel'), 'Body_Type'] = 'Sedan, Crossover'

        bts = []
        for car in df.self['Body_Type']:
            c=car.split()
            if (len(c)==2):
                bts.append(c[0][:3]+','+c[1][:3])
            else:
                bts.append(car[:3])
        df.self['bts']=bts

        useful_columns = ['Make', 'Model', 'Variant', 'Car', 'Ex-Showroom_Price', 'Displacement', 'Cylinders', 'ARAI_Certified_Mileage', 'Fuel_Tank_Capacity', 'Fuel_Type', 'Height', 'Length', 'Width', 'Body_Type', 'Doors', 'Power', 'Torque', 'Seating_Capacity', 'Wheelbase', 'bts' ]

        df.self = df.self[useful_columns]

        df.self.drop(df.self[df.self['Fuel_Type'].ne('Petrol') & df.self['Fuel_Type'].ne('Diesel')].index, inplace = True)


        df.self.loc[df.self.ARAI_Certified_Mileage == '9.8-10.0 km/litre','ARAI_Certified_Mileage'] = '10'
        df.self.loc[df.self.ARAI_Certified_Mileage == '10kmpl km/litre','ARAI_Certified_Mileage'] = '10'
        df.self.loc[df.self.ARAI_Certified_Mileage == '22.4-21.9 km/litre','ARAI_Certified_Mileage'] = '22'

        df.self['ARAI_Certified_Mileage'] = df.self['ARAI_Certified_Mileage'].str.replace(' km/litre','',regex=False).astype(float)

        df.self.loc[(df.self['Model']).eq('Benz Amg Gt 4-Door Coupe') & (df.self['Make']).eq('Mercedes'), 'Displacement'] = int(3998)
        df.self.loc[(df.self['Model']).eq('Benz Amg Gt 4-Door Coupe') & (df.self['Make']).eq('Mercedes'), 'Displacement'] = int(3982)
        df.self['Displacement'] = df.self['Displacement'].str.replace(' cc','',regex=False)

        
        df.self.loc[(df.self['Car']).eq('Mahindra Alturas G4 2Wd At'), 'Doors'] = int(5)
        df.self.loc[(df.self['Car']).eq('Volkswagen Tiguan Highline 2.0L Tdi Amt'), 'Doors'] = int(4)
        df.self.loc[(df.self['Car']).eq('Porsche Cayenne Coupe Base'), 'Doors'] = int(4)
        df.self.loc[(df.self['Car']).eq('Porsche Cayenne Coupe Turbo'), 'Doors'] = int(4)

        df.self.loc[(df.self['Car']).eq('Mahindra Bolero Power Plus Plus Ac Bs4 Ps'), 'Torque'] = '180Nm@1440rpm'
        df.self.loc[(df.self['Car']).eq('Bmw 6-Series 630I Gt Luxury Line'), 'Torque'] = '400Nm@1550rpm'


        df.self.loc[(df.self['Car']).eq('Mahindra Alturas G4 2Wd At'), 'Seating_Capacity'] = float(7.0)
        df.self.loc[(df.self['Car']).eq('Volkswagen Tiguan Highline 2.0L Tdi Amt'), 'Seating_Capacity'] = float(5.0)
        df.self.loc[(df.self['Car']).eq('Renault Lodgy Stepway Rxz 110Ps 8-Seater'), 'Seating_Capacity'] = float(8.0)
        df.self.loc[(df.self['Car']).eq('Porsche Cayenne Coupe Base'), 'Seating_Capacity'] = float(4.0)
        df.self.loc[(df.self['Car']).eq('Porsche Cayenne Coupe Turbo'), 'Seating_Capacity'] = float(4.0)


        df.self.loc[(df.self['Car']).eq('Mercedes Benz C-Class C 43 Amg'), 'ARAI_Certified_Mileage'] = float(14.49)
        df.self.loc[(df.self['Car']).eq('Mercedes Benz E-Class E350 D'), 'ARAI_Certified_Mileage'] = float(14.2)
        df.self.loc[(df.self['Car']).eq('Mercedes Benz E-Class E220D'), 'ARAI_Certified_Mileage'] = float(14.2)
        df.self.loc[(df.self['Car']).eq('Mercedes Benz E-Class E220D Expression'), 'ARAI_Certified_Mileage'] = float(14.2)
        df.self.loc[(df.self['Car']).eq('Mercedes Benz E-Class E220D Exclusive'), 'ARAI_Certified_Mileage'] = float(14.2)


        HP = df.self.Power.str.extract(r'(\d{1,4}).*').astype(int) * 0.98632
        HP = HP.apply(lambda x: round(x,2))
        TQ = df.self.Torque.str.extract(r'(\d{1,4}).*').astype(int)
        TQ = TQ.apply(lambda x: round(x,2))
        df.self.Torque = TQ
        df.self.Power = HP

        df.self['Cylinders'] = df.self['Cylinders'].astype(int)
        df.self['Doors'] = df.self['Doors'].astype(int)
        df.self['Seating_Capacity'] = df.self['Seating_Capacity'].astype(int)

        df.self['Height'] = df.self['Height'].str.replace(' mm','',regex=False).astype(float)
        df.self['Length'] = df.self['Length'].str.replace(' mm','',regex=False).astype(float)
        df.self['Width'] = df.self['Width'].str.replace(' mm','',regex=False).astype(float)
        df.self['Fuel_Tank_Capacity'] = df.self['Fuel_Tank_Capacity'].str.replace(' litres','',regex=False).astype(float)

        df.self.rename(columns = {'Ex-Showroom_Price':'price'}, inplace = True)
        df.self= df.self[df.self['Car'].ne('Bugatti Chiron W16') & df.self['Car'].ne('Bugatti Chiron Sport')]


        df.self.loc[(df.self['Body_Type']) == ('Hatchback'), 'Body_Type'] = int(1)
        df.self.loc[(df.self['Body_Type']) == ('MPV'), 'Body_Type'] = int(2)
        df.self.loc[(df.self['Body_Type']) == ('MUV'), 'Body_Type'] = int(3)
        df.self.loc[(df.self['Body_Type']) == ('SUV'), 'Body_Type'] = int(4)
        df.self.loc[(df.self['Body_Type']) == ('Sedan'), 'Body_Type'] = int(5)
        df.self.loc[(df.self['Body_Type']) == ('Crossover'), 'Body_Type'] = int(6)
        df.self.loc[(df.self['Body_Type']) == ('Coupe'), 'Body_Type'] = int(7)
        df.self.loc[(df.self['Body_Type']) == ('Sports, Hatchback'), 'Body_Type'] = int(8)
        df.self.loc[(df.self['Body_Type']) == ('Convertible'), 'Body_Type'] = int(9)
        df.self.loc[(df.self['Body_Type']) == ('Sedan, Coupe'), 'Body_Type'] = int(10)
        df.self.loc[(df.self['Body_Type']) == ('Sports'), 'Body_Type'] = int(11)
        df.self.loc[(df.self['Body_Type']) == ('Crossover, SUV'), 'Body_Type'] = int(12)
        df.self.loc[(df.self['Body_Type']) == ('SUV, Crossover'), 'Body_Type'] = int(13)
        df.self.loc[(df.self['Body_Type']) == ('Sedan, Crossover'), 'Body_Type'] = int(14)
        df.self.loc[(df.self['Body_Type']) == ('Sports, Convertible'), 'Body_Type'] = int(15)
        df.self.loc[(df.self['Body_Type']) == ('Coupe, Convertible'), 'Body_Type'] = int(16)

        df.self.loc[(df.self['Fuel_Type']) == ('Petrol'), 'Fuel_Type'] = int(1)
        df.self.loc[(df.self['Fuel_Type']) == ('Diesel'), 'Fuel_Type'] = int(2)

        df.self.columns = ['make', 'model', 'variant', 'car', 'price', 'displacement', 'cylinders', 'mileage', 'fuel_capacity', 'fuel_type', 'height', 'length', 'width', 'body_type', 'doors', 'power', 'torque', 'seating_capacity', 'wheelbase', 'bts']

        df.self.drop(['make', 'model', 'variant', 'car', 'bts'], axis=1, inplace=True)
        df.self.insert(15, "Price", df.self.price, False)
        df.self.drop('price', axis=1, inplace=True)
        df.self.rename(columns = {'Price':'price'}, inplace = True)

        df.self.reset_index(drop=True, inplace=True)
        df.self.to_csv('../datasets/cleaned_dataset/cleaned_car_data.csv', index=False)


# for col in df.self.columns:
#     print(f'{col} : {df.self[col].isna().sum()}')


# # In[34]:


# df.self.shape


# # In[35]:


# (df.self.loc[(df.self['price']<1000000)]).shape


# # In[36]:


# (df.self.loc[df.self['price']>=5000000]).shape


# # In[37]:


# df.self.loc[(df.self['price']>=7500000) & (df.self['price']<10000000)].shape


# # In[38]:


# df.self.loc[(df.self['price']>=10000000)].shape


# # In[ ]:




