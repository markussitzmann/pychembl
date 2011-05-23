from pychembl.settings import *
from pychembl.db.auto_schema import *





molecule = chembldb.query(MoleculeDictionary).filter(MoleculeDictionary.molregno==47340).one()

print molecule
print molecule.hierarchy.molecule
print molecule.hierarchy.parent
print molecule.hierarchy.active

print molecule.parent
print molecule.active

print molecule.pref_name
print molecule.parent.pref_name
print molecule.active.pref_name

print molecule.structure.canonical_smiles
print molecule.parent.structure.canonical_smiles
print molecule.active.structure.canonical_smiles

print molecule.property.hba
print molecule.parent.property.hba
print molecule.active.property.hba
