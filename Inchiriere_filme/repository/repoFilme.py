from domain.filme import Film

class RepoFilm:

    def __init__(self, lista_filme):
        self.__lista_filme = lista_filme


    """
    Adauga un nou film in lista si actualizeaza fisierul

    film_nou - Film
    """
    def adauga(self, film_nou):
        self.__lista_filme.append(film_nou)
        self.scrie_in_fisier()


    """
    Sterge un film din lista si actualizeaza fisierul

    film_de_sters - Film
    """
    def sterge(self, film_de_sters):
        if film_de_sters in self.__lista_filme:
            self.__lista_filme.remove(film_de_sters)
            self.scrie_in_fisier()


    """
    Modifica datele unui film

    film_nou - Film
    film_vechi - Film
    """
    def modifica(self, film_nou, film_vechi):
        if film_vechi in self.__lista_filme:
            self.__lista_filme.remove(film_vechi)
            self.__lista_filme.append(film_nou)
            self.scrie_in_fisier()


    """
    Returneaza lista filmelor
    """
    def get_all(self):
        return self.__lista_filme


    """
    Scrie filmele din lista in fisier
    """
    def scrie_in_fisier(self):
        f=open("filme.txt","w")
        for x in self.__lista_filme:
            f.write(str(x.get_id())+";"+str(x.get_titlu())+";"+str(x.get_descriere())+";"+str(x.get_gen()+"\n"))
        f.close()


    """
    Incarca filmele din fisier
    """
    def citeste_filme_din_fisier(self):
        self.__lista_filme=[]
        f=open("filme.txt","r")
        for x in f:
            if ";" not in x:
                continue
            text=x.split(";")
            film_nou=Film(text[0],text[1],text[2],text[3].strip().lower())
            self.__lista_filme.append(film_nou)
        f.close()