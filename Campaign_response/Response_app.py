import streamlit as st
import datetime 
import requests
import time
# import os


ft_acc = ['ID','Recency','Date_Customer','Cmp3Accepted','Cmp5Accepted','Cmp4Accepted','Cmp1Accepted',
        'WebVisitsMonth', 'Marital_Status','Amount_on_Wines','Disposable_Income','No_of_Teen_in_home','No_of_Kids_in_home',
       'Discounted_Purchases','WebPurchases', 'CatalogPurchases','StorePurchases', 'Amount_on_Fruits',
       'Amount_on_MeatProducts', 'Amount_on_FishProducts','Amount_on_SweetProducts', 'Amount_on_GoldProds','Education_Level'
       ]


dic = {}


nav = st.sidebar.radio( "Navigation", ['Home','About','Predictions'])

if nav == 'Home':
    st.title("Customers Campaign Response")
    st.markdown("##### *Know your customers behaviour* " )
    

    st.text("")
    
    st.text("")
    
    
    st.image(
            "https://media.istockphoto.com/photos/close-up-woman-paying-by-contactless-card-terminal-on-bar-counter-picture-id1152767835?k=20&m=1152767835&s=612x612&w=0&h=3CyFEuWqct0JiYZSZGbMUkA8o-ULrh2PC6QbzRhm3DA=",
           
            # Manually Adjust the width of the image as per requirement
        )
    
    
if nav == 'About':
    st.title("Project Description")
    # st.markdown("##### *Know your customers behaviour* " )
    
    st.write(
        """
        
        This project makes use of an Artificial Intelligence(AI) algorithm to predict the response of your customers to your marketing campaigns  by 
        entering the details of their purchasing behaviours and other personal attributes
        
        """
             )
    
    st.text("")
    
    st.text("")
    
    st.text("")
    
    st.markdown("##### *Here is an outine of customers details and their meanings*")
    
    st.info(
    '''  
    - Year of Birth : Birth year of the customer
    - Education Level : The highest level of education attained by the User
    - Marital Status : Marital status of the customer
    - Disposable Income : Yearly household disposable income of the customer
    - No of Kids : Total count of children in the customer's home
    - No of Teen : Number of teenagers in the customer's household
    - Date Customer : Date of customer's enrollment with the company
    - Recency : Number of days since customer's last purchase
    - Discounted Purchases : Counts of purchases made by the customer using coupons
    - Web Purchases : Counts of purchases made by the customer through the company’s website
    - Catalog Purchases : Counts of purchases made by the customer using a catalogue
    - Store Purchases : Counts of purchases made by the customer directly in stores
    - Amount on Wines : Total amount customer spent on wine and drinks within the last 3 years
    - Amount on Fruits : Total amount customer spent on fruity food within the last 3 years
    - Amount on Meat Products : Total amount customer spent on meat products and livestock within the last 3 years
    - Amount on Fish Products : Total amount customer spent on fish alone within the last 3 years
    - Amount on Sweet Products : Total amount customer spent on sweets and chocolates within the last 3 years
    - Amount on Gold Prods : Total amount customer spent on golden products within the last 3 years
    - Web Visits Month : The number of times the customer of visits to company’s website within the last 4 weeks
    - Accepted Campaign : When campaign offer was accepted 
    
                ''',)
    
    
    
    



if nav == 'Predictions':
    
    
    st.title("Customer's Details")

    st.text("")

    st.text("")


    third,last = st.columns(2)

    

    dic["Recency"] = last.number_input("Recency",step= 1)  

    dic["Date_Customer"] = str(third.date_input('Date Customer',value = datetime.date(2012, 1, 1), min_value= datetime.date(2012, 1, 1), max_value= datetime.date(2015, 1, 1)))

    # x = dic["Date_Customer"].str.strip('')[0]

    # print('dates: ', x )


    one,two = st.columns(2)

    dic["Marital_Status"] = one.selectbox("Marital Status",( "Married", "Together","Single","Divorced","Widow","Alone","YOLO","Absurd"))  

    dic["Education_Level"] = two.selectbox('Education Level',( "Graduation", "PhD","Master","2n Cycle","Basic"))


    one,two = st.columns(2)

    dic["No_of_Kids_in_home"] = one.number_input("No of Kids",step= 1) 

    dic["No_of_Teen_in_home"] = two.number_input("No of Teen",step=1) 
    st.text("")



    dic["WebVisitsMonth"] = st.slider("Web Visits Month",0, 20, 1)  

    st.text("")
        
    first,second = st.columns([2,1])

    dic["Disposable_Income"] = first.number_input('Disposable Income',step= 1) 

    dic["Amount_on_Wines"] = second.number_input('Amount on Wines',step= 1) 

    st.text("")

    first,second,third = st.columns(3)

    dic["Amount_on_Fruits"] = first.number_input('Amount on Fruits',step= 1) 

    dic["Amount_on_MeatProducts"] = second.number_input('Amount on MeatProducts',step= 1) 

    dic["Amount_on_FishProducts"] = third.number_input('Amount on FishProducts',step= 1) 

    st.text("")

    second,third, fourth = st.columns([1,2,1 ])

    dic["Amount_on_SweetProducts"] = second.number_input('Amount on SweetProducts',step= 1)  

    dic["Amount_on_GoldProds"] = third.number_input('Amount on GoldProds',step= 1) 

    dic["Discounted_Purchases"] = fourth.number_input('Discounted Purchases',step= 1) 

    st.text("")

    first,second,third = st.columns(3) 

        

    dic["WebPurchases"] = first.number_input('Web Purchases',step= 1) 

    dic["CatalogPurchases"] = second.number_input('Catalog Purchases',step= 1) 

    dic["StorePurchases"] = third.number_input('Store Purchases',step= 1) 


 
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

       
        
    
    
    
        



