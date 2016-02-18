from pyArango.connection import *
from pyArango.collection import Collection, Field, Edges
from pyArango.graph import Graph, EdgeDefinition


# set URL for Arangodb database server
ARANGOURL='http://localhost:8001'
conn = Connection( arangoURL = ARANGOURL )

DATABASE="mydb"
VTXCOLLECTION="MyVertices"

class Connection(Edges):
    _field = { 'weight' : Field() }

EDGECOLLECTION="Connection"

class MyGraph(Graph):
    _edgeDefinitions =( EdgeDefinition( "Connection", fromCollections = [ VTXCOLLECTION ], toCollections = [ VTXCOLLECTION ] ), )
    _orphanedCollections = []

GRAPH="MyGraph"

if conn.hasDatabase( name=DATABASE ) :
    db = conn[ DATABASE ]
else:
    db = conn.createDatabase( name=DATABASE )

if db.hasCollection( name=VTXCOLLECTION ) :
    collection = db[ VTXCOLLECTION ]
else:
    collection = db.createCollection( name=VTXCOLLECTION )
    for i in range(11) :
        doc = collection.createDocument()
        doc[ "name" ] ="Tesla-%d" % i
        doc[ "number" ] = i
        doc._key = "Key_%d" %i
        doc.save()

if db.hasCollection( EDGECOLLECTION ):
    edges = db[ EDGECOLLECTION ]
else:
    edges = db.createCollection( EDGECOLLECTION )

if db.hasGraph( name = GRAPH ):
    graph = db.graphs[ GRAPH ]
else:
    graph = db.createGraph( name=GRAPH )
    for i in range(10):
        doc1 = collection[ "Key_%d" %i ] 
        doc2 = collection[ "Key_%d" %(i+1) ] 
        graph.link( EDGECOLLECTION, doc1, doc2, { "weight" : 0.5 })
