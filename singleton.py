class Singleton(object):
    __instance = None

    def __new__(self):
        if self.__instance == None:
            self.__instance = object.__new__(self)
        return self.__instance

a = Singleton()
print a
b = Singleton()
print b