from django.urls import path
from . import views

urlpatterns = [
    path('ajouter_categorie/', views.ajouter_categorie, name='ajouter_categorie'),
    path('modifier_categorie/<int:pk>/', views.modifier_categorie, name='modifier_categorie'),
    path('supprimer_categorie/<int:pk>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('liste_categories/', views.liste_categories, name='liste_categories'),
    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),
    path('modifier_produit/<int:pk>/', views.modifier_produit, name='modifier_produit'),
    path('supprimer_produit/<int:pk>/', views.supprimer_produit, name='supprimer_produit'),
    path('liste_produits/', views.liste_produits, name='liste_produits'),
    path('passer_commande/', views.passer_commande, name='passer_commande'),
    path('confirmation_commande/', views.confirmation_commande, name='confirmation_commande'),
    path('panier_vide/', views.panier_vide, name='panier_vide'),  # Ajout de l'URL pour panier_vide
    path('produit/<int:pk>/', views.detail_produit, name='detail_produit'),

]
