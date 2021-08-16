"""display module allowing interaction with the player"""
from views.display import Display


class Menu:

    """Class menu to offer the different choices to the player.
    """

    def main_user(self):

        """method showing the possible choices to the player.
        Detects with a condition if the user input matches
        one of the expected choices.
        return: str or False  """

        userchoice = input("Veuillez faire votre choix :\n \
            1/ voir mes favoris\n \
            2/ rechercher un substitut\n \
            3/ réinitilisation de la base de donnée\n \
                Note: Pour revenir au menu principal appuyer sur q\n")

        possibility = ("1", "2", "3", "q")

        if userchoice in possibility:
            return userchoice
        else:
            return False

    def name_database(self):

        """method requesting the name of the player's database.
        return:(str) the choice user for the database's name """

        userchoice = input("Merci d'inscrire le nom \
        de votre base de donnée:\n")

        return userchoice

    def generic_choice(self, liste):

        """generic method allowing to make a choice
        among a list of object put in argument.
        With a condition, the user enters their choice
        which is returned or return to the main menu
        by pressing q which returns False.

        args:
        -message (list): contains the list of objects to select

        return: (str or False) choice utilisateur or False."""

        print("Veuillez faire votre choix \
        et inscrire le numéro correpondant: ")

        for element in liste:
            print(element.id, ":", element.name)

        userchoice = input("")

        if userchoice == "q":
            return False
        else:
            return userchoice

    def saved_substitute(self):

        """method asking the user if he wants to save his substitute.
        With a condition, returns the user's choice
        if it is in the list otherwise False

        return str or False """

        userchoice = input("Souhaitez vous enregistrer le résultat de votre recherche? \n \
        Pour oui tappez o pour non tappez n\n ")

        possibility = ("o", "n", "q")

        if userchoice in possibility:
            return userchoice
        else:
            display = Display()
            display.retry()
            self.saved_substitute()
