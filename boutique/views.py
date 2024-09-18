from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Categorie, Commande, ProfilUtilisateur, ProduitImage, ProduitCommande  # Ajout des modèles manquants
from .forms import ProduitForm, CategorieForm
from django.db.models import Q


def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')  # Récupérer les images multiples
        if form.is_valid():
            produit = form.save()  # Sauvegarder le produit
            # Sauvegarder chaque image
            for image in images:
                ProduitImage.objects.create(produit=produit, image=image)
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'ajouter_produit.html', {'form': form})

def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'modifier_produit.html', {'form': form})

def supprimer_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'supprimer_produit.html', {'produit': produit})

def liste_produits(request):
    query = request.GET.get('q')
    categorie_id = request.GET.get('categorie')

    produits = Produit.objects.all()

    if query:
        produits = produits.filter(Q(nom__icontains=query) | Q(description__icontains=query))  # Correction du filtre pour plusieurs champs
    
    if categorie_id:
        produits = produits.filter(categorie_id=categorie_id)

    categories = Categorie.objects.all()
    return render(request, 'boutique/produits.html', {'produits': produits, 'categories': categories})

def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm()
    return render(request, 'ajouter_categorie.html', {'form': form})

def modifier_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'modifier_categorie.html', {'form': form})

def supprimer_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('liste_categories')
    return render(request, 'supprimer_categorie.html', {'categorie': categorie})

def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'liste_categories.html', {'categories': categories})

def passer_commande(request):
    if request.method == 'POST':
        adresse_livraison = request.POST.get('adresse_livraison')
        panier = request.session.get('panier', {})

        if not panier:
            return redirect('panier_vide')
        
        total = sum(Produit.objects.get(pk=prod_id).prix * quantite for prod_id, quantite in panier.items())

        commande = Commande.objects.create(
            utilisateur=request.user,
            adresse_livraison=adresse_livraison,
            total=total
        )

        for prod_id, quantite in panier.items():
            produit = Produit.objects.get(pk=prod_id)
            ProduitCommande.objects.create(
                produit=produit,
                commande=commande,
                quantite=quantite
            )

        request.session['panier'] = {}  # Vider le panier après la commande
        return redirect('confirmation_commande')

    return render(request, 'passer_commande.html')

def confirmation_commande(request):
    return render(request, 'confirmation_commande.html')

def panier_vide(request):
    return render(request, 'panier_vide.html')

def detail_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    return render(request, 'detail_produit.html', {'produit': produit})
