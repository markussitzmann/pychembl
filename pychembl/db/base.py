from sqlalchemy import create_engine, engine_from_config
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, DateTime, Integer, Float, String, Boolean, TIMESTAMP, MetaData, ForeignKey, UniqueConstraint
from sqlalchemy.types import BLOB as Blob
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref, join, mapper, object_session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sqlalchemy import and_, or_
from sqlalchemy.schema import DDL

from sqlalchemy.databases import mysql

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm.collections import attribute_mapped_collection

try:
	from local_settings import settings
except:
	pass

engine = engine_from_config(settings, 'sqlalchemy.')
Session = sessionmaker(bind=engine)
chembldb = Session()
metadata = MetaData(engine)
