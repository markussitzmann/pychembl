from base import *

compound_records_table = Table('compound_records', metadata, autoload=True)
class CompoundRecords(object):
	pass


docs_table = Table('docs', metadata, autoload=True)
class Docs(object):
	pass


activities_table = Table('activities', metadata, autoload=True)
class Activities(object):
	pass


molecule_dictionary_table = Table('molecule_dictionary', metadata, autoload=True)
class MoleculeDictionary(object):
	parent = association_proxy('hierarchy', 'parent')
	active_form = association_proxy('hierarchy', 'active')
	active = association_proxy('hierarchy', 'active')

molecule_synonyms_table = Table('molecule_synonyms', metadata, autoload=True)
class MoleculeSynonyms(object):
	pass


molecule_hierarchy_table = Table('molecule_hierarchy', metadata, autoload=True)
class MoleculeHierarchy(object):
	pass


compound_structures_table = Table('compound_structures', metadata, autoload=True)
class CompoundStructures(object):
	pass


compound_properties_table = Table('compound_properties', metadata, autoload=True)
class CompoundProperties(object):
	pass


source_table = Table('source', metadata, autoload=True)
class Source(object):
	pass


assays_table = Table('assays', metadata, autoload=True)
class Assays(object):
	#target_associations = association_proxy('assay2target', 'target')
	pass


assay_type_table = Table('assay_type', metadata, autoload=True)
class AssayType(object):
	pass


assay2target_table = Table('assay2target', metadata, autoload=True)
class Assay2Target(object):
	pass


target_dictionary_table = Table('target_dictionary', metadata, autoload=True)
class TargetDictionary(object):
	pass


curation_lookup_table = Table('curation_lookup', metadata, autoload=True)
class CurationLookup(object):
	pass


confidence_score_lookup_table = Table('confidence_score_lookup', metadata, autoload=True)
class ConfidenceScoreLookup(object):
	pass


relationship_type_table = Table('relationship_type', metadata, autoload=True)
class RelationshipType(object):
	pass


target_class_table = Table('target_class', metadata, autoload=True)
class TargetClass(object):
	pass


target_type_table = Table('target_type', metadata, autoload=True)
class TargetType(object):
	pass


formulations_table = Table('formulations', metadata, autoload=True)
class Formulations(object):
	pass


products_table = Table('products', metadata, autoload=True)
class Products(object):
	pass


chembl_id_lookup_table = Table('chembl_id_lookup', metadata, autoload=True)
class ChEMBLIDLookup(object):
	pass


protein_therapeutics_table = Table('protein_therapeutics', metadata, autoload=True)
class ProteinTherapeutics(object):
	pass


research_codes_table = Table('research_codes', metadata, autoload=True)
class ResearchCodes(object):
	pass


version_table = Table('version', metadata, autoload=True)
class Version(object):
	pass


atc_classification_table = Table('atc_classification', metadata, autoload=True)
class ATCClassification(object):
	pass


define_daily_dose_table = Table('defined_daily_dose', metadata, autoload=True)
class DefinedDailyDoseTable(object):
	pass

####

mapper(Activities, activities_table)

mapper(CompoundStructures, compound_structures_table)

mapper(CompoundProperties, compound_properties_table)

mapper(MoleculeSynonyms, molecule_synonyms_table)

mapper(MoleculeHierarchy, molecule_hierarchy_table, properties={
	'molecule': relationship(MoleculeDictionary, 
		primaryjoin=molecule_hierarchy_table.c.molregno==molecule_dictionary_table.c.molregno,
		backref=backref('hierarchy', uselist=False) 
	),
	'parent': relationship(MoleculeDictionary, 
		primaryjoin=molecule_hierarchy_table.c.parent_molregno==molecule_dictionary_table.c.molregno,
		backref='children'
	),
	'active': relationship(MoleculeDictionary, 
		primaryjoin=molecule_hierarchy_table.c.active_molregno==molecule_dictionary_table.c.molregno,
		backref='base_forms'
	),
})

mapper(MoleculeDictionary, molecule_dictionary_table, properties={
	'property': relationship(CompoundProperties, uselist=False, backref=backref('molecule', uselist=False)),
	'records': relationship(CompoundRecords, backref = 'molecule'),
	'activities': relationship(Activities, backref = 'molecule'),
	'structure': relationship(CompoundStructures, uselist=False, backref = 'molecule'),
	'formulations': relationship(Formulations, backref='molecule'),
	'synonyms': relationship(MoleculeSynonyms, backref='molecule'),
	'synonyms_by_type': relationship(MoleculeSynonyms, collection_class=attribute_mapped_collection('syn_type')),
})

mapper(Formulations, formulations_table)

mapper(Products, products_table, properties={
	'formulations': relationship(Formulations, backref='products'),
})

mapper(CompoundRecords, compound_records_table, properties = {
	'activities': relationship(Activities, backref = 'record')
})

mapper(Docs, docs_table, properties = {
	'records': relationship(CompoundRecords, backref = 'doc'),
	'assays': relationship(Assays, backref = 'doc'),
	'activities': relationship(Activities, backref = 'doc')
})

mapper(Source, source_table, properties = {
	'records': relationship(CompoundRecords, backref = 'source'),
	'assays': relationship(Assays, backref = 'source')
})

mapper(Assays, assays_table, properties = {
	'activities': relationship(Activities, backref='assays'),
	'targets': relationship(TargetDictionary, secondary=assay2target_table, backref='assays'),
	'target_associations': relationship(Assay2Target, collection_class=attribute_mapped_collection('target')),
	'type': relationship(AssayType, backref='assays')
})

mapper(Assay2Target, assay2target_table, properties = {
	'assays': relationship(Assays, backref='assay2target'),
	'targets': relationship(TargetDictionary, backref='assay2target'),
})

mapper(AssayType, assay_type_table)

mapper(TargetDictionary, target_dictionary_table, properties={
	'classes': relationship(TargetClass, backref='target')
})

mapper(CurationLookup, curation_lookup_table, properties={
	'assay2target': relationship(Assay2Target, backref='curator')
})

mapper(ConfidenceScoreLookup, confidence_score_lookup_table, properties={
	'assay2target': relationship(Assay2Target, backref='confidence_score_description')
})

mapper(RelationshipType, relationship_type_table, properties={
	'assay2target': relationship(Assay2Target, backref='relationship')
})

mapper(TargetClass, target_class_table)

mapper(TargetType, target_type_table, properties={
	'targets': relationship(TargetDictionary, backref='type')
})

mapper(ChEMBLIDLookup, chembl_id_lookup_table, properties ={
	'doc': relationship(Docs, backref='chembl_id_lookup', primaryjoin=chembl_id_lookup_table.c.chembl_id==docs_table.c.chembl_id, foreign_keys=[docs_table.c.chembl_id]),
	'target': relationship(TargetDictionary, backref='chembl_id_lookup', primaryjoin=chembl_id_lookup_table.c.chembl_id==target_dictionary_table.c.chembl_id, foreign_keys=[target_dictionary_table.c.chembl_id]),
	'assay': relationship(Assays, backref='chembl_id_lookup', primaryjoin=chembl_id_lookup_table.c.chembl_id==assays_table.c.chembl_id, foreign_keys=[assays_table.c.chembl_id]),
	'molecule': relationship(MoleculeDictionary, backref='chembl_id_lookup', primaryjoin=chembl_id_lookup_table.c.chembl_id==molecule_dictionary_table.c.chembl_id, foreign_keys=[molecule_dictionary_table.c.chembl_id])

})

mapper(ProteinTherapeutics, protein_therapeutics_table)

mapper(ResearchCodes, research_codes_table)

mapper(ATCClassification, atc_classification_table)

mapper(DefinedDailyDoseTable, define_daily_dose_table)