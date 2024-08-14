import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io


st.title("Data Analysis Web App")

data = pd.read_csv('train.csv')
st.write('Data ....')
st.write(data)
st.write('Data info')
buffer = io.StringIO()
data.info(buf=buffer)
s = buffer.getvalue()
st.text(s)



data[data.duplicated()] # xem dữ liệu trùng

data_new=data.drop_duplicates() # 
# data.drop_duplicates(inplace=True) 


st.text(data_new.describe())

data_new.isnull().sum() # thống kế số giá trị null

data_new1=data_new
data_new[data_new['Postal Code'].isnull()] # xem dong null

data_new=data_new.dropna() # oa cac dòng có null
data_new.isnull().sum() 

data_new1['Postal Code']=data_new1['Postal Code'].fillna('999')
data_new1[data_new1['Postal Code'].isnull()] # xem dong null

data_new['Order Date']=pd.to_datetime(data_new['Order Date'],format='%d/%m/%Y')# định dạng ngày tháng theo : dd/MM/yyyy
data_new['Ship Date']=pd.to_datetime(data_new['Ship Date'],format='%d/%m/%Y')
data_new['Sakes']=data_new['Sales'].astype(float) # định dạng lại dữ liệu tiền tệ
data_new.info()

# Thiết lập tiêu đề cho ứng dụng
st.title('Sales over Time Scatter Plot')

# Vẽ biểu đồ sử dụng Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(data_new['Order Date'], data_new['Sales'], marker='o')
ax.set_title('Sales over Time')
ax.set_xlabel('Order Date')
ax.set_ylabel('Sales')
ax.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Hiển thị biểu đồ trong Streamlit
st.pyplot(fig)



st.scatter_chart(data_new,x='Order Date',y='Sales')
st.balloons()

# picture = st.camera_input("Take a picture")

# if picture:
#     st.image(picture)
