# -*- coding: utf-8 -*-
def index():


    return dict()

def liste_aliments():
    liste_aliments = db(db.aliments).select()

    return dict(
        liste_aliments=liste_aliments,

        )

def ajouter_aliment():
    form = SQLFORM(db.aliments)
    form.next = URL(c='admin',f='liste_aliments')
    if form.process().accepted:
        response.flash = "L'aliment a bien été ajouté en BDD"
        response.type = 'success'
    elif form.errors:
        response.flash = 'Le formulaire contient des erreurs'
        response.type = 'danger'
    else:
        response.flash = 'Merci de bien vouloir remplir le formulaire'
        response.type = 'warning'
   
    return dict(form=form)

def supprimer_aliment():
    liste_aliments = db(db.aliments).select()

    return dict(
        liste_aliments=liste_aliments,

        )

def liste_recettes():
    print db(db.categories).select()
    liste_recettes = db(db.recettes.categorie.id == db.categories.id & db.recettes.ingredients.id == db.aliments.id).select()
    print liste_recettes
    
    return dict(
        liste_recettes = liste_recettes,

        )

def ajouter_recette():
    link = URL('list_records', args='db')
    form = SQLFORM(db.recettes, linkto=link)
    form.next = URL(c='admin',f='liste_recettes')
    if form.process().accepted:
        response.flash = "La recette a bien été ajouté en BDD"
        response.type = 'success'
    elif form.errors:
        response.flash = 'Le formulaire contient des erreurs'
        response.type = 'danger'
    else:
        response.flash = 'Merci de bien vouloir remplir le formulaire'
        response.type = 'warning'
   
    return dict(form=form)    

def supprimer_recette():
    liste_aliments = db(db.aliments).select()

    return dict(
        liste_aliments=liste_aliments,

        )