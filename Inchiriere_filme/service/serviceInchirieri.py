from domain.inchirieri import Inchiriere
from repository.repoInchirieri import RepoInchiriere
from validators.validatorInchiriere import ValidatorInchiriere


class ServiceInchiriere:
    def __init__(self, repo_inchiriere):
        self.__repo_inchiriere = repo_inchiriere

    def inchiriaza_film(self, id_inchiriere, id_film, cnp_client, data_inchiriere):
        # Initial, data_retur este goala
        noua_inchiriere = Inchiriere(id_inchiriere, id_film, cnp_client, data_inchiriere, "0000-00-00")
        validator = ValidatorInchiriere(noua_inchiriere, self.__repo_inchiriere.get_all())
        if validator.valideaza_id_inchiriere():
            self.__repo_inchiriere.adauga(noua_inchiriere)
        else:
            raise ValueError("ID invalid pentru inchiriere.")

    def returneaza_film(self, id_inchiriere, data_retur):
        gasit = False
        for inchiriere in self.__repo_inchiriere.get_all():
            if inchiriere.get_id() == id_inchiriere:
               # ACtualizez data de retur
                inchiriere_actualizata = Inchiriere(
                    inchiriere.get_id(),
                    inchiriere.get_id_film(),
                    inchiriere.get_cnp_client(),
                    inchiriere.get_data_inchiriere(),
                    data_retur.strip()
                )
                self.__repo_inchiriere.modifica(inchiriere_actualizata, inchiriere)
                gasit = True
                break
        if not gasit:
            raise ValueError("Inchirierea nu a fost gasita.")

    def get_toate_inchirierile(self):
        return self.__repo_inchiriere.get_all()