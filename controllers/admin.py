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


def upload_file():
    """
    File upload handler for the ajax form of the plugin jquery-file-upload
    Return the response in JSON required by the plugin
    """
    try:
        # Get the file from the form
        f = request.vars['files[]']
         
        # Store file
        id = db.files.insert(doc = db.files.doc.store(f.file, f.filename))
         
        # Compute size of the file and update the record
        record = db.files[id]
        path_list = []
        path_list.append(request.folder)
        path_list.append('uploads')
        path_list.append(record['doc'])
        size =  shutil.os.path.getsize(shutil.os.path.join(*path_list))
        File = db(db.files.id==id).select()[0]
        db.files[id] = dict(sizeFile=size)
        db.files[id] = dict(sessionId=response.session_id)
         
        res = dict(files=[{"name": str(f.filename), "size": size, "url": URL(f='download', args=[File['doc']]), "thumbnail_url": URL(f='download', args=[File['thumb']]), "delete_url": URL(f='delete_file', args=[File['doc']]), "delete_type": "DELETE" }])
         
        return gluon.contrib.simplejson.dumps(res, separators=(',',':'))

    except:
        return dict(message=T('Upload error'))
 
 
def delete_file():
    """
    Delete an uploaded file
    """
    try:
        name = request.args[0]
        db(db.files.doc==name).delete()
        return dict(message=T('File deleted'))
    except:
        return dict(message=T('Deletion error'))