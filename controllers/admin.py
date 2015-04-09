# -*- coding: utf-8 -*-
def index():
    return dict()

def liste_ingredients():
    liste_ingredients = db(db.ingredient).select()
    return dict(
        liste_ingredients=liste_ingredients,
        )

def ajouter_ingredient():
    form = SQLFORM(db.ingredient)
    form.next = URL(c='admin',f='liste_ingredients')
    if form.process().accepted:
        response.flash = "L'ingrédient a bien été ajouté en BDD"
        response.type = 'success'
    elif form.errors:
        response.flash = 'Le formulaire contient des erreurs'
        response.type = 'danger'
    else:
        response.flash = 'Merci de bien vouloir remplir le formulaire'
        response.type = 'warning'
   
    return dict(form=form)

def supprimer_ingredient():
    liste_ingredients = db(db.ingredient).select()

    return dict(
        liste_ingredients=liste_ingredients,
        )

def liste_recettes():
    recette_has_categorie = db(
        (db.recette.id==db.recette_has_categorie.recette) & (db.categorie.id==db.recette_has_categorie.categorie)).select(groupby=db.recette_has_categorie.recette)

    recette_has_ingredient = db(
        (db.recette.id==db.recette_has_ingredient.recette) & (db.ingredient.id==db.recette_has_ingredient.ingredient)).select(groupby=db.recette_has_ingredient.recette)
    print "recette_has_categorie"
    print recette_has_categorie
    print "recette_has_ingredient"
    print recette_has_ingredient
    recette_complete = db(
        (db.recette.id==db.recette_has_categorie.recette) & (db.categorie.id==db.recette_has_categorie.categorie)\
        & (db.recette.id==db.recette_has_ingredient.recette) & (db.ingredient.id==db.recette_has_ingredient.ingredient))
    liste_recettes = recette_complete.select(orderby=db.recette.id)
    print liste_recettes
    return dict(
        liste_recettes = liste_recettes,
        )

def ajouter_recette():
    liste_ingredients = db(db.ingredient).select()
    liste_categories = db(db.categorie).select()
    print request.vars
    if request.vars['_form'] == '_ajout_recette':
        liste_ingredients_recette = list()
        for var in request.vars:
            if var.startswith('ingredient'):
                liste_ingredients_recette.append({var:request.vars[var]})
        id_recette = db.recette.insert(
            intitule=request.vars['intitule'],
            temps_preparation=request.vars['temps_preparation'],
            temps_cuisson=request.vars['temps_cuisson'],
            temps_autre=request.vars['temps_autre'],
            kcals=request.vars['kcals'],
            proteines=request.vars['proteines'],
            glucides=request.vars['glucides'],
            lipides=request.vars['lipides'],
            etapes=request.vars['etapes']
        )
        for id_categorie in request.vars['categories']:
            db.recette_has_categorie.insert(
                recette=id_recette,
                categorie=id_categorie
            )
        for ingredient in liste_ingredients_recette:
            print ingredient
            ingredient_key = ingredient.keys()[0]
            id_ingredient = int(ingredient_key.split('[')[1].split(']')[0])
            db.recette_has_ingredient.insert(
                recette=id_recette,
                ingredient=id_ingredient,
                quantite=ingredient[ingredient_key]
            )
    '''
    if form.process().accepted:
        response.flash = "La recette a bien été ajouté en BDD"
        response.type = 'success'
    elif form.errors:
        response.flash = 'Le formulaire contient des erreurs'
        response.type = 'danger'
    else:
        response.flash = 'Merci de bien vouloir remplir le formulaire'
        response.type = 'warning'
    '''
    return dict(
        liste_ingredients=liste_ingredients,
        liste_categories=liste_categories
        )    

def supprimer_recette():
    liste_recettes = db(db.recette).select()

    return dict(
        liste_recettes=liste_recettes,

        )

def liste_categories():
    liste_categories = db(db.categorie).select()
    return dict(
        liste_categories=liste_categories,
        )
def ajouter_categorie():
    form = SQLFORM(db.categorie)
    form.next = URL(c='admin',f='liste_categories')
    if form.process().accepted:
        response.flash = "La catégorie a bien été ajouté en BDD"
        response.type = 'success'
    elif form.errors:
        response.flash = 'Le formulaire contient des erreurs'
        response.type = 'danger'
    else:
        response.flash = 'Merci de bien vouloir remplir le formulaire'
        response.type = 'warning'
    return dict(form=form)        

def supprimer_categorie():
    liste_categories = db(db.categorie).select()

    return dict(
        liste_categories=liste_categories,

        )