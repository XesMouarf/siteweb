# -*- coding: utf-8 -*-

# Table ingredient
# Défini un ingrédient
db.define_table('aliments',
	Field('name','string', requires=IS_NOT_EMPTY()),
	Field('kcals','integer', requires=IS_NOT_EMPTY()),
	Field('proteines','double', requires=IS_NOT_EMPTY()),
	Field('glucides','double', requires=IS_NOT_EMPTY()),
	Field('lipides','double', requires=IS_NOT_EMPTY())
)

# Table etape
# Défini une étape d'une recette
db.define_table('etape',
	Field('etape','string')
)


# Table catégorie
# Défini la catégorie d'une recette
db.define_table('categorie',
	Field('name','string')
)

# Table recette
# Défini une recette
db.define_table('recette',
	Field('intitule', 'string', requires=IS_NOT_EMPTY()),
	Field('temps_preparation','string', requires=IS_NOT_EMPTY()),
	Field('temps_cuisson','string', requires=IS_NOT_EMPTY()),
	Field('temps_autre', 'string', requires=IS_NOT_EMPTY()),
	Field('categorie', 'reference categorie'),
	Field('nb_personne','integer'),
	Field('commentaires','text'),
	Field('ingredients', 'list:reference ingredient'),
	Field('etapes', 'list:reference etape')
)