import mysql.connector
from manager import Manager
from brand import Brand


class BrandManager(Manager):
    
    def save_brand_table(self, liste):

        """enregistre les catégories dans la base de donnée en appelant le constructeur de la classe mère"""

        sql = "INSERT INTO brands (id, name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name=name"
        
        value = liste

        self.cur.executemany(sql, value)

        self.connexion_off.commit()

        print(self.cur.rowcount, "ligne insérée.")

        self.cur.close()

        self.cur = self.connexion_off.cursor()


        liste_name_brands = []
        for element in liste:
            liste_name_brands.append(element[1])

        names = tuple(liste_name_brands)
        query= (
            "SELECT * FROM brands "
            f"WHERE name IN ({', '.join('%s' for _ in names)})" 
        )
        self.cur.execute(query, names)
    
        res = self.cur.fetchall()

        liste_o_brands_id = []
        for element in res:
            liste_o_brands_id.append(Brand(element[1], element[0]))

        return liste_o_brands_id
