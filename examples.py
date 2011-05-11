from pychembl.settings import *
from pychembl.db.auto_schema import *

# loop over the first 1000 assays containing the term "human" in their assay description; yield the
# the result in blocks of 25 database rows

assays = session.query(Assays).filter(Assays.description.like('%human%')).limit(1000).yield_per(25)

for assay in assays:
	print "- %s" % (assay.description)
	
print "\n\n\n"


# select all 'Kallikrein 14' target entries (yields only one), find the related assays and print 
# activities and canonical SMILES of the ligand molecules

targets = session.query(TargetDictionary).filter(TargetDictionary.pref_name=='Kallikrein 14').all()

for target in targets:
	print target.description
	for assay in target.assays:
		print assay.description
		print "-------------------------------"
		for activity in assay.activities:
			 smiles = activity.molecule.structure.canonical_smiles
			 print "activity %s %s %s : %s" % (activity.relation, activity.published_value, activity.published_units, smiles) 

	
