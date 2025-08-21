import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from IPython.display import HTML
import base64

class TN_veg:
    def __init__(self):
        pass

    def re_index(self,df):
        df = df.reset_index(drop=True)
        df.index = df.index+1
        df.index.name = 'id'
        return df
    
    def image_html(self,img):
        with open(img,'rb') as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return f'<img src="data:image/png;base64,{encoded}" width="30">'

    def clean_data(self,url):
        df = pd.read_html(url)[0]
        df = df[['Unnamed: 0','Vegetable','Retail Price']]
        df.columns = ['images','Vegetable', 'Retail_Price_per_Kg']
        df['Avg_Price_per_Kg'] = (df['Retail_Price_per_Kg'].str.split('-',expand=True)[0].astype('int64') + df['Retail_Price_per_Kg'].str.split('-',expand=True)[1].astype('int64'))/2
        df['images']=[f"images/{i}.png" for i in range(1,55)]
        return self.re_index(df)
    
    def ess_veg(self,df):
        ess_df = pd.DataFrame()
        for i in ['Onion Big (பெரிய வெங்காயம்)', 'Onion Small (சின்ன வெங்காயம்)','Shallot (Pearl Onion) (சிறிய வெங்காயம்)',
            'Tomato (தக்காளி)', 'Green Chilli (பச்சை மிளகாய்)','Garlic (பூண்டு)', 'Ginger (இஞ்சி)',
            'Curry Leaves (கறிவேப்பிலை)'
            ]:
            ess_df = pd.concat([ess_df,df[df['Vegetable']==i]])
        ess_df.sort_values(by='Avg_Price_per_Kg', inplace=True)       
        ess_df =  self.re_index(ess_df)
        ess_df = ess_df.to_html(escape=False,formatters={'images':TN_veg().image_html})
        return ess_df
    
    def spin_veg(self,df):
        spin_df = pd.DataFrame()
        for i in ['Amaranth Leaves (சிறு கீரை)','Colocasia Leaves (சேப்பங்கிழங்கு கீரை)','Fenugreek Leaves (வெந்தயக்கீரை)','Sorrel Leaves (புளிச்ச கீரை)',
            'Spinach (கீரை)','Dill Leaves (வெந்தயம் இலைகள்)']:
            spin_df = pd.concat([spin_df,df[df['Vegetable']==i]])
        spin_df.sort_values(by='Avg_Price_per_Kg', inplace=True)
        spin_df =self.re_index(spin_df)
        spin_df = spin_df.to_html(escape=False,formatters={'images':TN_veg().image_html})
        return spin_df
    
    def gro_veg(self,df):
        gro_df = pd.DataFrame()
        for i in ['Beetroot (பீட்ரூட்)', 'Potato (உருளைக்கிழங்கு)','Carrot (கேரட்)','Colocasia (சேப்பங்கிழங்கு)'
                  'Elephant Yam (சேனைக்கிழங்கு)','Radish (முள்ளங்கி)','Sweet Potato (இனிப்பு உருளைக்கிழங்கு)']:
            gro_df = pd.concat([gro_df,df[df['Vegetable']==i]])
        gro_df.sort_values(by='Avg_Price_per_Kg', inplace=True)
        gro_df =self.re_index(gro_df)
        gro_df = gro_df.to_html(escape=False,formatters={'images':TN_veg().image_html})
        return gro_df

    def gen_veg(self,df):
        gen_df = pd.DataFrame()
        for i in ['Beetroot (பீட்ரூட்','Potato (உருளைக்கிழங்கு)','Cabbage (முட்டைக்கோஸ்)',
       'Carrot (கேரட்)', 'Cauliflower (காலிஃபிளவர்)','Coconut (தேங்காய்)','Drumsticks (முருங்கைக்காய்)', 'Brinjal (கத்திரிக்காய்)',
       'Brinjal (Big) (கத்திரிக்காய்)','Ladies Finger (வெண்டைக்காய்)',
       'Radish (முள்ளங்கி)', 'Ridge Gourd (பீர்க்கங்காய்)',]:
            gen_df = pd.concat([gen_df,df[df['Vegetable']==i]])
        gen_df.sort_values(by='Avg_Price_per_Kg', inplace=True)
        gen_df = self.re_index(gen_df)
        gen_df = gen_df.to_html(escape=False,formatters={'images':TN_veg().image_html})
        return gen_df

    
    def oth_veg(self,df):
        oth_df =pd.DataFrame()
        for i in df.Vegetable.values:
            if i not in ['Beetroot (பீட்ரூட்','Potato (உருளைக்கிழங்கு)','Cabbage (முட்டைக்கோஸ்)',
            'Carrot (கேரட்)', 'Cauliflower (காலிஃபிளவர்)','Coconut (தேங்காய்)','Drumsticks (முருங்கைக்காய்)', 'Brinjal (கத்திரிக்காய்)',
            'Brinjal (Big) (கத்திரிக்காய்)','Ladies Finger (வெண்டைக்காய்)',
            'Radish (முள்ளங்கி)', 'Ridge Gourd (பீர்க்கங்காய்)','Beetroot (பீட்ரூட்)', 'Potato (உருளைக்கிழங்கு)','Carrot (கேரட்)','Colocasia (சேப்பங்கிழங்கு)'
                'Elephant Yam (சேனைக்கிழங்கு)','Radish (முள்ளங்கி)','Sweet Potato (இனிப்பு உருளைக்கிழங்கு)','Amaranth Leaves (சிறு கீரை)','Colocasia Leaves (சேப்பங்கிழங்கு கீரை)','Fenugreek Leaves (வெந்தயக்கீரை)','Sorrel Leaves (புளிச்ச கீரை)',
                'Spinach (கீரை)','Dill Leaves (வெந்தயம் இலைகள்)','Onion Big (பெரிய வெங்காயம்)', 'Onion Small (சின்ன வெங்காயம்)','Shallot (Pearl Onion) (சிறிய வெங்காயம்)',
                'Tomato (தக்காளி)', 'Green Chilli (பச்சை மிளகாய்)','Garlic (பூண்டு)', 'Ginger (இஞ்சி)',
                'Curry Leaves (கறிவேப்பிலை)']:
                oth_df = pd.concat([oth_df,df[df['Vegetable']==i]])
        oth_df.sort_values(by='Avg_Price_per_Kg', inplace=True)
        oth_df =self.re_index(oth_df)
        oth_df = oth_df.to_html(escape=False,formatters={'images':TN_veg().image_html})
        return oth_df
    
    def cal_veg(seff,df,qty_df):

        cal_veg_df = pd.merge(df,qty_df,how='inner',on='Vegetable')
        cal_veg_df = pd.concat([cal_veg_df ,cal_veg_df['Retail_Price_per_Kg'].str.split(' - ',expand=True)],axis=1)
        cal_veg_df.columns = ['images','Vegetable','Retail_Price_per_Kg','Avg_Price_per_Kg','Quantity','min_val','max_val']
        cal_veg_df = cal_veg_df[['images','Vegetable','Quantity','min_val','max_val','Avg_Price_per_Kg']]
        cal_veg_df['Avg_Price'] = cal_veg_df['Avg_Price_per_Kg'] * cal_veg_df['Quantity']
        cal_veg_df['min_val'] = cal_veg_df['min_val'].astype('int64') * cal_veg_df['Quantity']
        cal_veg_df['max_val'] = cal_veg_df['max_val'].astype('int64') * cal_veg_df['Quantity']
        cal_veg_df['Retail_Price'] = cal_veg_df['min_val'].astype(str) + ' - ' + cal_veg_df['max_val'].astype(str)
        cal_veg_df = cal_veg_df[['images','Vegetable','Quantity','Retail_Price','Avg_Price']]
        
        #cal_veg_df = cal_veg_df.to_html(escape=False,formatters={'images':TN_veg().image_html})
        
        
        return cal_veg_df

