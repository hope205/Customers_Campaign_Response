# Import libraries
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import PolynomialFeatures



SEED = 123



# this are the features to be selected for feeding into the model

feat= ['Recency', 'year_month', 'Rec_count', 'Cmp3Accepted', 'Cmp5Accepted',
       'Cmp1Accepted', 'WebVisitsMonth', 'Marital_Status', 'wine_frac',
       'Duration_Customer', 'gold_dis', 'No_of_Teen_in_home', 'Web_count',
       'poly2_7', 'poly2_2', 'StorePurchases', 'Disposable_Income', 'poly1_3',
       'months_Dur_Customer', 'poly2_5', 'poly1_7', 'Education_Level',
       'poly2_11', 'total_kids', 'food_dis', 'poly1_9',
       'Amount_on_MeatProducts', 'Cmp4Accepted', 'poly2_17', 'fish_net',
       'poly2_3', 'meat_dis', 'poly1_2', 'poly2_10', 'CatalogPurchases',
       'Amount_on_FishProducts', 'WebPurchases', 'day_of_week_name', 'poly1_8',
       'Amount_on_GoldProds']

  


# this function handles the preoprocessing

def works(data):
    
    # data = pd.DataFrame(data)
    data.drop('ID',1,inplace = True)
    
    data['Date_Customer'] = pd.to_datetime(data['Date_Customer'])

    Today =  pd.to_datetime('2015-1-1')



    # Extract date features
    def extract_date_info(df,cols):
        for feat in cols:
            df[feat +'_year'] = df[feat].dt.year        
            df[feat +'_month'] = df[feat].dt.month
            df[feat +'_weekday'] = df[feat].dt.weekday
            
    

    extract_date_info(data,['Date_Customer'])

    data['Duration_Customer']  = (Today - data['Date_Customer']).dt.days

    data['months_Dur_Customer'] = (Today- data['Date_Customer']) / pd.Timedelta(days=31)
    data['months_Dur_Customer'] = data['months_Dur_Customer'].astype(int)

    dw_mapping={
        0: 'Monday', 
        1: 'Tuesday', 
        2: 'Wednesday', 
        3: 'Thursday', 
        4: 'Friday',
        5: 'Saturday', 
        6: 'Sunday'
    } 
    data['day_of_week_name']=data['Date_Customer'].dt.weekday.map(dw_mapping)


    data.drop(columns=['Date_Customer'],axis=1,inplace=True)
    
   #combine the year month feature  

    data['year_month'] = data['Date_Customer_year'].apply(str) + '_' + data['Date_Customer_month'].apply(str)

  

    #polynomial features
    
    
    poly_feature_1 = ['Discounted_Purchases', 'WebPurchases', 'CatalogPurchases',
       'StorePurchases']
    poly_feature_2 = ['Amount_on_Wines', 'Amount_on_Fruits',
        'Amount_on_MeatProducts', 'Amount_on_FishProducts',
        'Amount_on_SweetProducts', 'Amount_on_GoldProds']
        
        
        
    poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)

    poly1 = poly.fit_transform(data[poly_feature_1])
    poly2 = poly.fit_transform(data[poly_feature_2])
    
    
    df_poly1 = pd.DataFrame(poly1, columns=[f"poly1_{i}" for i in range(poly1.shape[1])])
    df_poly2 = pd.DataFrame(poly2, columns=[f"poly2_{i}" for i in range(poly2.shape[1])])

    new_data = pd.concat([data, df_poly1], axis = 1)
    new_data = pd.concat([new_data, df_poly2], axis = 1)

    data = new_data
    
    
    def rec(x):
         if (x > 0) & (x <= 20):
             x = 1
         elif (x > 20) & (x <= 40):
             x = 2
         elif (x > 40) & (x <= 60):
             x = 3
         elif (x > 60) & (x <= 80):
             x = 4
         else:
             x = 5
             
         return x
     
    def web(x):
         if (x > 0) & (x <= 5):
             x = 1
         elif (x > 5) & (x <= 10):
             x = 2
         elif (x > 10) & (x <= 15):
             x = 3
         elif (x > 15) & (x <= 20):
             x = 4
         else:
             x = 5
             
         return x
        
    
    
    data['Rec_count'] = data['Recency'].apply(rec)
        
    data['Web_count'] = data['WebVisitsMonth'].apply(web)  

    
    #create additional new features
    
    data['total_kids'] = data['No_of_Kids_in_home'] + data['No_of_Teen_in_home']
    
    data['total_purchase'] = data['WebPurchases'] + data['CatalogPurchases'] + data['StorePurchases']

    data['tot_food_price'] = data['Amount_on_Wines']+ data['Amount_on_Fruits'] + data['Amount_on_MeatProducts']+ data['Amount_on_Wines'] + data['Amount_on_FishProducts'] + data['Amount_on_SweetProducts'] + data['Amount_on_GoldProds']

    data['wine_frac'] = data['Amount_on_Wines'] / data['tot_food_price']    

    data['fish_net'] = data['tot_food_price']  - data['Amount_on_FishProducts']   

    data['gold_dis'] = data['Amount_on_GoldProds'] / data['Disposable_Income']    

    data['meat_dis'] = data['Amount_on_MeatProducts'] / data['Disposable_Income']    

    data['food_dis'] = data['Disposable_Income']  - data['tot_food_price']     

        
   
    data = data[feat]

    return data



def predict_res(config, model):
     
    df = pd.DataFrame([config])
        
    preproc_df =works(df)

    y_pred = model.predict(preproc_df)
    
    
    return y_pred
    


