import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style('darkgrid')

pd.set_option('display.max_columns', None)

df = pd.read_csv('../datasets/raw_datasets/cars_engage_2022.csv', index_col=0)

df = df[df['Cylinders'].notna()]
df = df[df['ARAI_Certified_Mileage'].notna()]
df = df[df['Displacement'].notna()]
df = df[df['Fuel_System'].notna()]
df = df[df['Wheelbase'].notna()]
df = df[df['Width'].notna()]
df = df[df['Fuel_Tank_Capacity'].notna()]
df = df[df['Wheelbase'].notna()]

df.loc[(df['Model'].str[:4]).eq('Merc'), 'Make'] = 'Mercedes'
df.loc[(df['Model'].str[:3]).eq('Go+'), 'Make'] = 'Datsun'
df.loc[(df['Model'].str[:4]).eq('Roll'), 'Make'] = 'Rolls-Royce'

df.loc[(df['Model'].str[:4]).eq('Merc'), 'Model'] = df['Model'].str[9:]
df.loc[(df['Model'].str[:3]).eq('Go+'), 'Model'] = 'Datsun'
df.loc[(df['Model'].str[:4]).eq('Roll'), 'Model'] = df['Model'].str[12:]

df['Ex-Showroom_Price'] = df['Ex-Showroom_Price'].str.replace('Rs. ','',regex=False)
df['Ex-Showroom_Price'] = df['Ex-Showroom_Price'].str.replace(',','',regex=False)
df['Ex-Showroom_Price'] = df['Ex-Showroom_Price'].astype(int)

df['Wheelbase'] = df['Wheelbase'].str.replace(' mm','',regex=False)
df['Wheelbase'] = df['Wheelbase'].astype(int)

df.insert(4, "Car", df.Make + ' ' + df.Model + ' ' + df.Variant, False)

df.loc[(df['Car']) == ('Mahindra Alturas G4 2Wd At'), 'Body_Type'] = 'SUV'
df.loc[(df['Car']) == ('Maserati Ghibli Gransport'), 'Body_Type'] = 'Sedan, Crossover'
df.loc[(df['Car']) == ('Maserati Ghibli Granlusso'), 'Body_Type'] = 'Sedan, Crossover'
df.loc[(df['Car']) == ('Porsche Cayenne Coupe Base'), 'Body_Type'] = 'Sedan, Coupe'
df.loc[(df['Car']) == ('Porsche Cayenne Coupe Turbo'), 'Body_Type'] = 'Sedan, Coupe'
df.loc[(df['Car']) == ('Maserati Ghibli Diesel'), 'Body_Type'] = 'Sedan, Crossover'

bts = []
for car in df['Body_Type']:
    c=car.split()
    if (len(c)==2):
        bts.append(c[0][:3]+','+c[1][:3])
    else:
        bts.append(car[:3])
df['bts']=bts

useful_columns = ['Make', 'Model', 'Variant', 'Car', 'Ex-Showroom_Price', 'Displacement', 'Cylinders', 'ARAI_Certified_Mileage', 'Fuel_Tank_Capacity', 'Fuel_Type', 'Height', 'Length', 'Width', 'Body_Type', 'Doors', 'Power', 'Torque', 'Seating_Capacity', 'Wheelbase', 'bts' ]

df = df[useful_columns]


# price_df.set_index('Car', inplace=True)

# df.sort_values(by=['Ex-Showroom_Price'], inplace=True)

df.drop(df[df['Fuel_Type'].ne('Petrol') & df['Fuel_Type'].ne('Diesel')].index, inplace = True)


# df.loc[(df['Start_/_Stop_Button']).isna(), 'Start_/_Stop_Button'] = 'No'
# df.loc[(df['Number_of_Airbags']).isna(), 'Number_of_Airbags'] = int(0)
# df.loc[(df['Parking_Assistance']).isna(), 'Parking_Assistance'] = 'No'
# df.loc[(df['Infotainment_Screen']).isna(), 'Infotainment_Screen'] = 'No'


df.loc[df.ARAI_Certified_Mileage == '9.8-10.0 km/litre','ARAI_Certified_Mileage'] = '10'
df.loc[df.ARAI_Certified_Mileage == '10kmpl km/litre','ARAI_Certified_Mileage'] = '10'
df.loc[df.ARAI_Certified_Mileage == '22.4-21.9 km/litre','ARAI_Certified_Mileage'] = '22'

df['ARAI_Certified_Mileage'] = df['ARAI_Certified_Mileage'].str.replace(' km/litre','',regex=False).astype(float)

df.loc[(df['Model']).eq('Benz Amg Gt 4-Door Coupe') & (df['Make']).eq('Mercedes'), 'Displacement'] = int(3998)
df.loc[(df['Model']).eq('Benz Amg Gt 4-Door Coupe') & (df['Make']).eq('Mercedes'), 'Displacement'] = int(3982)
df['Displacement'] = df['Displacement'].str.replace(' cc','',regex=False)

# df.loc[(df['Car']).eq('Mini Clubman Cooper S'), 'Drivetrain'] = 'FWD (Front Wheel Drive)'
# df.loc[(df['Car']).eq('Mercedes Benz E-Class Cabriolet E400'), 'Drivetrain'] = 'AWD (All Wheel Drive)'
# df.loc[(df['Car']).eq('Tata Nexon Xe'), 'Drivetrain'] = 'FWD (Front Wheel Drive)'

df.loc[(df['Car']).eq('Mahindra Alturas G4 2Wd At'), 'Doors'] = int(5)
df.loc[(df['Car']).eq('Volkswagen Tiguan Highline 2.0L Tdi Amt'), 'Doors'] = int(4)
df.loc[(df['Car']).eq('Porsche Cayenne Coupe Base'), 'Doors'] = int(4)
df.loc[(df['Car']).eq('Porsche Cayenne Coupe Turbo'), 'Doors'] = int(4)

df.loc[(df['Car']).eq('Mahindra Bolero Power Plus Plus Ac Bs4 Ps'), 'Torque'] = '180Nm@1440rpm'
df.loc[(df['Car']).eq('Bmw 6-Series 630I Gt Luxury Line'), 'Torque'] = '400Nm@1550rpm'


df.loc[(df['Car']).eq('Mahindra Alturas G4 2Wd At'), 'Seating_Capacity'] = float(7.0)
df.loc[(df['Car']).eq('Volkswagen Tiguan Highline 2.0L Tdi Amt'), 'Seating_Capacity'] = float(5.0)
df.loc[(df['Car']).eq('Renault Lodgy Stepway Rxz 110Ps 8-Seater'), 'Seating_Capacity'] = float(8.0)
df.loc[(df['Car']).eq('Porsche Cayenne Coupe Base'), 'Seating_Capacity'] = float(4.0)
df.loc[(df['Car']).eq('Porsche Cayenne Coupe Turbo'), 'Seating_Capacity'] = float(4.0)


# df.loc[(df['Car']).eq('Mercedes Benz E-Class Cabriolet E400'), 'Seats_Material'] = 'Leather'
# df.loc[(df['Car']).eq('Rolls-Royce Cullinan Suv'), 'Seats_Material'] = 'Leather'
# df.loc[(df['Car']).eq('Hyundai Venue 1.2 Kappa Mt S'), 'Seats_Material'] = 'Fabric'
# df.loc[(df['Car']).eq('Mg Hector 2.0L Sharp'), 'Seats_Material'] = 'Leather'
# df.loc[(df['Car']).eq('Nissan Kicks Xl Petrol'), 'Seats_Material'] = 'Fabric'


df.loc[(df['Car']).eq('Mercedes Benz C-Class C 43 Amg'), 'ARAI_Certified_Mileage'] = float(14.49)
df.loc[(df['Car']).eq('Mercedes Benz E-Class E350 D'), 'ARAI_Certified_Mileage'] = float(14.2)
df.loc[(df['Car']).eq('Mercedes Benz E-Class E220D'), 'ARAI_Certified_Mileage'] = float(14.2)
df.loc[(df['Car']).eq('Mercedes Benz E-Class E220D Expression'), 'ARAI_Certified_Mileage'] = float(14.2)
df.loc[(df['Car']).eq('Mercedes Benz E-Class E220D Exclusive'), 'ARAI_Certified_Mileage'] = float(14.2)

# df.loc[(df['Car']).eq('Mercedes Benz E-Class Cabriolet E400'), 'Type'] = 'Automatic'


HP = df.Power.str.extract(r'(\d{1,4}).*').astype(int) * 0.98632
HP = HP.apply(lambda x: round(x,2))
TQ = df.Torque.str.extract(r'(\d{1,4}).*').astype(int)
TQ = TQ.apply(lambda x: round(x,2))
df.Torque = TQ
df.Power = HP


df['Cylinders'] = df['Cylinders'].astype(int)
df['Doors'] = df['Doors'].astype(int)
df['Seating_Capacity'] = df['Seating_Capacity'].astype(int)

df['Height'] = df['Height'].str.replace(' mm','',regex=False).astype(float)
df['Length'] = df['Length'].str.replace(' mm','',regex=False).astype(float)
df['Width'] = df['Width'].str.replace(' mm','',regex=False).astype(float)
df['Fuel_Tank_Capacity'] = df['Fuel_Tank_Capacity'].str.replace(' litres','',regex=False).astype(float)


df.rename(columns = {'Ex-Showroom_Price':'price'}, inplace = True)
df= df[df['Car'].ne('Bugatti Chiron W16') & df['Car'].ne('Bugatti Chiron Sport')]


df.loc[(df['Body_Type']) == ('Hatchback'), 'Body_Type'] = int(1)
df.loc[(df['Body_Type']) == ('MPV'), 'Body_Type'] = int(2)
df.loc[(df['Body_Type']) == ('MUV'), 'Body_Type'] = int(3)
df.loc[(df['Body_Type']) == ('SUV'), 'Body_Type'] = int(4)
df.loc[(df['Body_Type']) == ('Sedan'), 'Body_Type'] = int(5)
df.loc[(df['Body_Type']) == ('Crossover'), 'Body_Type'] = int(6)
df.loc[(df['Body_Type']) == ('Coupe'), 'Body_Type'] = int(7)
df.loc[(df['Body_Type']) == ('Sports, Hatchback'), 'Body_Type'] = int(8)
df.loc[(df['Body_Type']) == ('Convertible'), 'Body_Type'] = int(9)
df.loc[(df['Body_Type']) == ('Sedan, Coupe'), 'Body_Type'] = int(10)
df.loc[(df['Body_Type']) == ('Sports'), 'Body_Type'] = int(11)
df.loc[(df['Body_Type']) == ('Crossover, SUV'), 'Body_Type'] = int(12)
df.loc[(df['Body_Type']) == ('SUV, Crossover'), 'Body_Type'] = int(13)
df.loc[(df['Body_Type']) == ('Sedan, Crossover'), 'Body_Type'] = int(14)
df.loc[(df['Body_Type']) == ('Sports, Convertible'), 'Body_Type'] = int(15)
df.loc[(df['Body_Type']) == ('Coupe, Convertible'), 'Body_Type'] = int(16)


df.loc[(df['Fuel_Type']) == ('Petrol'), 'Fuel_Type'] = int(1)
df.loc[(df['Fuel_Type']) == ('Diesel'), 'Fuel_Type'] = int(2)


df.loc[(df['Torque']) == 1712, 'Torque'] = int(172)

df.columns = ['make', 'model', 'variant', 'car', 'price', 'displacement', 'cylinders', 'mileage', 'fuel_capacity', 'fuel_type', 'height', 'length', 'width', 'body_type', 'doors', 'power', 'torque', 'seating_capacity', 'wheelbase', 'bts']

df.drop(['make', 'model', 'variant'], axis=1, inplace=True)
df.insert(16, "Price", df.price, False)
df.drop('price', axis=1, inplace=True)
df.rename(columns = {'Price':'price'}, inplace = True)


df.reset_index(drop=True, inplace=True)
df.to_csv('../datasets/cleaned_dataset/cleaned_car_data.csv', index=False)

# for col in df.columns:
#     print(f'{col} : {df[col].isna().sum()}')
