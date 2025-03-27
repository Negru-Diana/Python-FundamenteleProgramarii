class Client:

    def __init__(self, id_client, nume, cnp):
        self.__id = id_client
        self.__nume = nume
        self.__cnp = cnp



    def get_id(self):
        return self.__id


    def get_nume(self):
        return self.__nume


    def get_cnp(self):
        return self.__cnp


    def set_id_client(self, value):
        self.__id_client = value


    def set_nume(self, value):
        self.__nume = value


    def set_cnp(self, value):
        self.__cnp = value