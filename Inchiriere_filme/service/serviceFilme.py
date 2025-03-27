from domain.filme import Film
from repository.repoFilme import RepoFilm
from validators.validatorFilm import ValidatorFilm
import string
import random


class ServiceFilm:
    def __init__(self, repo_film):
        self.__repo_film = repo_film


    """
    Creeaza un film nou si il adauga in lista de filme daca datele sunt valide

    id - int, > 0
    titlu - string nenul
    descriere - string nenul
    gen - string din lista de gen-uri ("thriller","horror","romance","distopic","desen", "comedie", "drama", "politist")

    returneaza: True, daca filmul a fost creat si adaugat cu succes
    eroare: daca unele date sunt invalide
    """
    def creeaza_film(self, id, titlu, descriere, gen):
        film_nou = Film(id, titlu, descriere, gen)
        validator_film = ValidatorFilm(film_nou, self.__repo_film.get_all())
        errors = []
        if not validator_film.valideaza_id():
            errors.append("ID invalid. Trebuie sa fie unic si pozitiv.")
        if not validator_film.valideaza_titlu():
            errors.append("Titlul nu poate fi gol.")
        if not validator_film.valideaza_descriere():
            errors.append("Descrierea nu poate fi goala.")
        if not validator_film.valideaza_gen():
            valid_genres = ", ".join(validator_film._ValidatorFilm__lista_genuri)
            errors.append(f"Gen invalid. Genurile valide sunt: {valid_genres}")
        if errors:
            raise ValueError("\n".join(errors))
        else:
            self.__repo_film.adauga(film_nou)
            return True


    """
    Sterge un film din lista de filme, daca acesta exista

    id_film - int

    returneaza: True, daca filmul a fost sters cu succes
    eroare: daca filmul cu id-ul dat nu exista in lista de filme
    """
    def sterge_film(self, id_film):
        for film in self.__repo_film.get_all():
            if film.get_id() == id_film:
                self.__repo_film.sterge(film)
                return True
        raise ValueError(f"Filmul cu ID-ul {id_film} nu exista.")


    """
    Modifica datele unui film din lista de filme

    id_vechi - int, > 0 (id-ul vechi al filmului de modificat)
    id_nou - int, > 0 (id-ul nou al filmului de modificat)
    titlu_nou - string
    descriere_noua - string
    gen_nou - string din lista de genuri ("thriller","horror","romance","distopic","desen", "comedie", "drama", "politist")

    returneaza: True, daca filmul a fost modificat
    eroare: daca datele noi ale filmului sunt invalide
    """
    def modifica_film(self, id_vechi, id_nou, titlu_nou, descriere_noua, gen_nou):
        film_vechi = None
        for film in self.__repo_film.get_all():
            if film.get_id() == id_vechi:
                film_vechi = film
                break
        if not film_vechi:
            raise ValueError(f"Filmul cu ID-ul {id_vechi} nu exista.")
    
        # Creez lista temporara fara filmul vechi pentru validare
        lista_temp = [film for film in self.__repo_film.get_all() if film.get_id() != id_vechi]
    
        film_nou = Film(id_nou, titlu_nou, descriere_noua, gen_nou)
        validator = ValidatorFilm(film_nou, lista_temp)
    
        errors = []
        if not validator.valideaza_id():
            errors.append("ID invalid. Trebuie sa fie unic si pozitiv.")
        if not validator.valideaza_titlu():
            errors.append("Titlul nu poate fi gol.")
        if not validator.valideaza_descriere():
            errors.append("Descrierea nu poate fi goala.")
        if not validator.valideaza_gen():
            valid_genres = ", ".join(validator._ValidatorFilm__lista_genuri)
            errors.append(f"Gen invalid. Genurile valide sunt: {valid_genres}")
    
        if errors:
            raise ValueError("\n".join(errors))
        else:
            self.__repo_film.modifica(film_nou, film_vechi)
            return True


    """
    Cauta filme dupa un string

    titlu - string

    returneaza: lista de filme care contin acel string in titlu
    """
    def cauta_filme_dupa_titlu(self, titlu):
        return [film for film in self.__repo_film.get_all() if titlu.lower() in film.get_titlu().lower()]

    """
    Cauta filme de un anumit gen

    gen - string

    returneaza: lista de filme care au genul specificat
    """
    def cauta_filme_dupa_gen(self, gen):
        return [film for film in self.__repo_film.get_all() if film.get_gen().lower() == gen.lower()]


    """
    Cauta un film dupa id

    id_film - int

    returneaza: Film
    eroare: daca filmul cu id-ul dat nu exista
    """
    def cauta_film_dupa_id(self, id_film):
        for film in self.__repo_film.get_all():
            if film.get_id() == id_film:
                return film
        raise ValueError(f"Filmul cu ID-ul {id_film} nu exista.")


    """
    Returneaza toate filmele din lista de filme
    """
    def get_all_filme(self):
        return self.__repo_film.get_all()


    """
    Genereaza un film random pe care il adauga la lista de filme

    returneaza: Film (filmul nou generat)
    """
    def genereaza_film_random(self):
        while True:
            letters= string.ascii_letters
            titlu=''.join(random.choice(letters) for i in range(10))
            id_film=int(random.randint(900,14000))
            descriere=''.join(random.choice(letters) for i in range(20))
            index=int(random.randint(0,7))
            lista_genuri=["thriller","horror","romance","distopic","desen", "comedie", "drama", "politist"]
            gen=lista_genuri[index]
        
            # Verific daca ID-ul exista deja
            try:
                self.cauta_film_dupa_id(id_film)
            except ValueError:
                # Daca nu exista, pot folosi ID-ul generat
                film_nou = Film(id_film, titlu, descriere, gen)
                self.__repo_film.adauga(film_nou)
                return film_nou