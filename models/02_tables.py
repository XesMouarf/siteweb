# -*- coding: utf-8 -*-

# Table ingredient
# Défini un ingrédient
db.define_table('ingredient',
	Field('name','string', requires=IS_NOT_EMPTY()),
	Field('kcals','double', requires=IS_NOT_EMPTY()),
	Field('proteines','double', requires=IS_NOT_EMPTY()),
	Field('glucides','double', requires=IS_NOT_EMPTY()),
	Field('lipides','double', requires=IS_NOT_EMPTY()),
	format=lambda r: r.name+' prot:'+str(r.proteines)+' gluc:'+str(r.glucides)+' lip: '+str(r.lipides) or None
)

# Table catégorie
# Défini la catégorie d'une recette
db.define_table('categorie',
	Field('name','string', requires=IS_NOT_EMPTY()),
	format=lambda r: r.name or None
)

# Table recette
# Défini une recette
db.define_table('recette',
	Field('intitule', 'string', requires=IS_NOT_EMPTY()),
	Field('temps_preparation','string', requires=IS_NOT_EMPTY()),
	Field('temps_cuisson','string', requires=IS_NOT_EMPTY()),
	Field('temps_autre', 'string'),
	Field('kcals', 'integer', requires=IS_NOT_EMPTY()),
	Field('proteines', 'double', requires=IS_NOT_EMPTY()),
	Field('glucides', 'double', requires=IS_NOT_EMPTY()),
	Field('lipides', 'double', requires=IS_NOT_EMPTY()),
	Field('etapes', 'text', requires=IS_NOT_EMPTY()),
	Field('note', 'integer', default=0),
	Field('vignette', 'upload', autodelete=True, uploadfolder='applications/siteweb/static'),
	Field('image1', 'upload', autodelete=True, uploadfolder='applications/siteweb/static'),
	Field('image2', 'upload', autodelete=True, uploadfolder='applications/siteweb/static'),
	Field('image3', 'upload', autodelete=True, uploadfolder='applications/siteweb/static'),
	Field('image4', 'upload', autodelete=True, uploadfolder='applications/siteweb/static'),
	Field('image5', 'upload', autodelete=True, uploadfolder='applications/siteweb/static'),
	Field('image6', 'upload', autodelete=True, uploadfolder='applications/siteweb/static'),
	Field('image7', 'upload', autodelete=True, uploadfolder='applications/siteweb/static'),
	Field('image8', 'upload', autodelete=True, uploadfolder='applications/siteweb/static'),
	Field('image9', 'upload', autodelete=True, uploadfolder='applications/siteweb/static'),
	Field('image10', 'upload', autodelete=True, uploadfolder='applications/siteweb/static'),
	format=lambda r: r.intitule or None
)

db.define_table('recette_has_categorie',
	Field('recette', 'reference recette'),
	Field('categorie', 'reference categorie')
)

db.define_table('recette_has_ingredient',
	Field('recette', 'reference recette'),
	Field('ingredient', 'reference ingredient'),
	Field('quantite', 'string', requires=IS_NOT_EMPTY())
)
