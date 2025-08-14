#import pandas
import pandas as pd
from sqlalchemy import create_engine

#pd.read_csv('file_name.csv')
df_1 = pd.read_csv('vendor_a.csv')
df_2 = pd.read_csv('vendor_b.csv')
df_3 = pd.read_csv('vendor_c.csv')

#file_name.rename(columns={'previous_name':'new_name'}, inplace = True)
df_1.rename(columns={'OrderID':'order_id','Date':'order_date','Product':'order_product','Qty':'order_qty','Price':'order_price'}, inplace = True)
df_2.rename(columns={'ID':'order_id','OrderDate':'order_date','Item':'order_product','Quantity':'order_qty','UnitPrice':'order_price'}, inplace = True)
df_3.rename(columns={'Order_Num':'order_id','Dt':'order_date','ProductName':'order_product','Count':'order_qty','Price_USD':'order_price'}, inplace = True)

#pd.concat([df_1, 2, 3], ignore_index = True) <= ignore the previous index and make them starting from zero
df_all = pd.concat([df_1, df_2, df_3], ignore_index = True) 

#pd.to_datetime = changing letter type to datetime
df_all['order_date'] = pd.to_datetime(df_all['order_date'], errors = 'coerce')

#drop_duplicates(subset = ['column_name1', 'column_name2', ...], inplace = True)
#drop_na(subset={'column_name1', 'column_name2', ...}, inplace = True)
df_all.drop_duplicates(subset = ['order_id', 'order_date', 'order_product', 'order_qty', 'order_price'], inplace = True)
df_all.dropna(subset={'order_id','order_date','order_price','order_qty','order_product'}, inplace = True)

from sqlalchemy import create_engine
#('mysql+mysqlconnector://username/password@localhost/schema_name')
engine = create_engine('mysql+mysqlconnector://root:Happydk%401@localhost/sales_db')

#name.to_sql(table_name, con=engine)
df_all.to_sql('sales', con=engine, if_exists = 'replace', index = False)





