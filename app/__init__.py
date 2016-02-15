from flask import Flask, render_template, request
from pyArango.connection import *

DATABASE="mydb"
VTXCOLLECTION="MyVertices"
EDGECOLLECTION="MyEdges"
GRAPH="MyGraph"

app = Flask( __name__ )
conn = Connection()
db = conn[ DATABASE ]
vtx = db[ VTXCOLLECTION ]
edges = db[ EDGECOLLECTION ]
graph = dg[ GRAPH ]

@app.route("/")
def home_view () :
    return render_template( "base.html" )

@app.route( "/bootstrap" )
def bootstrap () :
    return render_template( "bootstrap.html" ) 

@app.route( "/project", methods = [ "GET", "POST" ] )
def view () :
    if request.method == "GET" :
        return render_template("project.html", users=vertices.fetchAll() )
    elif request.method == "POST" :
        doc = db[ VTXCOLLECTION ].createDocument()
        doc[ "name" ] = request.form.get( "name" )
        doc[ "number" ] = request.form.get( "number" )
        doc.save()

        return render_template("project.html", users=vertices.fetchAll() )
