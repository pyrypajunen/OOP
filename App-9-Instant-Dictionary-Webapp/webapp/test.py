class D:
    
    @classmethod
    def method(cls): #cls = class itself, not class instance, self = instance of the class
        print(cls)
        
D.method()