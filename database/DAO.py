from database.DB_connect import DBConnect
from model.go_retailers import Retailer
from model.ricavi import Ricavi


class DAO():
    def __init__(self):
        pass

    @classmethod
    def getAllAnni(cls):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """select distinct year(gds.date)
                   from go_daily_sales gds"""
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(row[0])
        cursor.close()
        cnx.close()
        return res

    @classmethod
    def getAllBrand(cls):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """select distinct gp.Product_brand
                   from go_products gp """
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(row[0])
        cursor.close()
        cnx.close()
        return res

    @classmethod
    def getAllRetailer(cls):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                   from go_retailers"""
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(Retailer(**row))
        cursor.close()
        cnx.close()
        return res

    @classmethod
    def getRicavi(cls,anno,brand,retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select gds.date, (gds.Unit_sale_price*gds.Quantity) as ricavo, gr.Retailer_code, gp.Product_number 
                   from go_retailers gr, go_products gp, go_daily_sales gds
                   where (YEAR(gds.date) = COALESCE(%s, YEAR(gds.date))) and gp.Product_brand = COALESCE(%s, gp.Product_brand) and gr.Retailer_name = COALESCE(%s, gr.Retailer_name)
                   """
        cursor.execute(query, (anno,brand,retailer,))
        res = []
        for row in cursor:
            res.append(Ricavi(row["date"], row["ricavo"], row["Retailer_code"], row["Product_number"]))
        cursor.close()
        cnx.close()
        res.sort(reverse=True)
        return res[0:5]