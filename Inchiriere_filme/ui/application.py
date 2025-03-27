from domain.filme import Film
from repository.repoClienti import RepoClient
from repository.repoFilme import RepoFilm
from repository.repoInchirieri import RepoInchiriere
from service.serviceClienti import ServiceClient
from service.serviceFilme import ServiceFilm
from service.serviceInchirieri import ServiceInchiriere
from service.ServiceRapoarte import ServiceRapoarte



def meniu_filme(service_film):
    while True:
        print("\n=== MENIU FILME ===")
        print("1. Adauga film nou")
        print("2. Sterge film")
        print("3. Modifica film")
        print("4. Cauta film")
        print("5. Lista filme")
        print("6. Genereaza film random")
        print("0. Inapoi la MENIU")
        
        optiune = input("\nAlege o optiune: ")
    
    
        try:
            if optiune == "1":
                print("\n--- Adauga film nou ---")
                id_film = input("ID film: ")
                titlu = input("Titlu: ")
                descriere = input("Descriere: ")
                gen = input("Gen: ")
                
                service_film.creeaza_film(id_film, titlu, descriere, gen)
                print("Film adaugat cu succes!")
            
            elif optiune == "2":
                print("\n--- Sterge film ---")
                id_film = input("Introdu ID-ul filmului de sters: ")
                service_film.sterge_film(id_film)
                print("Film sters cu succes!")
            
            elif optiune == "3":
                print("\n--- Modificare film ---")
                id_vechi = input("Introdu ID-ul filmului de modificat: ").strip()
    
                try:
                    film_vechi = service_film.cauta_film_dupa_id(id_vechi)
                    id_nou = input("Noul ID (lasa gol pentru acelasi ID): ").strip() or film_vechi.get_id()
                    titlu_nou = input("Noul titlu (lasa gol pentru acelasi titlu): ").strip() or film_vechi.get_titlu()
                    descriere_noua = input("Noua descriere (lasa gol pentru aceeasi descriere): ").strip() or film_vechi.get_descriere()
                    gen_nou = (input("Noul gen (lasa gol pentru acelasi gen): ").strip().lower() 
                               or film_vechi.get_gen().lower())
        
                    service_film.modifica_film(id_vechi, id_nou, titlu_nou, descriere_noua, gen_nou)
                    print("Film modificat cu succes!")
        
                except ValueError as ve:
                    print(f"Eroare: {ve}")
            
            elif optiune == "4":
                print("\n--- Cauta film ---")
                print("1. Cauta dupa titlu")
                print("2. Cauta dupa gen")
                sub_optiune = input("Alege tipul de cautare (1 sau 2): ")
    
                try:
                    if sub_optiune == "1":
                        titlu_cautat = input("Introdu titlul filmului: ")
                        filme = service_film.cauta_filme_dupa_titlu(titlu_cautat)
                        tip_cautare = f"cu titlul '{titlu_cautat}'"
            
                    elif sub_optiune == "2":
                        gen_cautat = input("Introdu genul filmelor: ")
                        filme = service_film.cauta_filme_dupa_gen(gen_cautat)
                        tip_cautare = f"din genul '{gen_cautat}'"
            
                    else:
                        print("Optiune invalida!")
                        return

                    if len(filme) > 0:
                        print(f"\nAu fost gasite {len(filme)} filme {tip_cautare}:")
                        for film in filme:
                            print(f"ID: {film.get_id()}")
                            print(f"Titlu: {film.get_titlu()}")
                            print(f"Descriere: {film.get_descriere()}")
                            print(f"Gen: {film.get_gen()}")
                            print("-----------------------")
                    else:
                        print(f"\nNu exista filme {tip_cautare}.")

                except Exception as e:
                    print(f"Eroare la cautare: {str(e)}")

            elif optiune == "5":
                print("\n--- Lista tuturor filmelor ---")
                filme = service_film.get_all_filme()
                if not filme:
                    print("Nu exista filme in lista!")
                else:
                    for film in filme:
                        print(f"ID: {film.get_id()}")
                        print(f"Titlu: {film.get_titlu()}")
                        print(f"Descriere: {film.get_descriere()}")
                        print(f"Gen: {film.get_gen()}")
                        print("-----------------------")

            elif optiune == "6":
                try:
                    film_nou = service_film.genereaza_film_random()
                    print(f"A fost generat un film random cu titlu {film_nou.get_titlu()}\n")
                except Exception as e:
                    print("\nA aparut o eroare la generarea unui nou film!\n")
            
            elif optiune == "0":
                return
            
            else:
                print("Optiune invalida! Te rog sa alegi un numar intre 0 si 6.")
        
        except ValueError as ve:
            print(f"\nEroare: {ve}")
        except Exception as e:
            print(f"\nA aparut o eroare neasteptata: {str(e)}")



def meniu_clienti(service_client):
    while True:
        print("\n=== MENIU CLIENTI ===")
        print("1. Adauga client")
        print("2. Sterge client")
        print("3. Modifica client")
        print("4. Cauta client")
        print("5. Lista clienti")
        print("6. Genereaza client random")
        print("0. Inapoi la MENIU")
        
        optiune = input("\nAlege o optiune: ")
        
        try:
            if optiune == "1":
                print("\n--- Adauga client ---")
                id_client = input("ID client: ").strip()
                nume = input("Nume: ").strip()
                cnp = input("CNP: ").strip()
                
                service_client.adauga_client(id_client, nume, cnp)
                print("Client adaugat cu succes!")
            
            elif optiune == "2":
                print("\n--- Sterge client ---")
                id_client = input("Introdu ID-ul clientului de sters: ").strip()
                service_client.sterge_client(id_client)
                print("Client sters cu succes!")
            
            elif optiune == "3":
                print("\n--- Modifica client ---")
                id_vechi = input("Introdu ID-ul clientului de modificat: ").strip()
                
                try:
                    client_vechi = service_client.cauta_client_dupa_id(id_vechi)
                    
                    id_nou = input("Noul ID (lasa gol pentru acelasi ID): ").strip() or client_vechi.get_id()
                    nume_nou = input("Noul nume (lasa gol pentru acelasi nume): ").strip() or client_vechi.get_nume()
                    cnp_nou = input("Noul CNP (lasa gol pentru acelasi CNP): ").strip() or client_vechi.get_cnp()
                    
                    service_client.modifica_client(id_vechi, id_nou, nume_nou, cnp_nou)
                    print("Client modificat cu succes!")
                
                except ValueError as ve:
                    print(f"Eroare: {ve}")
            
            elif optiune == "4":
                print("\n--- Cauta client ---")
                print("1. Cauta dupa nume")
                print("2. Cauta dupa CNP")
                sub_opt = input("Alege tipul de cautare (1 sau 2): ")
                
                try:
                    if sub_opt == "1":
                        search_str = input("Nume: ").strip()
                        clienti = service_client.cauta_clienti_dupa_string(search_str)
                        tip_cautare = f"pentru '{search_str}'"
                    
                    elif sub_opt == "2":
                        cnp = input("Introdu CNP-ul: ").strip()
                        clienti = [service_client.cauta_client_dupa_cnp(cnp)]
                        tip_cautare = f"cu CNP-ul '{cnp}'"
                    
                    else:
                        print("Optiune invalida!")
                        continue
                    
                    if clienti:
                        print(f"\nRezultate cautare {tip_cautare}:")
                        for client in clienti:
                            print(f"ID: {client.get_id()}")
                            print(f"Nume: {client.get_nume()}")
                            print(f"CNP: {client.get_cnp()}")
                            print("-------------------")
                    else:
                        print("\nNu s-au gasit rezultate!")
                
                except Exception as e:
                    print(f"Eroare la cautare: {str(e)}")
            
            elif optiune == "5":
                print("\n--- Lista tuturor clientilor ---")
                clienti = service_client.get_all_clienti()
                if not clienti:
                    print("Nu exista clienti in lista!")
                else:
                    for client in clienti:
                        print(f"ID: {client.get_id()}")
                        print(f"Nume: {client.get_nume()}")
                        print(f"CNP: {client.get_cnp()}")
                        print("-------------------")

            elif optiune == "6":
                try:
                    client_nou = service_client.genereaza_client_random()
                    print(f"A fost generat un client random cu numele {client_nou.get_nume()}\n")
                except Exception as e:
                    print("\nA aparut o eroare la generarea unui nou client!\n")
            
            elif optiune == "0":
                return
            
            else:
                print("Optiune invalida! Te rog sa alegi un numar intre 0 si 6.")
        
        except ValueError as ve:
            print(f"\nEroare: {ve}")
        except Exception as e:
            print(f"\nA aparut o eroare neasteptata: {str(e)}")
    


def meniu_inchirieri(service_inchiriere, service_film, service_client):
     while True:
        print("\n=== MENIU INCHIRIERI ===")
        print("1. Inchiriaza film")
        print("2. Returneaza film")
        print("3. Afiseaza toate inchirierile")
        print("0. Inapoi la MENIU")
        
        optiune = input("\nAlege o optiune: ")
        
        try:
            if optiune == "1":
                print("\n--- Inchiriaza film ---")
                id_inchiriere = input("ID inchiriere: ").strip()
                id_film = input("ID film: ").strip()
                cnp_client = input("CNP client: ").strip()
                data_inchiriere = input("Data inchiriere (ex. 2024-01-01): ").strip()
                
                # Verific daca filmul exista
                try:
                    service_film.cauta_film_dupa_id(id_film)
                except ValueError:
                    print("Eroare: Filmul nu exista.")
                    continue
                
                # Verific daca clientul exista
                try:
                    service_client.cauta_client_dupa_cnp(cnp_client)
                except ValueError:
                    print("Eroare: Clientul nu exista.")
                    continue
                
                # Adaug inchirierea
                try:
                    service_inchiriere.inchiriaza_film(id_inchiriere, id_film, cnp_client, data_inchiriere)
                    print("Film inchiriat cu succes!")
                except ValueError as e:
                    print(f"Eroare: {e}")
            
            elif optiune == "2":
                print("\n--- Returneaza film ---")
                id_inchiriere = input("ID inchiriere: ").strip()
                data_retur = input("Data retur (ex. 2024-01-05): ").strip()
                
                try:
                    service_inchiriere.returneaza_film(id_inchiriere, data_retur)
                    print("Film returnat cu succes!")
                except ValueError as e:
                    print(f"Eroare: {e}")
            
            elif optiune == "3":
                print("\n--- Lista inchirieri ---")
                inchirieri = service_inchiriere.get_toate_inchirierile()
                if not inchirieri:
                    print("Nu exista inregistrari.")
                else:
                    for i, inchiriere in enumerate(inchirieri, 1):
                        print(f"Inchiriere #{i}:")
                        print(f"ID: {inchiriere.get_id()}")
                        print(f"Film ID: {inchiriere.get_id_film()}")
                        print(f"Client CNP: {inchiriere.get_cnp_client()}")
                        print(f"Data inchiriere: {inchiriere.get_data_inchiriere()}")
                        print(f"Data returnare: {inchiriere.get_data_retur()}")
                        print("-----------------------")
            
            elif optiune == "0":
                return
            
            else:
                print("Optiune invalida! Alege 0-3.")
        
        except ValueError as ve:
            print(f"Eroare validare: {ve}")
        except Exception as e:
            print(f"Eroare neasteptata: {e}")



def meniu_rapoarte(service_rapoarte):
    while True:
        print("\n=== MENIU RAPOARTE ===")
        print("1. Clienti cu filme inchiriate curent")
        print("2. Top 3 cele mai inchiriate filme")
        print("3. Top 30% clienti cu cele mai multe inchirieri")
        print("0. Inapoi la MENIU")
        
        optiune = input("\nAlege o optiune: ")
        
        try:
            if optiune == "1":
                print("\n--- Clienti cu filme inchiriate curent ---")
                clienti = service_rapoarte.clienti_cu_filme_inchiriate()
                if not clienti:
                    print("Nu exista clienti cu filme inchiriate in acest moment.")
                else:
                    for client, numar in clienti.items():
                        print(f"Client: {client.get_nume()} (CNP: {client.get_cnp()}) - {numar} filme inchiriate")
            
            elif optiune == "2":
                print("\n--- Top 3 cele mai inchiriate filme ---")
                top_filme = service_rapoarte.top_filme_inchiriate()
                if not top_filme:
                    print("Nu exista filme inchiriate.")
                else:
                    for idx, (film, count) in enumerate(top_filme, 1):
                        print(f"{idx}. {film.get_titlu()} - {count} inchirieri")
            
            elif optiune == "3":
                print("\n--- Top 30% clienti cu cele mai multe inchirieri ---")
                top_clienti = service_rapoarte.top_30_clienti()
                if not top_clienti:
                    print("Nu exista date despre clienti.")
                else:
                    for idx, (client, count) in enumerate(top_clienti, 1):
                        print(f"{idx}. {client.get_nume()} (CNP: {client.get_cnp()}) - {count} inchirieri")
            
            elif optiune == "0":
                return
            
            else:
                print("Optiune invalida! Te rog alege 1-3 sau 0.")
        
        except Exception as e:
            print(f"A aparut o eroare: {str(e)}")



def start():

    # Filme:
    lista_filme = []
    repo_filme = RepoFilm(lista_filme)
    service_film = ServiceFilm(repo_filme)
    repo_filme.citeste_filme_din_fisier() # Inacrc datele existente din fisiere


    # Clienti:
    lista_clienti = []
    repo_clienti = RepoClient(lista_clienti)
    service_client = ServiceClient(repo_clienti)
    repo_clienti.citeste_din_fisier() # Inacrc datele existente din fisiere
    

    # Inchirieri
    lista_inchirieri = []
    repo_inchirieri = RepoInchiriere(lista_inchirieri)
    service_inchiriere = ServiceInchiriere(repo_inchirieri)
    repo_inchirieri.citeste_filme_din_fisier() # Inacrc datele existente din fisiere
   
    # Rapoarte
    service_rapoarte = ServiceRapoarte(repo_inchirieri, repo_clienti, repo_filme)


    while True:
        print("\n=== MENIU ===")
        print("1. Gestiune filme")
        print("2. Gestiune clienti")
        print("3. Gestiune inchirieri")
        print("4. Vizualizeaza rapoarte")
        print("0. Iesire")

        optiune = input("\nAlege o optiune: ")
        
        try:
            if optiune == "1":
                meniu_filme(service_film)

            elif optiune == "2":
                meniu_clienti(service_client)


            elif optiune == "3":
                meniu_inchirieri(service_inchiriere, service_film, service_client)
            

            elif optiune == "4":
                meniu_rapoarte(service_rapoarte)

            
            elif optiune == "0":
                print("\n\nBye :)\n\n")
                break
            
            else:
                print("Optiune invalida! Te rog sa alegi un numar intre 0 si 5.")
        
        except ValueError as ve:
            print(f"\nEroare: {ve}")
        except Exception as e:
            print(f"\nA aparut o eroare neasteptata: {str(e)}")
        



