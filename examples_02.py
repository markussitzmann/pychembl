from pychembl.settings import *
from pychembl.db.auto_schema import *


print chembldb.query(MoleculeDictionary).count()
print chembldb.query(CompoundStructures).count()
print chembldb.query(CompoundProperties).count()


molecule = chembldb.query(MoleculeDictionary).filter(MoleculeDictionary.molregno==675049).one()

p = molecule.property
s = molecule.structure

print p.alogp
print p.hba
print p.acd_most_apka

print s.standard_inchi
print s.canonical_smiles
print s.molformula


print molecule.property.alogp
print molecule.property.hba
print molecule.property.acd_most_apka

print molecule.structure.standard_inchi
print molecule.structure.canonical_smiles
print molecule.structure.molformula
