from abc import ABCMeta , abstractmethod
class personne (metaclass = ABCMeta) :
    def __init__(self,code,name,prenom,age):
        self._code = code
        self._name = name
        self._prenom = prenom
        self._age = age

    @property
    def getcode (self):
        return self._code
    @property
    def getname (self):
        return self._name
    @property
    def getprenom (self):
        return self._prenom
    @property
    def getage (self):
        return self._age
    
    def setcode (self,code) :
        self._code= code
    def setname (self,name) :
        self._name= name
    def setprenom (self,prenom) :
        self._prenom= prenom
    def setage (self,age) :
        self._age = age

    @abstractmethod
    def tostring (self) :
        pass

    def Equals (self,p):
         if (self.getcode==p.getcode):
            return True
         else :
            return False
    
        
class employe (personne):
    _count1 = 0
    def __init__(self,code ,name,prenom,age,grade):
        super().__init__(code,name,prenom,age)
        self.__grade = grade
        employe._count1 += 1

    @property
    def getgrade (self):
        return self.__grade
    
    def setgrade (self,grade) :
        self.__grade= grade
    
    def tostring (self) :
        print(f"the code :{self.getcode}")
        print(f"the name :{self.getname}")
        print(f"the prenom :{self.getprenom}")
        print (f"the age:{self.getage}")
        print (f"grade :{self.__grade}")
        print (f" nbr employe :{employe._count1}")
    
    def Equals(self, p):
        return super().Equals(p)
    
class eleve (personne):
     _count2 = 0
     def __init__(self,code ,name,prenom,age,niveau,moyenne):
        super().__init__(code,name,prenom,age)
        self.__niveau = niveau
        self.__moyenne = moyenne
        eleve._count2 += 1

     @property
     def getniveau (self):
        return self.__niveau
     @property
     def getmoyenne (self):
        return self.__moyenne
    
     def setgrade (self,niveau) :
        self.__niveau= niveau
     def setmoyenne (self,moyenne) :
        self.__moyenne= moyenne

     def tostring (self) :
        print(f"the code :{self.getcode}")
        print(f"the name :{self.getname}")
        print(f"the prenom :{self.getprenom}")
        print (f"the age:{self.getage}")
        print (f"niveau :{self.__niveau}")
        print (f"moyenne :{self.__moyenne}")
        print (f" nbr eleve :{employe._count1}")

     def Equals(self, p):
        return super().Equals(p)
     

e1 = employe ("123","farah","saiza","20","9")
e1.tostring()
e2 = employe ("456","wissal","loutfi","21","10")
e2.tostring()
print (e2.Equals(e1))
e3 = employe ("789","rihab","kabaj","22","5")
e3.tostring()
print (e3.Equals(e2))

el1 = eleve("123","farah","saiza","20","5eme","15")
el1.tostring()
el2 = eleve("456","wissal","loutfi","21","bac","16")
el1.tostring()
print (el2.Equals(el1))
el3 = eleve ("789","rihab","kabaj","22","6eme","18")
el3.tostring()
print (el3.Equals(el2))
print (employe._count1 + eleve._count2)