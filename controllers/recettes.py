# -*- coding: utf-8 -*-
def index():


    return dict()


def ajouter_recette():
    form = SQLFORM(db.recette)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)