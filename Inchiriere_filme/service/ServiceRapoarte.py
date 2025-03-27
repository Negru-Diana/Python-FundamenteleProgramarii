from domain.clienti import Client
from domain.filme import Film
from domain.inchirieri import Inchiriere
from repository.repoClienti import RepoClient
from repository.repoFilme import RepoFilm
from repository.repoInchirieri import RepoInchiriere


class ServiceRapoarte:
    def __init__(self, repo_inchiriere, repo_clienti, repo_filme):
        self.__repo_inchiriere = repo_inchiriere
        self.__repo_clienti = repo_clienti
        self.__repo_filme = repo_filme


    """
    Returneaza un dictionar cu clientii si numarul de filme inchiriate curent (nereturnate)
    Format: {Client: numar_filme_inchiriate}
    """
    def clienti_cu_filme_inchiriate(self):
        clienti_cu_inchirieri = {}
        for inchiriere in self.__repo_inchiriere.get_all():
            # Consider ca o inchiriere este activa daca data de retur este "0000-00-00"
            if inchiriere.get_data_retur() == "0000-00-00":
                cnp_client = inchiriere.get_cnp_client()
                # Cauta clientul dupa CNP
                for client in self.__repo_clienti.get_all():
                    if client.get_cnp() == cnp_client:
                        if client not in clienti_cu_inchirieri:
                            clienti_cu_inchirieri[client] = 0
                        clienti_cu_inchirieri[client] += 1
                        break
        return clienti_cu_inchirieri


    """
    Returneaza o lista de tupluri (Film, numar_inchirieri) ordonata descrescator dupa numar_inchirieri
    """
    def top_filme_inchiriate(self):
        contor_filme = {}
        for inchiriere in self.__repo_inchiriere.get_all():
            id_film = inchiriere.get_id_film()
            for film in self.__repo_filme.get_all():
                if film.get_id() == id_film:
                    if film not in contor_filme:
                        contor_filme[film] = 0
                    contor_filme[film] += 1
                    break

        # Convertesc dictionarul intr-o lista de tupluri
        filme_list = list(contor_filme.items())
        
        # Sortez cu Comb Sort (descrescator dupa numarul de inchirieri)
        self.comb_sort(
            filme_list, 
            key=lambda x: x[1],  # x[1] este numarul de inchirieri
            reverse=True
        )
        
        return filme_list[:3] # Primele 3



    """
    Returneaza primii 30% clienti cu cele mai multe inchirieri (total istoric)
    """
    def top_30_clienti(self):
        contor_clienti = {}
        for inchiriere in self.__repo_inchiriere.get_all():
            cnp_client = inchiriere.get_cnp_client()
            for client in self.__repo_clienti.get_all():
                if client.get_cnp() == cnp_client:
                    if client not in contor_clienti:
                        contor_clienti[client] = 0
                    contor_clienti[client] += 1
                    break

        # Convertesc dictionarul intr-o lista de tupluri
        clienti_list = list(contor_clienti.items())
        
        # Sortez cu Insertion Sort (descrescator dupa numarul de inchirieri)
        self.insertion_sort(
            clienti_list, 
            key=lambda x: x[1],  # x[1] este numarul de inchirieri
            reverse=True
        )
        
        total_clienti = len(self.__repo_clienti.get_all())
        nr_clienti_top = max(1, round(0.3 * total_clienti))
        
        return clienti_list[:nr_clienti_top]





    """
    Sorteaza the_list folosind algoritmul Comb Sort

    the_list - lista cu elemente de sortat
    key - functie care extrage cheia de comparare din fiecare element
    reverse - True (crescator)/False (descrescator)
    """
    @staticmethod
    def comb_sort(the_list,key, reverse): 
        n = len(the_list)
        gap = n
        shrink = 1.3
        swapped = True

        while gap > 1 or swapped:
            gap = max(1, int(gap / shrink))
            swapped = False

            for i in range(n - gap):
                if (key(the_list[i])>key(the_list[i + gap])):
                    the_list[i], the_list[i + gap] = the_list[i + gap], the_list[i]
                    swapped = True

        if reverse:
            the_list.reverse()



    """
    Sorteaza the_list folosind algoritmul Insertion Sort

    the_list - lista cu elemente de sortat
    key - functie care extrage cheia de comparare din fiecare element
    reverse - True (crescator)/False (descrescator)
    """
    @staticmethod
    def insertion_sort(the_list, key, reverse):
        reverse=False
        for i in range(1, len(the_list)):
            current_value = the_list[i]
            position = i

            while position > 0 and (key(the_list[position - 1])>key(current_value)):
                the_list[position] = the_list[position - 1]
                position -= 1

            the_list[position] = current_value

        if reverse:
            the_list.reverse()


