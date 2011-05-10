from base import *


molecule_dictionary_table = Table('molecule_dictionary', metadata,
	Column('molregno', Integer, primary_key=True, autoincrement=True),
	Column('pref_name', String(255)),
	Column('chembl_id', String(20)),
	Column('max_phase', Integer(unsigned=True))
)

class MoleculeDictionary(object):
	def __init__(self, molregno, pref_name, chembl_id, max_phase):
		self.molregno = molregno
		self.pref_name = pref_name
		
mapper(MoleculeDictionary, molecule_dictionary_table)



