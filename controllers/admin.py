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
    form.next = URL('icook','admin','aliments')
    if form.process().accepted:
        response.flash = "L'aliment a bien été ajouté en BDD"
        response.type = 'success'
    elif form.errors:
        response.flash = 'Le formulaire contient des erreurs'
        response.type = 'danger'
    else:
        response.flash = 'Please fill the form'
        response.type = 'warning'
   
    return dict(form=form)

def supprimer_aliment():
    liste_aliments = db(db.aliments).select()

    return dict(
        liste_aliments=liste_aliments,

        )