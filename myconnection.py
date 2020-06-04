from pymysql import *

class myconnection:
    def connect(self):
        conn=connect('localhost','root','','onlineshopping')
        return conn
    def fethcategories(self):
        list=['Electronics','Furniture','Books','Clothes','Shoes','Household']
        return list