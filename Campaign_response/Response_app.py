import streamlit as st
import datetime 
import requests
import time
# import os


ft_acc = ['ID','Recency','Date_Customer','Cmp3Accepted', 'Cmp5Accepted','Cmp4Accepted','Cmp1Accepted',
        'WebVisitsMonth', 'Marital_Status','Amount_on_Wines','Disposable_Income','No_of_Teen_in_home','No_of_Kids_in_home',
       'Discounted_Purchases','WebPurchases', 'CatalogPurchases','StorePurchases', 'Amount_on_Fruits',
       'Amount_on_MeatProducts', 'Amount_on_FishProducts','Amount_on_SweetProducts', 'Amount_on_GoldProds','Education_Level'
       ]


dic = {}


# nav = st.sidebar.radio( "Navigation", ['Home','Predictions'])

# if nav == 'Home':
#     st.title("Customers Campaign Response")
#     st.markdown("##### *Know your customers behaviour* " )
    

#     st.text("")
    
#     st.text("")
    
    
#     path = os.path.dirname(__file__) 
#     my_file = path+'\customer.jpg'
    
#     # print(my_file) Campaign_response\customer.jpg
    
#     st.image('Campaign_response\customer.jpg') 


# if nav == 'Predictions':
    
    
st.title("Customer's Details")

st.text("")

st.text("")


first,third,last = st.columns(3)

dic["ID"] = first.text_input("ID")

dic["Recency"] = last.number_input("Recency")  

dic["Date_Customer"] = str(third.date_input('Date Customer',value = datetime.date(2012, 1, 1), min_value= datetime.date(2012, 1, 1), max_value= datetime.date(2015, 1, 1)))

# x = dic["Date_Customer"].str.strip('')[0]

# print('dates: ', x )


one,two = st.columns(2)

dic["Marital_Status"] = one.selectbox("Marital Status",( "Married", "Together","Single","Divorced","Widow","Alone","YOLO","Absurd"))  

dic["Education_Level"] = two.selectbox('Education Level',( "Graduation", "PhD","Master","2n Cycle","Basic"))


one,two = st.columns(2)

dic["No_of_Kids_in_home"] = one.number_input("No of Kids") 

dic["No_of_Teen_in_home"] = two.number_input("No of Teen") 
st.text("")



dic["WebVisitsMonth"] = st.slider("Web Visits Month",0, 20, 1)  

st.text("")
    
first,second = st.columns([2,1])

dic["Disposable_Income"] = first.number_input('Disposable Income') 

dic["Amount_on_Wines"] = second.number_input('Amount on Wines') 

st.text("")

first,second,third = st.columns(3)

dic["Amount_on_Fruits"] = first.number_input('Amount on Fruits') 

dic["Amount_on_MeatProducts"] = second.number_input('Amount on MeatProducts') 

dic["Amount_on_FishProducts"] = third.number_input('Amount on FishProducts') 

st.text("")

second,third, fourth = st.columns([1,2,1 ])

dic["Amount_on_SweetProducts"] = second.number_input('Amount on SweetProducts')  

dic["Amount_on_GoldProds"] = third.number_input('Amount on GoldProds') 

dic["Discounted_Purchases"] = fourth.number_input('Discounted Purchases') 

st.text("")

first,second,third = st.columns(3) 

    

dic["WebPurchases"] = first.number_input('Web Purchases') 

dic["CatalogPurchases"] = second.number_input('Catalog Purchases') 

dic["StorePurchases"] = third.number_input('Store Purchases') 


st.text("")




sel = st.selectbox("Accepted Campaign",( "Campaign 1", "Campaign 3","Campaign 4","Campaign 5"))



if sel == "Campaign 1":
    dic["Cmp1Accepted"] = 1
    dic["Cmp3Accepted"] = 0
    dic["Cmp4Accepted"] = 0
    dic["Cmp5Accepted"] = 0

elif sel == "Campaign 3":
    dic["Cmp1Accepted"] = 0
    dic["Cmp3Accepted"] = 1
    dic["Cmp4Accepted"] = 0
    dic["Cmp5Accepted"] = 0
elif sel == "Campaign 4":
    dic["Cmp1Accepted"] = 0
    dic["Cmp3Accepted"] = 0
    dic["Cmp4Accepted"] = 1
    dic["Cmp5Accepted"] = 0
elif sel == "Campaign 5":
    dic["Cmp1Accepted"] = 0
    dic["Cmp3Accepted"] = 0
    dic["Cmp4Accepted"] = 0
    dic["Cmp5Accepted"] = 1
else:
    print('none')





st.text("")

st.text("")


st.text("")




# Function to make API request        
def processRequest(path, json):

    retries = 0
    result = None
    _maxNumRetries = 10
    
    result = ''

    while True:

        response = requests.post(path, json = json)

        if response.status_code == 429: 

            print( "Message: %s" % ( response.json()['error']['message'] ) )

            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break

        elif response.status_code == 200 or response.status_code == 201:
            result = response.json()['Customer_prediction'][0]
            print(result)
            
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json()['error']['message'] ) )

        break
    
    
    return result





url = "https://customer-campaign.herokuapp.com/predict"

    
if st.button("Submit"):
    
    g = processRequest(url, dic)
    
    with st.spinner('Wait for it...'):
        time.sleep(2)
    
    print('New prediction: ',g)
    
    if g == 1:
        st.success('This customer will respond to the campaign')
    else:
        st.success('This customer will not respond to the campaign') 

       
        
    
    
    
        



