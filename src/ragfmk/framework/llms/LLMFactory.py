__author__ = "Benoit CAYLA"
__email__ = "admin@datacorner.fr"
__license__ = "MIT"

import importlib
import importlib.resources
import ragfmk.utils.CONST as C
from ragfmk.framework.llms.LLMBaseObject import LLMBaseObject
import json

class LLMFactory():
    
    @staticmethod
    def getInstance(jsonConfig) -> LLMBaseObject:
        """ This function dynamically instanciate the right data Class to create a dynamic object. 
            This to avoid in loading all the connectors (if any of them failed for example) when making a global import, 
            by this way only the needed import is done on the fly
            Args:
                classname (str): full classname (must inherit from the dpInstantiableObj Class)
            Returns:
                Object (dpInstantiableObj): Object
        """
        try:

            # Read the config file
            jparams = json.loads(jsonConfig)
            
            # Get the class to instantiate
            fullClassPath = jparams["pclass"]
            if (fullClassPath == C.NULLSTRING):
                raise Exception("The {} parameter is mandatory and cannot be empty".format(fullClassPath))
            else:
                # Get the latest element : the class name without the path
                llmClass = fullClassPath.split(".")[-1]

            # Instantiate the object
            datasourceObject = importlib.import_module(name=fullClassPath)
            llmClassInst = getattr(datasourceObject, llmClass)
            objectInst = llmClassInst()
            
            # Add the parameters from the config json file
            objectInst.setJSONParameters(jsonConfig)
            # Initialize if necessary
            objectInst.init()
            
            return objectInst
        
        except Exception as e: 
            return None
    