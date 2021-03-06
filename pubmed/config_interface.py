# -*- coding: utf-8 -*-
"""
TODO:
- document
- provide tkinter interface
"""

#Standard Library Imports
import os
import importlib.machinery #Python 3.3+

from . import errors

try:
    from . import user_config as config
except ImportError:
    #config = {}
    raise errors.InvalidConfig('user_config.py not found')
        
      
if hasattr(config,'config_location'):
    #In this case the config is really only a pointer to another config  
    config_location = config.config_location
    
    if not os.path.exists(config_location):
        raise errors.InvalidConfig('Specified configuration path does not exist')
    
    loader = importlib.machinery.SourceFileLoader('config', config_location)    
    config = loader.load_module()
    

class Config(object):
    
    def __init__(self):        
        self.email = _get(config,'email',None)
        self.tool = _get(config,'tool','Python Scholar Tools')
        self.api_key = _get(config,'api_key',None)

        
def _get(module,name,default_value):

    if hasattr(module,name):
        return getattr(module,name)
    else:
        return default_value