# Python Object oriented programming
Nodarbībā Nr.6 es iepazinos ar objektu orientētu programmēšanu, ar kuru mēs veidojam objekta šablonu un no tā veidojam objektus ar kādām vērtībām.

## Objekta veidošana
Pirmkārt, vajag nodefinēt objekta šablonu ar kādām īpašībām :  
>  
>class PartyAnimal:
>   x = 0
>  
>   def party(self) :
>     self.x = self.x + 1
>     print("So far",self.x)
>  
Lai izveidotu objektu no šablona, vajag piešķirt kādam mainīgajam visas objekta īpašības :  
>  
>an = PartyAnimal()
>  
Arī pastāv objektu radniecība (parent/child objekti). Mēs varam izveidot jaunu objektu (child) ar jau izveidota objekta paplašinājumu (parent). Piemēram, mēs varam PartyAnimal objektu uzrakstīt citā failā un pēc tam importēt to jaunajā failā un paplašināt to :   
>  
>from party import PartyAnimal
>  
>class CricketFan(PartyAnimal):
>   points = 0
>   def six(self):
>      self.points = self.points + 6
>      self.party()
>      print(self.name,"points",self.points)
>  
