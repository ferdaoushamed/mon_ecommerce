from django.contrib import admin
from .models import Produit, Categorie, ProduitImage, ProfilUtilisateur, Commande, ProduitCommande

class ProduitImageInline(admin.TabularInline):
    model = ProduitImage
    extra = 1

class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prix', 'stock', 'promotion']
    search_fields = ['nom', 'description']
    inlines = [ProduitImageInline]

admin.site.register(Categorie)
admin.site.register(Produit, ProduitAdmin)  # Enregistre le modèle Produit avec l'admin personnalisé
admin.site.register(ProduitImage)
admin.site.register(ProfilUtilisateur)
admin.site.register(Commande)
admin.site.register(ProduitCommande)
