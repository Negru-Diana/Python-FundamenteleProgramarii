class Inchiriere:

    def __init__(self, id, id_film, cnp_client, data_inchiriere, data_retur):
        self.__id = id
        self.__id_film = id_film
        self.__cnp_client = cnp_client
        self.__data_inchiriere = data_inchiriere
        self.__data_retur = data_retur

    def get_id(self):
        return self.__id


    def get_id_film(self):
        return self.__id_film


    def get_cnp_client(self):
        return self.__cnp_client


    def get_data_inchiriere(self):
        return self.__data_inchiriere


    def get_data_retur(self):
        return self.__data_retur


    def set_id(self, value):
        self.__id = value


    def set_id_film(self, value):
        self.__id_film = value


    def set_cnp_client(self, value):
        self.__cnp_client = value


    def set_data_inchiriere(self, value):
        self.__data_inchiriere = value


    def set_data_retur(self, value):
        self.__data_retur = value
