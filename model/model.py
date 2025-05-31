from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    @staticmethod
    def getAllAnni():
        return DAO.getAllAnni()

    @staticmethod
    def getAllBrand():
        return DAO.getAllBrand()

    @staticmethod
    def getAllRetailer():
        return DAO.getAllRetailer()

    @staticmethod
    def getRicavi(anno,brand,retailer):
        return DAO.getRicavi(anno,brand,retailer)