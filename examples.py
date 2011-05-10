from settings import *

from chembl.db.auto_schema import *

assays = session.query(Assays).yield_per(100).limit(1000)

for assay in assays:
	print "%s %s" % (assay.description, len(assay.targets))
	#os = assay.targets
	#if len(os) > 1:
	#	print len(os)
	#for o in os:
	#	print "  %s" % len(o)
	
#molecules = session.query(MoleculeDictionary).filter(MoleculeDictionary.molregno==480382).all()
		
#i = 1
#for molecule in molecules:
#	print '%s ------------' % i
	#print record.source.src_description
	#print record.doc.journal
	#print len(record.doc.records)
	#print record.molecule.structure.molfile
	#print record.molecule.structure.standard_inchi_key
	#for key in record.molecule.synonyms_by_type.keys():
	#	print key
	
	#print ">>> %s" % molecule.structure.canonical_smiles
	#print "    %s" % molecule.hierarchy.parent.structure.canonical_smiles
	#print "    %s" % molecule.hierarchy.active.structure.canonical_smiles

	
#	i += 1
#	if i == 1000:
#		break

#print i

#print s.chembl_id
#print s.property
#print s.compound_properties
