# Rodney Vlot Pizza Calculator


#Prijzen van de champignon pizza
SmallchampignonPrijs  = 6.95
MediumchampignonPrijs = 8.70
LargechampignonPrijs   = 11.95
FamilychampignonPrijs     = 12.95
 
# De uitkomst van het menu
print("____________HET MENU____________")
print("----------------Small, 25 cm----------------")
print("--------------------€6.95--------------------")
print("=================================================")
print("---------------Medium, 30 cm---------------")
print("--------------------€8.70-------------------")
print("=================================================")
print("----------------Large, 35 cm----------------")
print("-------------------€11.95-------------------")
print("=================================================")
print("-----------------Family, 40 cm-----------------")
print("-------------------€12.95-------------------")
 
# Het aantal dat besteld world
aantalSmallchampignon  = int(input("Aantal Small champignon Pizza's:  "))
aantalMediumchampignon = int(input("Aantal Medium Champignon Pizza's: "))
aantalLargechampignon   = int(input("Aantal Large champignon Pizza's:   "))
aantalFamilychampignon    = int(input("Aantal Family champignon Pizza's:     "))
 
# Hier word de prijs en het aantal bij elkaar opgeteld
TotaleSmallChampignon  = (SmallchampignonPrijs  * aantalSmallchampignon)
TotaleMediumChampignon = (MediumchampignonPrijs * aantalMediumchampignon)
TotaleLargeChampignon   = (LargechampignonPrijs   * aantalLargechampignon)
TotalelFamilyChampignon     = (FamilychampignonPrijs     * aantalFamilychampignon)
 
# Hier word het hele aantal bij elkaar opgeteld
TotaleBestelling = (TotaleSmallChampignon + TotaleMediumChampignon + TotaleLargeChampignon + TotalelFamilyChampignon)
 
# Prijs de maat van de pizza
print("Subtotaal Small champignon Pizza:    " + " €" + str(TotaleSmallChampignon))
print("==============================================================")
print("Subtotaal Medium champignon Pizza:   " + " €" + str(TotaleMediumChampignon))
print("==============================================================")
print("Subtotaal Large champignon Pizza: " + " €" + str(TotaleLargeChampignon))
print("==============================================================")
print("Subtotaal Family champignon Pizza:   " + " €" + str(TotalelFamilyChampignon))
print("==============================================================")
 
# Hier word het te betalen subtotaal berekend
print("Te betalen bedrag: " + "€" + str(TotaleBestelling))