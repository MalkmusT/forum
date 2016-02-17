from pyArango.Collection import Edges

class Connections(Edges):
    _validation = {
            'on_save' : False,
            'on_set' : False,
            'allow_foreign_fields' : True 
            }
    _fields = { 
            'weight' : Field( NotNull = True )
            }

