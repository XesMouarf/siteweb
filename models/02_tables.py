# -*- coding: utf-8 -*-

# Table ingredient
# Défini un ingrédient
db.define_table('aliments',
	Field('name','string', requires=IS_NOT_EMPTY()),
	Field('kcals','integer', requires=IS_NOT_EMPTY()),
	Field('proteines','double', requires=IS_NOT_EMPTY()),
	Field('glucides','double', requires=IS_NOT_EMPTY()),
	Field('lipides','double', requires=IS_NOT_EMPTY()),
	format='%(name)s'
)

# Table catégorie
# Défini la catégorie d'une recette
db.define_table('categories',
	Field('name','string', requires=IS_NOT_EMPTY()),
	format='%(name)s'
)

# Table recette
# Défini une recette
db.define_table('recettes',
	Field('intitule', 'string', requires=IS_NOT_EMPTY()),
	Field('temps_preparation','string', requires=IS_NOT_EMPTY()),
	Field('temps_cuisson','string', requires=IS_NOT_EMPTY()),
	Field('temps_autre', 'string', requires=IS_NOT_EMPTY()),
	Field('categorie', 'list:reference categories'),
	Field('kcals', 'integer', requires=IS_NOT_EMPTY()),
	Field('proteines', 'double', requires=IS_NOT_EMPTY()),
	Field('glucides', 'double', requires=IS_NOT_EMPTY()),
	Field('lipides', 'double', requires=IS_NOT_EMPTY()),
	Field('commentaires','text'),
	Field('ingredients', 'list:reference aliments'),
	Field('etapes', 'text')
)

db.recettes.categorie.requires = IS_IN_DB(db,db.categories.id,'%(name)s')
db.recettes.ingredients.requires = IS_IN_DB(db,db.aliments.id,'%(name)s')