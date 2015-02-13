from xml.etree import cElementTree as xtree

class Binder(object):
    """Class describing binders : select, insert, update, delete
        name : select, insert, update, delete
        itemPath : dotted path i.e : products.product
        produces : json or xml 
        urls : list of urls related to the api
        inputs : list of key object
    """

    def __init__(self, name, itemPath, produces, pollingFrequencySeconds=30, urls=[], inputs=[]):
        """Initializes the class
        """
        self.name = name
        self.itemPath = itemPath
        self.pollingFrequencySeconds = pollingFrequencySeconds
        self.produces = produces

    
    def addInput(self, key):
        """Add key element to the binder
        """
        pass

class BinderKey(object):
    """Class representing a key which is part of inputs
    """

    def __init__(self, id, type, paramType, required='false', like=''):
        """Initializes the class
        """
        self.id = id
        self.type = type
        self.paramType = paramType
        self.required = required

        self._etree = self._buildElementTree()

    def _buildElementTree(self,):
        """Turns object into ElementTre
        """
        t_key = xtree.Element('key')
        for item in self.__dict__.items():
            t_key.set(*item)
        
        return t_key
        
    def to_elementTree(self,):
        """Returns object as ElementTree
        """
        return self.etree



    