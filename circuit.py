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
        print("Moteur is dead!!", self.temperature_moteur)

    def accelerer(self, n:float):
        print(f"Température moteur avant accélération : {self.temperature_moteur:.2f}") 
        self._vitesse += n
        self._temperature_moteur = (self._temperature_pneumatique * 0.09) * (self._vitesse * 0.11)
        print(f"Vitesse après accélération : {self._vitesse:.2f} et Température moteur : {self._temperature_moteur:.2f}")

        if self.temperature_moteur > 360:
           self.moteur_is_dead()

    def DRS(self):
        print(f"Température moteur avant DRS : {self.temperature_moteur:.2f}")  
        vitesse_avant_DRS = self._vitesse  # Sauvegarde la vitesse avant DRS
        self.accelerer(self._vitesse * 0.15)  # Augmente la vitesse de 15%
        print(f"Vitesse après accélération DRS : {self._vitesse:.2f} et Température moteur : {self._temperature_moteur:.2f}")
        print(f"Vitesse avant DRS : {vitesse_avant_DRS:.2f}, Vitesse après DRS : {self._vitesse:.2f}")
        if self.temperature_moteur > 360:
           self.moteur_is_dead()

    def depassement(self, pilote: 'F1'):
        if  self.position < pilote.position:
         
            try:
                self.position = pilote.position 
                pilote.position += 1
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
  

    def depassement(self, pilote: 'F1'):
        
        if self.position < pilote.position:
            print("Vous devriez être derrière le pilote à dépasser !")
            return

        # Effectuer le dépassement
        try:
            self.position = pilote.position
            pilote.position += 1
            self._temperature_pneumatique -= self._temperature_pneumatique * 0.08  # Diminution des températures pneumatique
            print(f"Dépassement réussi ! {self.nom} est maintenant en position {self.position}")
        except ValueError as e:
            print(f"Erreur de dépassement : {e}")


    
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
        self._position = self._position + 1
        print(f"Température pneumatique : {self._temperature_pneumatique}, Vitesse : {self._vitesse}, Position : {self._position}")


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
        self._position = self._position + 1 
        self._vitesse -= random.uniform(5, 12)
        print(f"Température pneumatique : {self.temperature_pneumatique}, Vitesse : {round(self.vitesse)}, Position : {self.position}")

    def depasser_autre_ecurie(self):
             self.temperature_pneumatique -= self.temperature_pneumatique * 0.11
             self.position = self.position + 1

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
    #RedBull est en position 3
    redbull = RedBull(position=3, temperature_moteur=90.0)
    #Mercedes est en position 2
    mercedes = Mercedes(position=2, temperature_moteur=85.0)
    #Ferrari est en position 1
    ferrari = Ferrari(position=1, temperature_moteur=80.0)
    print(redbull)  
    print(mercedes)  
    print(ferrari) 
    print("Position actuelle de Redbull :", redbull.position)
    print("Position actuelle de Mercedes :", mercedes.position) 
    print("Position actuelle de Ferrari :", ferrari.position)  
    #Redbull dépasse Mercedes
    print("Redbull accélère :", redbull.accelerer(10.5))
    print("Redbull dépasse Mercedes :", redbull.depassement(mercedes))
    #Mercedes subi un dépassement de Redbull
    print("Mercedes subi un dépassement de Redbull :", mercedes.subir_depassement_RedBull())
    #Redbull accélère encore
    print("Redbull accélère :", redbull.DRS())
    print("Redbull accélère", redbull.accelerer(50))
    #Redbull dépasse Ferrari
    print("La position actuelle de RedBull", redbull.position)
    print("Redbull a dépassé Ferrari :", redbull.depassement(ferrari))
    #Ferrari subi un dépassement de Redbull
    print("Ferrari subi un dépassement de Redbull :", ferrari.subir_depassement_RedBull())
    print("Ferrari subi un dépassement de Redbull :", ferrari.subir_depassement_RedBull())
    print("Redbull accélère", redbull.accelerer(50))
    print("La position actuelle de RedBull", redbull.position)
    print("RedBull continue à s'accélérer...", redbull.DRS())
    print("Température moteur: ", redbull.temperature_moteur)
    #Redbull a gagné la course!!!

    
  

   
