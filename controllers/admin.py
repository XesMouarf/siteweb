# -*- coding: utf-8 -*-
from gluon.contrib.markdown.markdown2 import markdown

def index():
    return dict()

def ingredients():
    for i in request.vars:
        db(db.ingredient.id == int(i)).delete()
    liste_ingredients = db(db.ingredient).select()
    return dict(
        liste_ingredients=liste_ingredients,
        )

def ajouter_ingredient():
    form = SQLFORM(db.ingredient)
    form.next = URL(c='admin', f='liste_ingredients')
    if form.process().accepted:
        response.flash = "L'ingrédient a bien été ajouté en BDD"
        response.type = 'success'
    elif form.errors:
        response.flash = 'Le formulaire contient des erreurs'
        response.type = 'danger'
   
    return dict(form=form)

def modifier_ingredient():
    form = SQLFORM(db.ingredient)

    # vérification de l'argument
    try:
        _id = int(request.args[0])
    except:
        raise HTTP(400, "L'ingrédient n'existe pas Kappa")
    if _id <= 0:
        raise HTTP(400, "L'ingrédient n'existe pas Kappa")

    ingredient = db(db.ingredient.id == _id).select()
    try:
        ingredient = ingredient[0]
    except:
        raise HTTP(400, "L'ingrédient n'existe pas Kappa")

    if request.vars['_form_name'] == 'modif':
        ingredient.update_record(
            name=request.vars['name'],
            kcals=request.vars['kcals'],
            proteines=request.vars['proteines'],
            lipides=request.vars['lipides'],
            glucides=request.vars['glucides'])
        redirect(URL(c='admin',f='ingredients'))    
    return dict(
        form=form,
        ingredient = ingredient
        )

def liste_recettes():
    recette_has_categorie = db(
        (db.recette.id==db.recette_has_categorie.recette) & (db.categorie.id==db.recette_has_categorie.categorie)).select(groupby=db.recette_has_categorie.recette)

    recette_has_ingredient = db(
        (db.recette.id==db.recette_has_ingredient.recette) & (db.ingredient.id==db.recette_has_ingredient.ingredient)).select(groupby=db.recette_has_ingredient.recette)

    recette_complete = db(
        (db.recette.id==db.recette_has_categorie.recette) & (db.categorie.id==db.recette_has_categorie.categorie)\
        & (db.recette.id==db.recette_has_ingredient.recette) & (db.ingredient.id==db.recette_has_ingredient.ingredient))

    liste_recettes = recette_complete.select(orderby=db.recette.id)

    return dict(
        liste_recettes = liste_recettes,
        )

def afficher_recette():
    
    recette = db(db.recette.id == request.args[0]).select()
    categories = db((db.categorie.id == db.recette_has_categorie.categorie) & (db.recette.id == db.recette_has_categorie.recette) & (db.recette.id == request.args[0])).select(db.categorie.name,db.categorie.id)
    ingredients = db((db.recette.id==db.recette_has_ingredient.recette) & (db.ingredient.id==db.recette_has_ingredient.ingredient) & (db.recette.id == request.args[0])).select(db.ingredient.name)
    recette[0].note = 4
    recette[0].etapes = XML(markdown(recette[0].etapes))
    return dict(
        recette = recette,
        categories = categories,
        ingredients = ingredients)

def ajouter_recette():
    liste_ingredients = db(db.ingredient).select()
    liste_categories = db(db.categorie).select()
    form = SQLFORM(db.recette)
    
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
            etapes=request.vars['etapes'],
            vignette=request.vars['vignette'],
            image1=request.vars['image1'],
            image2=request.vars['image2'],
            image3=request.vars['image3'],
            image4=request.vars['image4'],
            image5=request.vars['image5'],
            image6=request.vars['image6'],
            image7=request.vars['image7'],
            image8=request.vars['image8'],
            image9=request.vars['image9'],
            image10=request.vars['image10'],
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
        form = form,
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


