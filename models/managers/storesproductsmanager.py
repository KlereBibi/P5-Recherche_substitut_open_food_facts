"""this module allows you to interact with the storesproducts's table"""

from models.managers.manager import Manager


class StoresProductsManager(Manager):

    """class to communicate with table StoresProductsManager
        Args:
        -Manager (class parent): initializes the connection to the database """

    def save(self, storesproducts):

        """method to save data in the storesproducts table
        Args:
        - storesproducts (liste) : tuple with id_products and id_stores"""

        cursor = self.connexion.cursor()

        sql = "INSERT INTO stores_products (id_products, id_stores)\
             VALUES (%s, %s)"

        cursor.executemany(sql, storesproducts)

        super().end_request(cursor)
