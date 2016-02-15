from pyArango.connection import *

DATABASE="mydb"
VTXCOLLECTION="MyVertices"
EDGECOLLECTION="MyEdges"
GRAPH="MyGraph"

conn = Connection()

if not conn.hasDatabase( name=DATABASE ) :
    db = conn.createDatabase( name=DATABASE )
    if not db.hasCollection( name=VTXCOLLECTION ) :
        collection = db.createCollection( name=VTXCOLLECTION )

        for i in range(11):
            doc = collection.createDocument()
            doc[ "name" ] ="Tesla-%d" % i
            doc[ "number" ] = i
            doc._key = "Key_%d" %i
            doc.save
    if not db.hasGraph( name=GRAPH ):
        graph = db.createGraph( name=GRAPH )
        for doc in collection.fetchAll():
            vtx = graph.creatVertex( VTXCOLLECTION, doc )
        for i in range(10):
            doc1 = collection[ "Key_%d" %i ] 
            doc2 = collection[ "Key_%d" %(i+1) ] 
            graph.link( EDGECOLLECTION, doc1, doc2, { "weight" : 0.5 })
