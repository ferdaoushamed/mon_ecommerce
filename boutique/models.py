from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image_principale = models.ImageField(upload_to='produits/')  # Image principale
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    promotion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Nouveau champ pour les promotions

    def __str__(self):
        return self.nom  # Corriger la méthode __str__ pour retourner le nom du produit

class ProduitImage(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='produits/images/')

    def __str__(self):
        return f"Image pour {self.produit.nom}"


class ProfilUtilisateur(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.utilisateur.username

class Commande(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit, through='ProduitCommande')
    date_commande = models.DateTimeField(auto_now_add=True)
    adresse_livraison = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Commande {self.id} - {self.utilisateur.username}"

class ProduitCommande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"
    
