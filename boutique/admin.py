from django.contrib import admin
from .models import Categorie, Produit, Commande, ProduitCommande

admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(ProduitCommande)


# Register your models here.
