from pyArango.Graph import Graph, EdgeDefinition

class MyGraph(Graph):
    __edgeDefinitions =( EdgeDefinition( "Link", fromCollections = [ VTXCOLLECTION ], toCollections = [ VTXCOLLECTION ] ), )
    __orphanedCollections = []
