 ## Hierarchical Inheritance 

class Details:

    def __init__(self):
        self.name = ""
        self.price = ""
        self.seasons =""

    def setData(self,name,price,seasons):
        self.name = name
        self.price = price
        self.seasons = seasons

    def showData(self):
        print(f'name = {self.name}')
        print(f'price = {self.price}')
        print(f'season = {self.seasons}')

class Market(Details):

    def __init__(self):
        self.vendor = ""
        self.farmer = ""

    def setMarket(self,name,price,seasons,vendor,farmer):
        self.setData(name,price,seasons)
        self.vendor = vendor
        self.farmer = farmer

    def showMarket(self):
        self.showData()
        print(f'vendor ={self.vendor}')
        print(f'farmer ={self.farmer}')

class shops(Details):

    def __init__(self):
        self.zomato = ""
        self.blinkit =""
        self.jiomart = ""

    def region(self,name,price,seasons,zomato,blinkit,jiomart):
         self.setData(name,price,seasons)
         self.zomato = zomato
         self.blinkit = blinkit
         self.jiomart = jiomart

    def showregion(self):
        self.showData()
        print(f'zomato = {self.zomato}')   
        print(f'blinkit = {self.blinkit}')   
        print(f'jiomart = {self.jiomart}')   


markobj = Market()
markobj.setMarket('Mango',200,'summer','suresh','mukesh')
markobj.showMarket()

print('----')
print(f'shops class object')

shopobj = shops()
shopobj.region('lichi',250,'summer',240,260,300)
shopobj.showregion()
