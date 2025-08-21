import pandas as pd
from bs4 import BeautifulSoup
import requests
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import streamlit.components.v1 as components
from Fun import TN_veg
from IPython.display import HTML

def home():
  st.set_page_config(page_title = "Tamilnadu Vegetable Market Price Today",
                    page_icon = "🚨",layout = "wide")
  c1,c2 =st.columns([1.5,2])
  c1.image('cover.png',width=800)
  c2.title("Tamilnadu Vegetable ",width='stretch')
  c2.title("Market")
  st.header("Today Market Price")
  

gen_url = 'https://vegetablemarketprice.com'

find = 'https://vegetablemarketprice.com/market'
response = requests.get(find)
soup = BeautifulSoup(response.text, 'html')
link_dic = dict(zip([i.get_text(strip=True).replace('market price','').strip() for i in soup.find_all(class_ = 'market-link-div')],
         [i['href'] for i in soup.find_all(class_='market-link')]))
del_list = ['Andaman and Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
             'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 
             'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 
             'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 
            'Odisha',  'Punjab', 'Rajasthan', 'Sikkim',  'Telangana', 'Tripura', 'Uttar Pradesh', 
            'Uttarakhand', 'West Bengal', 'Agra', 'Ahmedabad',  'Bangalore', 'Bhopal',  'Delhi New', 
              'Ernakulam',  'Gangtok', 'Hosur', 'Hyderabad', 'Itanagar', 'Jaipur',  'Kolkata', 'Kollam','Kozhikode', 
                'Lucknow','Mayiladuthurai', 'Mumbai','Noida', 'Palakkad', 'Patna',  'Udagamandalam (Ooty)', 'Varanasi', 'Visakhapatnam']


for i in del_list:
    del link_dic[i]

link_dic = dict(sorted(link_dic.items()))

def genral_view():
  
  with st.form(key = 'Select District'):
      A = st.selectbox('Select District:',link_dic.keys(),width=300)
      submit = st.form_submit_button(label='Submit')
      if submit:
        st.write(f"{A} District Vegetable Marked Prices")
        
        response = requests.get(gen_url+link_dic[A])
        soup = BeautifulSoup(response.text, 'html')
        st.write(soup.find(class_="calendar-selection-container").get_text(strip=True))
        
        df = TN_veg().clean_data(gen_url+link_dic[A])

        st.markdown("""
                  <style>
                  table {
                      font-size: 12px;
                      width: auto;
                  }
                  td, th {
                      padding: 4px 8px;
                      text-align: center;
                      vertical-align: middle;
                  }
                  img {
                      display: block;
                      margin: auto;
                  }
                  </style>
              """, unsafe_allow_html=True)

        c1,c2 = st.columns(2,gap='small',border=True)
        with c1:
          st.info("Essential Vegetables")
          st.markdown(TN_veg().ess_veg(df), unsafe_allow_html=True)
          
        with c2:
          st.info("Spinach Vareties")
          st.markdown(TN_veg().spin_veg(df), unsafe_allow_html=True)

        c3,c4 = st.columns(2,gap='small',border=True)
        with c3:
          st.info("Ground Vegetables")
          st.markdown(TN_veg().gro_veg(df), unsafe_allow_html=True)
        with c4:
          st.info("Frequent Used Vegitables")
          st.markdown(TN_veg().gen_veg(df), unsafe_allow_html=True)

        st.info("Other Vegitables")
        st.markdown(TN_veg().oth_veg(df), unsafe_allow_html=True)


def cal_view():
  st.title("Vegetable Price Calculator")
  link = st.selectbox("Select District:",link_dic.keys())
  df = TN_veg().clean_data(gen_url+link_dic[link])
  sel_veg = st.multiselect("Select the Vegitables:",df['Vegetable'].unique())
  wh_mes_df = pd.DataFrame()
  
  with st.form("my_form"):
    
    l = []
    for i in sel_veg:
      qty = st.number_input(i)
      l.append([i,qty])
       
    submit_button = st.form_submit_button("Submit")
    if submit_button:
      Qty_df = pd.DataFrame(l,columns=['Vegetable','Quantity'])
      
      cal_df = TN_veg().cal_veg(df,Qty_df)
      sum = cal_df['Avg_Price'].sum()
      wh_mes_df = pd.concat([wh_mes_df,cal_df])
      cal_df = cal_df.to_html(escape=False,formatters={'images':TN_veg().image_html})  
      st.markdown(cal_df,unsafe_allow_html=True)
      st.markdown(f"Total Average Price for buying is: Rs.{sum}")
    

  html_output = wh_mes_df.to_html(escape=False,formatters={'images':TN_veg().image_html})
    
  st.download_button(
    label="Download price list as HTML file",
    data=html_output,
    file_name="Todayvegmarket.html",
    mime="text/html",
    help="Click to download the marketprice Table"
  )
  
  

home()

page = st.radio("Select the page:", ["Vegetable Market Price Today", "Vegetable Price Calculator"],horizontal=True,key="page")

if page == "Vegetable Market Price Today":
    genral_view()
elif page == "Vegetable Price Calculator":
    cal_view()

        
        