# -*- coding: utf-8 -*-

# Table ingredient
# Défini un ingrédient
db.define_table('ingredient',
	Field('name','string', requires=IS_NOT_EMPTY()),
	Field('kcals','integer', requires=IS_NOT_EMPTY()),
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

"""
from smarthumb import SMARTHUMB
box = (200, 200)
Files.thumb1.compute = lambda row: SMARTHUMB(row.image1, box)
Files.thumb2.compute = lambda row: SMARTHUMB(row.image2, box)
Files.thumb3.compute = lambda row: SMARTHUMB(row.image3, box)
Files.thumb4.compute = lambda row: SMARTHUMB(row.image4, box)
Files.thumb5.compute = lambda row: SMARTHUMB(row.image5, box)
Files.thumb6.compute = lambda row: SMARTHUMB(row.image6, box)
Files.thumb7.compute = lambda row: SMARTHUMB(row.image7, box)
Files.thumb8.compute = lambda row: SMARTHUMB(row.image8, box)
Files.thumb9.compute = lambda row: SMARTHUMB(row.image9, box)
Files.thumb10.compute = lambda row: SMARTHUMB(row.image10, box)
"""