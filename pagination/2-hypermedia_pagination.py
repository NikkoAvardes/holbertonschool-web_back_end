#!/usr/bin/env python3
"""
Module : 2-hypermedia_pagination
Ce module fournit une classe Server pour paginer une base de données de
et retourner des informations de pagination au format hypermédia.

Fonctions principales :
    - Server.dataset() : Charge et met en cache le dataset CSV.
    - Server.get_page(page, page_size) : Retourne une page de données paginées.
    - Server.get_hyper(page, page_size) : Retourne une page de données avec
    métadonnées hypermédia.
"""
import csv
import math
import typing

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Classe Server pour paginer une base de données de prénoms populaires
    et fournir des métadonnées hypermédia.

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

    def dataset(self) -> typing.List[list]:
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

    def get_page(self, page: int = 1,
                 page_size: int = 10) -> typing.List[list]:
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

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> typing.Dict[str, typing.Any]:
        """
        Retourne une page de données paginées avec des métadonnées hypermédia.

        Args:
            page (int): Numéro de la page (commence à 1).
            page_size (int): Nombre d'éléments par page.

        Returns:
            Dict[str, Any]: Dictionnaire contenant la page de
            données et les métadonnées :
                - page_size : nombre d'éléments dans la page
                - page : numéro de la page courante
                - data : liste des éléments de la page
                - next_page : numéro de la page suivante ou None
                - prev_page : numéro de la page précédente ou None
                - total_pages : nombre total de pages
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
