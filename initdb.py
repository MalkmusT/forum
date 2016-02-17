from pyArango.connection import *

DATABASE="mydb"
VTXCOLLECTION="MyVertices"
EDGECOLLECTION="MyEdges"
GRAPH="MyGraph"

# set URL for Arangodb database server
ARANGOURL='http://localhost:8001'
conn = Connection( arangoURL=ARANGOURL )

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

if not db.hasCollection( name=EDGECOLLECTION ):
    edges = db.createCollection( name=EDGECOLLECTION )
else:
    edges = db[ EDGECOLLECTION ]

if db.hasGraph( name = GRAPH ):
    graph = db[ GRAPH ]
else:
    graph = db.createGraph( name=GRAPH )
    for doc in collection.fetchAll():
        vtx = graph.creatVertex( edges, doc )
    for i in range(10):
        doc1 = collection[ "Key_%d" %i ] 
        doc2 = collection[ "Key_%d" %(i+1) ] 
        graph.link( edges, doc1, doc2, { "weight" : 0.5 })
