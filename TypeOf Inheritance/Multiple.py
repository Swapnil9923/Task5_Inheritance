class IPL:

    def __init__(self,Team_name,players):
        self.Team_name =Team_name
        self.players =players
        
    def printname(self):
        print(f'Teamname ={self.Team_name},players={self.players}')

class Country:

    def __init__(self, Position, runs):
        self.position = Position
        self.runs = runs

    def printcountry(self):
        print(f'position = {self.position},runs ={self.runs}')
        

class scorecard(IPL,Country):

     def __init__(self, Team_name, players, position, runs, century, hundred):
        IPL.__init__(self, Team_name, players)  
        Country.__init__(self, position, runs)  
        self.century = century
        self.hundred = hundred


     def printscorecard(self):
        print(f'TeamName ={self.Team_name}')
        print(f'players ={self.players}')
        print(f'position {self.position}')
        print(f'runs = {self.runs}')
        print(f'century ={self.century}')
        print(f'hundred ={self.hundred}')


iplobj =IPL('MI','Rohit')

iplobj.printname()


countryobj = Country('Captain',200)

countryobj.printcountry()

cardobj = scorecard('MI','Rohit','Captain',200,3,4)

cardobj.printscorecard()


                    