from flask import Flask, render_template, request
from pyArango.connection import *
from pyArango.collection import Edges, Field
from pyArango.graph import Graph, EdgeDefinition


app = Flask( __name__ )

ARANGOURL='http://localhost:8001'
conn = Connection( arangoURL=ARANGOURL)

DATABASE="mydb"
VTXCOLLECTION="MyVertices"

class Connection ( Edges ):
    _field = { 'weight' : Field() }

class MyGraph (Graph ) :
    _edgeDefinitions =( EdgeDefinition( "Connection", fromCollections = [ VTXCOLLECTION ], toCollections = [ VTXCOLLECTION ] ), )
    _orphanedCollections = []


db = conn[ DATABASE ]
vtx = db[ VTXCOLLECTION ]

EDGECOLLECTION="Connection"
edges = db[ EDGECOLLECTION ]

GRAPH="MyGraph"
graph = db.graphs[ GRAPH ]

active = vtx[ "Key_4" ]


def createNewVtx ( request ):
    doc = vtx.createDocument()
    doc[ "name" ] = request.form.get("name")
    doc[ "number" ] = request.form.get("number")
    doc.save()
    return doc

def linkNewVtx ( old, new ) :
    graph.link( EDGECOLLECTION, old, new, { "weight" : 0.5 } )
   
def getPostsAround ( tvtx ):
    dist = 0.2
    return [ vtx[ v[ "_key" ] ] for v in graph.traverse( tvtx, direction = "outbound", itemOrder = "backward",
        uniqueness = { vertices : "global" }, :q
        )[ "visited" ][ "vertices" ] ]

@app.route("/")
def home_view () :
    return render_template( "base.html" )

@app.route( "/bootstrap" )
def bootstrap () :
    return render_template( "bootstrap.html" ) 

@app.route( "/project", methods = [ "GET", "POST" ] )
def view () :
    if request.method == "GET" :
        return render_template("project.html", users=getPostsAround( active ) )
    elif request.method == "POST" :
        new = createNewVtx( request )
        linkNewVtx( active, new )

        return render_template("project.html", users=getPostsAround( active ) )
