# import python modules required

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys

# read in the cleaned data

df = pd.read_csv('datasets/cleaned_dataset/cleaned_car_data.csv')
df.columns = ['car', 'disp', 'cyl', 'mil', 'fuel', 'fuel_t', 'hei', 'leng', 'wid', 'body_t', 'doors', 'powe', 'tor', 'seat_c', 'wheel', 'price', 'bts']

# get variables from the server

budget = int(sys.argv[1])
body_t = int(sys.argv[2])
disp = float(sys.argv[3])
mil = float(sys.argv[4])
fuel = float(sys.argv[5])
powe = float(sys.argv[6])
tor = float(sys.argv[7])
price = float(sys.argv[8])

p1=1000000
p2=3500000
p3=5000000
p4=7500000
p5=10000000

# lower limit in the customer segment price range
def lower_l (df, price): 
    # print(df[(df['price'] > price)])
    return df[(df['price'] > price)]
# upper limit in the customer segment price range   
def upper_l (df, price):
    return df[(df['price'] < price)]


#calculates the percentages and generates graph
def val_ret(df, disp, mil, fuel, powe, tor):
    num = df[df['disp']<disp].count()['disp']
    den = df['disp'].count()
    if den!=0 or num!=0:
        per = (num/den)*100
        disp_per = per
    else:
        disp_per = 0

    #  df_s= df.sort_values('disp')
    #  plots the graph on top of each other and exports it
    fig=go.Figure()

    fig.add_trace(
    go.Scatter(
        mode='markers',
        x=df['disp'],
        y=df['price'],
        marker=dict(
            color='green',
            size=8,
            line=dict(
                color='Black',
                width=1
            )
        ),
        showlegend=False
    ))

    fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[disp],
        y=[price],
        marker=dict(
            color='Red',
            size=12,
            line=dict(
                color='Black',
                width=2
            )
        ),
        showlegend=False
    ))
    
    
    fig.update_layout(
    title="Price vs Displacement for given customer segment",
    xaxis_title="Displacement in cc",
    yaxis_title="Price",
    font=dict(size=18)
    )

    fig.write_html('public/graphs/graph1.html')
    print(float(np.round(disp_per, 2)))
    sys.stdout.flush()



    # num = df[df['disp']<disp and df['body_t']==body_t].count()['disp']
    # den = df[df['body_t'==body_t]].count()['body_t']
    # if den!=0 or num!=0:
    #     per = (num/den)*100
    #     disp_b_per = per
    # else:
    #     disp_b_per = 0

    # #  df_s= df.sort_values('disp')
    # #  plots the graph on top of each other and exports it
    # fig=go.Figure()
    # fig.add_trace(
    # go.Scatter(
    #     mode='markers',
    #     x=df['disp'],
    #     y=df['price'],
    #     marker=dict(
    #         color='green',
    #         size=8,
    #         line=dict(
    #             color='Black',
    #             width=1
    #         )
    #     ),
    #     showlegend=False
    # ))
    # fig.add_trace(
    # go.Scatter(
    #     mode='markers',
    #     x=[disp],
    #     y=[price],
    #     marker=dict(
    #         color='Red',
    #         size=12,
    #         line=dict(
    #             color='Black',
    #             width=2
    #         )
    #     ),
    #     showlegend=False
    # ))
    # fig.update_layout(
    # title="Price vs Displacement for given customer segment",
    # xaxis_title="Displacement in cc",
    # yaxis_title="Price",
    # font=dict(size=18)
    # )
    # fig.write_html('public/graphs/graph1.html')
    # print(float(np.round(disp_per, 2)))
    # sys.stdout.flush()






    
    num = df[df['mil']<mil].count()['mil']
    den = df['mil'].count()
    if den!=0 or num!=0:
        per = (num/den)*100
        mil_per = per
    else:
        mil_per = 0

    # df_s = df.sort_values('mil')
    
    fig=go.Figure()
    
    fig.add_trace(
    go.Scatter(
        mode='markers',
        x=df['mil'],
        y=df['price'],
        marker=dict(
            color='green',
            size=8,
            line=dict(
                color='Black',
                width=1
            )
        ),
        showlegend=False
    ))
    
    fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[mil],
        y=[price],
        marker=dict(
            color='Red',
            size=12,
            line=dict(
                color='Black',
                width=2
            )
        ),
        showlegend=False
    ))
    
    fig.update_layout(
    title="Price vs Mileage for given customer segment",
    xaxis_title="Mileage in KM/L",
    yaxis_title="Price",
    font=dict(size=18)
    )


    fig.write_html('public/graphs/graph2.html')

    print(float(np.round(mil_per, 2)))
    sys.stdout.flush()
    
    num = df[df['fuel']<fuel].count()['fuel']
    den = df['fuel'].count()
    if den!=0 or num!=0:
        per = (num/den)*100
        fuel_per = per
    else:
        fuel_per = 0

    # df_s = df.sort_values('fuel')
    
    fig=go.Figure()

    
    fig.add_trace(
    go.Scatter(
        mode='markers',
        x=df['fuel'],
        y=df['price'],
        marker=dict(
            color='green',
            size=8,
            line=dict(
                color='Black',
                width=1
            )
        ),
        showlegend=False
    ))

    fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[fuel],
        y=[price],
        marker=dict(
            color='Red',
            size=12,
            line=dict(
                color='Black',
                width=2
            )
        ),
        showlegend=False
    ))
    
    
    fig.update_layout(
    title="Price vs Fuel Tank Capacity for given price segment",
    xaxis_title="Fuel Tank Capacity in L",
    yaxis_title="Price",
    font=dict(size=18)
    )


    fig.write_html('public/graphs/graph3.html')

    print(float(np.round(fuel_per, 2)))
    sys.stdout.flush()
    
    num = df[df['powe']<powe].count()['powe']
    den = df['powe'].count()
    if den!=0 or num!=0:
        per = (num/den)*100
        powe_per = per
    else:
        powe_per = 0

    # df_s = df.sort_values('powe')
    
    fig=go.Figure()
    
    fig.add_trace(
    go.Scatter(
        mode='markers',
        x=df['powe'],
        y=df['price'],
        marker=dict(
            color='green',
            size=8,
            line=dict(
                color='Black',
                width=1
            )
        ),
        showlegend=False
    ))

    fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[powe],
        y=[price],
        marker=dict(
            color='Red',
            size=12,
            line=dict(
                color='Black',
                width=2
            )
        ),
        showlegend=False
    ))
    
    fig.update_layout(
    title="Price vs Power for given customer segment",
    xaxis_title="Power in Brake Horsepower",
    yaxis_title="Price",
    font=dict(size=18)
    )


    fig.write_html('public/graphs/graph4.html')
    print(float(np.round(powe_per, 2)))
    sys.stdout.flush()
    
    num = df[df['tor']<tor].count()['tor']
    den = df['tor'].count()
    if den!=0 or num!=0:
        per = (num/den)*100
        tor_per = per
    else:
        tor_per = 0

    # df_s = df.sort_values('tor')
    
    fig=go.Figure()

    fig.add_trace(
    go.Scatter(
        mode='markers',
        x=df['tor'],
        y=df['price'],
        marker=dict(
            color='green',
            size=8,
            line=dict(
                color='Black',
                width=1
            )
        ),
        showlegend=False
    ))

    fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[tor],
        y=[price],
        marker=dict(
            color='Red',
            size=12,
            line=dict(
                color='Black',
                width=2
            )
        ),
        showlegend=False
    ))
    
    
    fig.update_layout(
    title="Price vs Torque for given price segment",
    xaxis_title="Torque in Nm",
    yaxis_title="Price",
    font=dict(size=18)
    )


    fig.write_html('public/graphs/graph5.html')

    print(float(np.round(tor_per, 2)))
    sys.stdout.flush()
    
    return

if budget==1:
    
    df_1 = upper_l(df, p1)
    val_ret(df_1, disp, mil, fuel, powe, tor)
            
elif budget == 2:
    
    df_u = upper_l(df, p2)
    df_1 = lower_l(df_u, p1)
    val_ret(df_1, disp, mil, fuel, powe, tor)
        
   
elif budget ==3:
    
    df_u = upper_l(df, p3)
    df_1 = lower_l(df_u, p2)
    val_ret(df_1, disp, mil, fuel, powe, tor)

elif budget==4:

    df_u = upper_l(df, p4)
    df_1 = lower_l(df_u, p3)
    val_ret(df_1, disp, mil, fuel, powe, tor)

elif budget==5:
    
    df_u = upper_l(df, p5)
    df_1 = lower_l(df_u, p4)
    val_ret(df_1, disp, mil, fuel, powe, tor)
            
else :

    df_1 = lower_l(df, p5)
    val_ret(df_1, disp, mil, fuel, powe, tor)
        
    

# In[17]:


# budget = sys.argv[1]
# body_t = sys.argv[1]
# disp = sys.argv[1]
# cyl = sys.argv[1]
# mil = sys.argv[1]
# fuel = sys.argv[1]
# fuel_t = sys.argv[1]
# hei = sys.argv[1]
# leng = sys.argv[1]
# wid = sys.argv[1]
# doors = sys.argv[1]
# powe = sys.argv[1]
# tor = sys.argv[1]
# seat_c = sys.argv[1]
# wheel = sys.argv[1]
# price = sys.argv[1]


# In[ ]:


# import pandas as pd
# import plotly.express as px
# import sys

# df = pd.read_csv('datasets/cleaned_dataset/cleaned_Car_data')
# price = sys.argv[1]
# body_t = sys.argv[2]


# fig =px.scatter(x=range(10), y=range(10))
# fig.write_html("public/graphs/graph1.html")

