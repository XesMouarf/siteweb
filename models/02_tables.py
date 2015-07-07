# -*- coding: utf-8 -*-

# Table ingredient
# Défini un ingrédient
db.define_table('ingredient',
	Field('name','string', requires=IS_NOT_EMPTY()),
	Field('kcals','double'),
	Field('sodium','double'),
	Field('magnesium','double'),
	Field('phosphore','double'),
	Field('potasium','double'),
	Field('calcium','double'),
	Field('maganese','double'),
	Field('fer','double'),
	Field('cuivre','double'),
	Field('zinc','double'),
	Field('selenium','double'),
	Field('iode','double'),
	Field('proteines','double'),
	Field('glucides','double'),
	Field('lipides','double'),
	Field('amidon','double'),
	Field('fibre','double'),
	Field('vitamine_d','double'),
	Field('vitamine_e','double'),
	Field('vitamine_k1','double'),
	Field('vitamine_k2','double'),
	Field('vitamine_c','double'),
	Field('vitamine_b1','double'),
	Field('vitamine_b2','double'),
	Field('vitamine_b3','double'),
	Field('vitamine_b5','double'),
	Field('vitamine_b6','double'),
	Field('vitamine_b12','double'),
	Field('vitamine_b9','double'),
	Field('hasmacro','boolean',default=False),
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
