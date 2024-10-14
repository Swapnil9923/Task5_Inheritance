##  Hybrid inheritance

class A:

    def phylum(self,tapeworm,planaria):
        self.tapeworm = tapeworm
        self.planaria = planaria
        print(f'Function of A class: Tapeworm = {self.tapeworm}, Planaria = {self.planaria}')


class B(A):

    def Mammals(self,bears,cats):
        self.bears= bears
        self.cats =cats
        print(f'Function of Class B: Bears = {self.bears}, Cats = {self.cats}')

class C(A):

    def Reptiles(self,python,alligator):
        self.python=python
        self.alligator= alligator
        print(f'Function of Class C: Python = {self.python}, Alligator = {self.alligator}')


class D(B,C):

    def Arthopoda(self,lobsters,crabs):
        self.lobsters=lobsters
        self.crabs =crabs
        print(f'Function of Class D: Lobsters = {self.lobsters}, Crabs = {self.crabs}')

classobj= D()

classobj.phylum('tapeworm1','planaria1')
classobj.Mammals('polar bears','Lion')
classobj.Reptiles('python snake','American alligator')
classobj.Arthopoda('Lobster','Crab')
 