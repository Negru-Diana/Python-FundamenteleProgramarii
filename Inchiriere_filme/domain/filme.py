class Film:

    def __init__(self, id, titlu, descriere, gen):
        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen.strip().lower()
        

    def get_id(self):
        return self.__id


    def get_titlu(self):
        return self.__titlu


    def get_descriere(self):
        return self.__descriere


    def get_gen(self):
        return self.__gen

    def set_id(self, value):
        self.__id = value


    def set_titlu(self, value):
        self.__titlu = value


    def set_descriere(self, value):
        self.__descriere = value


    def set_gen(self, value):
        self.__gen = value.strip().lower()

    
        