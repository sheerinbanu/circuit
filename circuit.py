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
        self._moteur = moteur
        self._temperature_pneumatique = temperature_pneumatique
        self._vitesse = vitesse
        self._position = position
        self._temperature_moteur = (self._temperature_pneumatique * 0.09) * (self._vitesse * 0.11)

    
    @property
    def moteur(self)->str:
        return self._moteur

    @moteur.setter
    def moteur(self, value):
        self._moteur = value

    @property
    def temperature_moteur(self)->float:
        return self._temperature_moteur

    @temperature_moteur.setter
    def temperature_moteur(self, value):
        self._temperature_moteur = value

    @property
    def vitesse(self)->float:
        return self._vitesse

    @vitesse.setter
    def vitesse(self, value):
        if value>=0:
            self._vitesse = value
        else:
            print("La vitesse ne peut pas être négative.")

    @property
    def position(self)->int:
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("La position doit être un entier positif.")
        self._position = value

    @property
    def temperature_pneumatique(self)->float:
        return self._temperature_pneumatique

    @temperature_pneumatique.setter
    def temperature_pneumatique(self, value):
        if value < 0:
            raise ValueError("La température pneumatique ne peut pas être négative.")
        self.temperature_pneumatique = value
        self._temperature_moteur = (self._temperature_pneumatique * 0.09) * (self._vitesse * 0.11)


    def moteur_is_dead(self):
        return self.temperature_moteur > 360

    def accelerer(self, n:float):
        self._vitesse += n

    def DRS(self):
        self.accelerer(self._vitesse*0.15)

    def depassement(self, pilote: 'F1'):
        if  self._position < pilote._position:
         
            try:
                self._position = pilote._position 
                pilote._position += 1
            except ValueError:
                print("Erreur de dépassement")
        else:
            print("Vous devriez être derrière le pilote à dépasser!")

    def __str__(self)->str:
        return (
                
                f"F1(moteur={self._moteur}, "
                f"temperature_pneumatique={self._temperature_pneumatique}, "
                f"vitesse={self._vitesse}, "
                f"temperature_moteur={self._temperature_moteur:.2f}, "
                f"position={self._position})")
    

class RedBull(F1):

    def __init__(self, position, temperature_moteur, moteur = "500cv", temperature_pneumatique = 110, vitesse = 200, nom: str = "RedBull")->None:
        super().__init__(position, temperature_moteur, moteur, temperature_pneumatique, vitesse)
        self.__nom = nom

    @property
    def nom(self):
        return self.__nom
    
    def depasser_mercedes(self):
        self._temperature_pneumatique -= self._temperature_pneumatique * 0.08 

    def depasser_ferrari(self):
        self._temperature_pneumatique -= self._temperature_pneumatique * 0.08 


    def __str__(self)->str:
        return (
            f"Écurie: {self.__nom}\n"
            f"Position: {self._position}\n"
            f"Température moteur: {self._temperature_moteur}°C\n"
            f"Moteur: {self._moteur}\n"
            f"Température pneumatique: {self.temperature_pneumatique}°C\n"
            f"Vitesse: {self._vitesse} km/h")

class Ferrari(F1):

    def __init__(self, position, temperature_moteur, moteur = "500cv", temperature_pneumatique = 110, vitesse = 200, nom: str = "Ferrari")->None:
        super().__init__(position, temperature_moteur, moteur, temperature_pneumatique, vitesse)
        self.__nom = nom

    @property
    def nom(self):
        return self.__nom

    def subir_depassement_RedBull(self):
        self._temperature_pneumatique += self._temperature_pneumatique * 0.12
        baisse_vitesse = random.randint(5,12)
        self._vitesse -= baisse_vitesse 


    def __str__(self)->str:
        return (
            f"Écurie: {self.__nom}\n"
            f"Position: {self._position}\n"
            f"Température moteur: {self._temperature_moteur}°C\n"
            f"Moteur: {self._moteur}\n"
            f"Température pneumatique: {self.temperature_pneumatique}°C\n"
            f"Vitesse: {self._vitesse} km/h")
    

class Mercedes(F1):
    def __init__(self, position, temperature_moteur, moteur = "500cv", temperature_pneumatique = 110, vitesse = 200, nom: str = "Mercedes")->None:
        super().__init__(position, temperature_moteur, moteur, temperature_pneumatique, vitesse)
        self.__nom = nom

    @property
    def nom(self):
        return self.__nom

    def subir_depassement_RedBull(self):
        self._temperature_pneumatique += self._temperature_pneumatique * 0.14 

    def depasser_autre_ecurie(self):
             self._temperature_pneumatique -= self._temperature_pneumatique * 0.11

    def __str__(self)->str:
        return (
            f"Écurie: {self.__nom}\n"
            f"Position: {self._position}\n"
            f"Température moteur: {self._temperature_moteur}°C\n"
            f"Moteur: {self._moteur}\n"
            f"Température pneumatique: {self.temperature_pneumatique}°C\n"
            f"Vitesse: {self._vitesse} km/h")


        
if __name__ == "__main__":
    
    # f1_car1 = F1(1,205.0, 0, 5)
    # f1_car2 = F1(position=2, temperature_moteur=85.0)
    # print(f1_car1)
    # print(f1_car2)
    # print(f1_car1.accelerer(10))    
    # print("\nAprès activation du DRS : ", f1_car1.DRS() )
    redbull = RedBull(position=1, temperature_moteur=90.0)
    mercedes = Mercedes(position=2, temperature_moteur=85.0)
    ferrari = Ferrari(position=3, temperature_moteur=80.0)
    print(redbull)  
    print(mercedes)  
    print(ferrari)  
    
  

   
