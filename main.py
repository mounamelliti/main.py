from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union 

app=FastAPI()

@app.get("/")
def accueil():
    return {"message": "Bienvenue sur l'API Ecosain 🚀"}

class Categorie(BaseModel):
  id:Union[int,str]
  nom:str

categories=[]

@app.get("/categories")
def get_categories():
    return categories

class Produit(BaseModel):
  id:Union[int,str]
  nom:str
  prix:float
  pesage:float
  description:str
  ingredients:str
  image:str
  categorie:str
  quantite:int

produits=[
    Produit(id="ES01", nom="Détachant pour vêtements", prix=9, pesage= 200, description="Spécialement conçu pour éliminer les taches de stylo et d'encre, ainsi que les taches de sang, de sueur et de nourriture, avant le lavage. Agiter avant utilisation, puis vaporiser le produit directement sur la tache, laisser agir quelques minutes, frotter puis laver comme d'habitude.", ingrdients="aa", image="image1.jpg", categorie="linge", quantite=10),
    Produit(id="ES02", nom="Meuble en bois", prix= 12, pesage= 200, description="Nettoie et fait briller les meubles en bois. Bien agiter avant utilisation, puis vaporiser le produit sur un chiffon doux et appliquer sur le meuble.", ingredients="aa", image="", catégorie="", quantite=10),
    Produit(id="ES03", nom="Désodorisant d'air", prix=7.5 , pesage= 220, description="Désodorise, parfume l'atmosphère et a des propriétés relaxantes et apaisantes.Secouez avant utilisation.", ingredients="aa", image="", catégorie="", quantite=10),
    Produit(id="ES04", nom="Vitres et inox", prix=9, pesage= 200, description="Nettoie les vitres et les surfaces en inox, tout en agissant comme un excellent agent anti-traces. Bien agiter avant utilisation. Vaporiser sur les surfaces en verre ou en inox, puis essuyer avec un chiffon en microfibres, du papier journal ou tout autre chiffon non pelucheux.", ingredients="aa", image="", categorie="", quantite=10),
    Produit(id="ES05", nom= "Lessive vaisselle à la main", prix=18, pesage= 450, description="Nettoie, dégraisse et désodorise efficacement, tout en étant doux pour les mains. Agiter légèrement avant utilisation, appliquer un peu de liquide sur une éponge, puis frotter la vaisselle et rincer à l'eau.", ingredients="aa", image="", categorie="", quantite=10),
    Produit(id="ES06", nom="Détartant WC et salle de bain", prix=15, pesage= 450, description="Nettoie, détartre, parfume, élimine radicalement les taches tenaces, combat les bactéries et fait briller les sanitaires.Appliquer le produit sur les surfaces à traiter, laisser agir quelques minutes, frotter avec une éponge, puis rincer à l'eau.", ingredients="aa", image="", categorie="", quantite=10),
    Produit(id="ES07", nom="Sol", prix=17.5, pesage=450, description="Nettoie et dégraisse tous types de revêtements de sol. Agiter avant utilisation. Utiliser 2 bouchons de ce produit dans un litre d'eau pour nettoyer tous types de revêtements de sol.Conserver dans un endroit frais et sec, à l'abri de la lumière et hors de portée des enfants.", ingredients="aa", image="", categorie="", quantite=10), 
    Produit(id="ES08", nom="Multi-usage", prix=18, pesage= 450, description="Nettoie et élimine la graisse ainsi que les odeurs sur toutes les surfaces de la cuisine, comme les fours, plans de travail, cuisinières, hottes, réfrigérateurs et éviers. Il est également efficace sur les surfaces de la salle de bain, telles que les lavabos, les robinets, etc. Bien agiter avant utilisation. Vaporiser sur la surface à traiter, laisser agir une minute, puis essuyer avec un chiffon ou frotter avec une éponge et rincer.Conserver dans un endroit frais et sec, à l'abri de la lumière et hors de portée des enfants.", ingredients="aa", image="", categorie="", quantite=10),
    Produit(id="ES09", nom="Poudre linge blanc", prix=11, pesage= 300, description="Nettoie, adoucit, dégraisse, désodorise et blanchit le linge blanc. Ajoutez 1 à 4 cuillères à soupe de poudre selon la capacité de votre machine à laver et le degré de salissure de votre linge. Effectuez votre lessive à une température de 60 °C.Conserver dans un endroit frais et sec, à l'abri de la lumière et hors de portée des enfants.", ingredients="aa", image="", categorie="", quantite=10),
    Produit(id="ES010", nom="Désodorisant tapis/canapés/moquettes", prix=12, pesage=350, description="Désodorisant sec pour tapis, canapés et moquettes. Versez la poudre sur toutes les surfaces à désodoriser, laissez agir 2 heures ou plus, puis frottez et passez l'aspirateur pour éliminer la poudre.Conserver dans un endroit frais et sec, à l'abri de la lumière et hors de portée des enfants.", ingredients="aa", image="", categorie="", quantite=10),
    Produit(id="ES011", nom="Poudre vaisselle machine", prix=12, pesage= 300, description="Nettoie, dégraisse et désodorise la vaisselle, évite les traces et lutte contre le calcaire. Remplissez le compartiment à détergent de votre lave-vaisselle jusqu'au repère, conformément aux instructions du fabricant.Conserver dans un endroit frais et sec, à l'abri de la lumière et hors de portée des enfants.", ingredients="aa", image="", categorie="", quantite=10),
    Produit(id="ES012", nom="Poudre linge machine", prix=11 , pesage= 300, description="Nettoie, adoucit, dégraisse et désodorise le linge. Ajoutez 1 à 4 cuillères à soupe de poudre selon la capacité de votre machine à laver et le degré de salissure de votre linge. Exécutez votre routine de lessive comme d'habitude. Conserver dans un endroit frais et sec, à l'abri de la lumière et hors de portée des enfants.", ingredients="aa", image="", categorie="", quantite=10),
    ]

@app.get("/Produits")
def get_Produits():
    return Produits

class Client(BaseModel):
  nom:str
  prenom:str
  email:str
  numéro_tél:int
  adresse:str
  mot_de_passe:str

clients=[]

@app.get("/Clients")
def get_Clients():
    return Clients

from enum import Enum

class StatutCommande(str, Enum):
    en_cours = "en cours"
    confirmée = "confirmée"
    livrée = "livrée"
    annulée = "annulée"

@app.put("/commandes/{id}/statut")
def modifier_statut_commande(id: Union[int,str], nouveau_statut: StatutCommande):
    for c in commandes:
        if c.id == id:
            c.statut = nouveau_statut
            return {"message": f"Statut de la commande {id} mis à jour ✅", "statut": c.statut}
    return {"message": "Commande non trouvée ❌"}

# Liste des produits disponibles avec leurs prix
produits_catalogue = {
    1: 10.0,
    2: 15.5,
    3: 8.75,
    4: 12.0,
    5: 20.0
}

class Commande(BaseModel):
  id: Union[int,str]          #id commande
  client_id:int   #identifiant du client qui a commandé
  produits:list[int]   #liste des produits commandés
  statut: StatutCommande  #statut de la commande(encours de préparation, expédié)
  total:float=0.0

commandes=[]

#voir toutes les commandes
@app.get("/commandes")
def get_commandes():
    return commandes

#voir une commande spécifique par id
@app.get("/commandes/{id}")
def get_commande(id: Union[int,str]):
    for c in commandes:
        if c.id == id:
            return c
    return {"message": "Commande non trouvée ❌"}

# Calcul automatique du total
@app.post("/commandes")
def ajouter_commande(commande: Commande):
    total = 0.0
    for pid in commande.produits:
        if pid in produits_catalogue:
            total += produits_catalogue[pid]
        else:
            return {"message": f"Produit ID {pid} introuvable ❌"}

# Remplacer total dans la commande (tu peux aussi le recalculer)
    commande.total = total
    commandes.append(commande)
    return {"message": "Commande ajoutée avec total calculé ✅","total": total}

class Panier(BaseModel):
   client_id: Union[int,str]
   produits:list[int]

panier=[]

#voir tous les paniers
@app.get("/panier")
def get_panier():
    return panier

#voir le panier d'un client
@app.get("/panier/{client_id}")
def get_panier_client(client_id: Union[int,str]):
    for p in panier:
        if p.client_id == client_id:
            return p
    return {"message": "Aucun panier trouvé pour ce client ❌"}

#ajouter/modifier le panier
@app.put("/panier")
def modifier_panier(nouveau_panier: Panier):
    for i, p in enumerate(panier):  #Parcourt tous les paniers
        if p.client_id == nouveau_panier.client_id:
            panier[i] = nouveau_panier  #Mise à jour si client existe
            return {"message": "Panier mis à jour ✅"}
    panier.append(nouveau_panier)  #Ajout si client non trouvé
    return {"message": "Nouveau panier ajouté ✅"}

#supprimer un panier
@app.delete("/panier/{client_id}")
def supprimer_panier(client_id: Union[int,str]):
    for i, p in enumerate(panier):
        if p.client_id == client_id:
            del panier[i]
            return {"message": f"Panier du client {client_id} supprimé ✅"}
    return {"message": "Aucun panier trouvé pour ce client ❌"}

class Paiement(BaseModel):
  id:int
  commande:int
  montant:float
  mode:str
  date:str

paiements=[]

@app.get("/paiements")
def get_paiements():
    return paiements

class Livraison(BaseModel):
  id:int
  avenue:str
  ville:str
  Gouvernement:str
  code_postal:int
  commande:int

livraisons=[]

@app.get("/livraisons")
def get_livraisons():
  return livraisons

@app.post("/livraisons")
def ajouter_livraison(livraison: Livraison):
    livraisons.append(livraison)
    return {"message": "Livraison ajoutée ✅"}
