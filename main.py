#Pour que ce programme fonctionne correctement, il est important d'installer la librairie prettytable
# la commande pour l'instaler est
# python -m pip install -U prettytable

import copy
from prettytable import PrettyTable

produit={
	"nom" : "aucun",
	"prix" : 0.0,
	"quantite" : 0
}
print("OUTIL DE GENERATION DE FACTURE")
listeProduits=[]
nbreProduits=int(input("Entrer le nombre de produits que vous souhitez facturer: "))
for i in range(0, nbreProduits):
	produitEnCours=copy.deepcopy(produit)
	print("-------------------------------------------------------------------------------")
	print(f'Enregistrement du produit {i+1}/{nbreProduits}')
	produitEnCours["nom"]=input("Entrer le nom du produit: ")
	produitEnCours["prix"]=float(input("Entrer le prix unitaire du produit: "))
	produitEnCours["quantite"]=int(input("Entrer la quantité du produit: "))
	listeProduits.append(produitEnCours)
prixTotal=0

t = PrettyTable(['Nom du produit', 'Prix unitaire', 'quantite', 'Prix total'])
for prod in listeProduits:
	t.add_row([prod["nom"], prod["prix"], prod["quantite"], prod["prix"]*prod["quantite"]])
	prixTotal+=(prod["prix"]*prod["quantite"])
print(t)

print(f'Prix total = {prixTotal} FCFA')
