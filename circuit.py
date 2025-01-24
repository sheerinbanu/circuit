import random

class F1:

    def __init__(self, position: int, temperature_moteur:float, moteur:str = "500cv", temperature_pneumatique: float = 110.0,  vitesse: float = 200.0) ->None:
        '''
            La classe F1 représente une voiture de Formule 1 avec plusieurs attributs liés à ces caractéristiques et performances.
            La constructeur permet de créer une instance de la classe avec les paramètres suivantes:
            - moteur de type str et représentant la puissance théorique du moteur de la F1 définie par défaut à 500cv.
            - temperature_pneumatique de type float et représentant la température initiale des pneus en degrés Celsius, définie par défaut à 110°C.
            - vitesse de type ploat représentant la vitesse actuelle de la F1 en kilomètres par heure, fixée par défaut à 200 km/h.
            - temperature_moteur de type float représeentant la température  calculée dynamiquement à partir de la formule suivante: temperature_moteur=(temperature_pneumatique×0.09)×(vitesse×0.11).
            - position de type int représentant  la position du pilote sur le circuit (place ou rang), initialisée à 1 par défaut.
        
        '''
        self.__moteur = moteur
        self.__temperature_pneumatique = temperature_pneumatique
        self.__vitesse = vitesse
        self.__position = position
        self.__temperature_moteur = (self.__temperature_pneumatique * 0.09) * (self.__vitesse * 0.11)

    
    @property
    def get_moteur(self)->str:
        return self.__moteur

    @get_moteur.setter
    def set_moteur(self, value):
        self.__moteur = value

    @property
    def get_temperature_moteur(self)->float:
        return self.__temperature_moteur

    @get_temperature_moteur.setter
    def set_temperature_moteur(self, value):
        self.__temperature_moteur = value

    @property
    def get_vitesse(self)->float:
        return self.__vitesse

    @get_vitesse.setter
    def set_vitesse(self, value):
        if value>=0:
            self.__vitesse = value
        else:
            print("La vitesse ne peut pas être négative.")

    @property
    def get_position(self)->int:
        return self.__position

    @get_position.setter
    def set_position(self, value):
        self.__position = value

    @property
    def get_temperature_pneumatique(self)->float:
        return self.__temperature_pneumatique

    @get_temperature_pneumatique.setter
    def set_temperature_pneumatique(self, value):
        self.temperature_pneumatique = value

    def moteur_is_dead(self):
        return self.temperature_moteur > 360

    def accelerer(self, n:float):
        self.__vitesse += n

    def DRS(self):
        self.accelerer(self.__vitesse*0.15)

    def depassement(self, pilote: 'F1'):
        if  self.__position < pilote.__position:
         
            try:
                self.__position = pilote.__position 
                pilote.__position += 1
            except ValueError:
                print("Erreur de dépassement")
        else:
            print("Vous devriez être derrière le pilote à dépasser!")

    def __str__(self)->str:
        return (f"F1(moteur={self.__moteur}, "
                f"temperature_pneumatique={self.__temperature_pneumatique}, "
                f"vitesse={self.__vitesse}, "
                f"temperature_moteur={self.__temperature_moteur:.2f}, "
                f"position={self.__position})")
    

class RedBull(F1):

    def __init__(self, position, temperature_moteur, moteur = "500cv", temperature_pneumatique = 110, vitesse = 200)->None:
        super().__init__(position, temperature_moteur, moteur, temperature_pneumatique, vitesse)

    
    def depasser_mercedes(self):
        self.__temperature_pneumatique -= self.__temperature_pneumatique * 0.08 

    def depasser_ferrari(self):
        self.__temperature_pneumatique -= self.__temperature_pneumatique * 0.08 


    def __str__(self)->str:
        return (
            f" RedBull : Position: {self.__position}\n"
            f"Température moteur: {self.__temperature_moteur}°C\n"
            f"Moteur: {self.__moteur}\n"
            f"Température pneumatique: {self.temperature_pneumatique}°C\n"
            f"Vitesse: {self.__vitesse} km/h")

class Ferrari(F1):

    def __init__(self, position, temperature_moteur, moteur = "500cv", temperature_pneumatique = 110, vitesse = 200)->None:
        super().__init__(position, temperature_moteur, moteur, temperature_pneumatique, vitesse)

    def subir_depassement_RedBull(self):
        self.__temperature_pneumatique += self.__temperature_pneumatique * 0.12
        baisse_vitesse = random.randint(5,12)
        self.__vitesse -= baisse_vitesse 


    def __str__(self)->str:
        return (
            f"Ferrari : Position: {self.__position}\n"
            f"Température moteur: {self.__temperature_moteur}°C\n"
            f"Moteur: {self.__moteur}\n"
            f"Température pneumatique: {self.temperature_pneumatique}°C\n"
            f"Vitesse: {self.__vitesse} km/h")
    

class Mercedes(F1):
    def __init__(self, position, temperature_moteur, moteur = "500cv", temperature_pneumatique = 110, vitesse = 200)->None:
        super().__init__(position, temperature_moteur, moteur, temperature_pneumatique, vitesse)

    def subir_depassement_RedBull(self):
        self.__temperature_pneumatique += self.__temperature_pneumatique * 0.14 

    def depasser_autre_ecurie(self):
             self.__temperature_pneumatique -= self.__temperature_pneumatique * 0.11

    def __str__(self)->str:
        return (
            f"Mercedes : Position: {self.__position}\n"
            f"Température moteur: {self.__temperature_moteur}°C\n"
            f"Moteur: {self.__moteur}\n"
            f"Température pneumatique: {self.temperature_pneumatique}°C\n"
            f"Vitesse: {self.__vitesse} km/h")


        
if __name__ == "__main__":
    
    f1_car1 = F1(1,205.0, 0, 5)
    f1_car2 = F1(position=2, temperature_moteur=85.0)
    print(f1_car1)
    print(f1_car2)
    print(f1_car1.accelerer(10))    
    print("\nAprès activation du DRS : ", f1_car1.DRS() )
    
  

   
