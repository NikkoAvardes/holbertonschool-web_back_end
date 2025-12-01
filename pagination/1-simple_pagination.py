
#!/usr/bin/env python3
"""
Module : 1-simple_pagination
Ce module fournit une classe Server pour paginer une base
de données de prénoms populaires.

Fonctions principales :
    - Server.dataset() : Charge et met en cache le dataset CSV.
    - Server.get_page(page, page_size) : Retourne une page de données paginées.
"""
import csv
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Classe Server pour paginer une base de données de prénoms populaires. 

    Attributs :
        DATA_FILE (str): Chemin du fichier CSV contenant les données.
        __dataset (List[List]): Cache du dataset chargé.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialise le serveur et le cache du dataset.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Charge le dataset à partir du fichier CSV et le met en cache.
        Retourne :
            List[List]: Liste des lignes du dataset (hors en-tête).
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retourne une page de données paginées.

        Args:
            page (int): Numéro de la page (commence à 1).
            page_size (int): Nombre d'éléments par page.

        Returns:
            List[List]: Sous-liste du dataset correspondant à la page demandée.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end]
