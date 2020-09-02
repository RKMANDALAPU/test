import mysql.connector
from datetime import date
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Bits1234",
    database="SUPPPLY_CHAIN"
)
mycursor=mydb.cursor()
a=date.today()
branch_id="B01"
item_id=int(input("enter item code"))
item_name=input("item name")
req_qty=int(input("enter qty"))
req_date=a
apr_qty=0
apr_date="0000-00-000"
damages=0
refelect_qty=0
manager_apr="NOT_APPOROVED"
branch_apr="NOT_APPOROVED"
return_qty=0
return_date="0000-00-0000"
manager_remark="null"
branch_remark="null"
return_apr="null"
return_remark="null"
print(a)
sql1="insert into branch_sales(branch_id,item_id,item_name,req_qty,req_date,apr_qty,manager_apr,branch_apr,return_qty,refelect_qty,damages) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val1=(branch_id,item_id,item_name,req_qty,req_date,apr_qty,manager_apr,branch_apr,return_qty,refelect_qty,damages,)
mycursor.execute(sql1,val1)
mydb.commit()
print(a)
