from pychembl.settings import *
from pychembl.db.auto_schema import *

# loop over the first 1000 assays containing the term "human" in their assay description; yield the
# the result in blocks of 25 database rows

assays = chembldb.query(Assays).filter(Assays.description.like('%human%'))

for assay in assays.limit(1000).yield_per(25):
	print "- %s" % (assay.description)
	
print "\n\n\n"


# select all 'Kallikrein 14' target entries (yields only one), find the related assays and print 
# activities and canonical SMILES of the ligand molecules

targets = chembldb.query(TargetDictionary)\
	.filter(TargetDictionary.pref_name=='Kallikrein 14').all()

for target in targets:
	for assay in target.assays:
		for activity in assay.activities:
			print "%s: activitiy %s %s %s : %s" % (
				target.description,
				activity.relation, 
				activity.published_value, 
				activity.published_units,
				activity.molecule.structure.canonical_smiles
			)
