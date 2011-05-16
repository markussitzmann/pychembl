from pychembl.settings import *
from pychembl.db.auto_schema import *

molecules = chembldb.query(MoleculeDictionary)
print type(molecules)

print molecules.count()

molecule = molecules.filter(MoleculeDictionary.molregno==675049).all()
molecule = molecules.filter(MoleculeDictionary.molregno==675049).one()
molecule = molecules.filter(MoleculeDictionary.molregno==675049).first()
molecule = molecules.get((675049,))


molecule = chembldb.query(MoleculeDictionary).filter(MoleculeDictionary.molregno==675049).one()

print molecule.molregno
print molecule.pref_name
print molecule.chembl_id
print molecule.first_approval
print molecule.natural_product


molecules = chembldb.query(MoleculeDictionary.chembl_id, MoleculeDictionary.chebi_id)

molecules = chembldb.query(MoleculeDictionary.chembl_id, MoleculeDictionary.chebi_id)
chembl_to_chebi_id_dictionary = dict(molecules.limit(5).all())
print chembl_to_chebi_id_dictionary

