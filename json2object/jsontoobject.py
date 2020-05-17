import json
import copy


def deserialize(data, model):
    '''
    Parameters
    ----------
    data : list of dictionaries of json model, dictionary or json string.
    model : The model that represents the data or empty class.
        
    Raises
    ------
    Exception
        Standard exception when incorrect data is passed.

    Returns
    -------
    Returns a single model of the passed in type or a list of models of the passed in type.

    '''    
    
    if data is None or (isinstance(data, str) and not data.strip()):
        raise Exception('The data passed in is either null or empty.')
    
    if model is None or isinstance(model, str):
        raise Exception('The model passed in is null or a string.')
    
    models = []
    
    if isinstance(data, list): # list of dictionaries that' represent the model
        
        for d in data:
            obj = copy.copy(model)
            
            results = deserialize(d, obj)            
            models.append(results)
        return models
    
    elif isinstance(data, dict): # single model as dictionary type
        
        obj = copy.copy(model)
        
        for k,v in data.items():
            if not isinstance(v, dict) and not isinstance(v, list):
                setattr(obj, k, v)
            
            elif isinstance(v, list): # Handles an attribute that is a list of a model
                attr = getattr(obj, k) # Need to make the list have at least 1 item in the collection to be able to verify object type
                result = deserialize(v, attr[0])
                setattr(obj, k, result)
                
            elif isinstance(v, dict):
                for k1,v1 in v.items():
                    try:                        
                        attr = getattr(obj, k)
                        result = deserialize(v, attr)
                        setattr(obj, k, result)                      
                    except:
                        pass
        return obj

    elif isinstance(data, str):
        
        return deserialize(json.loads(data), model)
    
    else:
        raise Exception('Data representation of model needs to be in a list of dictionaries, dictionary or str json. Check to see if format is correct.')