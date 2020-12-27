import pathlib
import requests
import functools
import sys

def get_extension( filepath ):
    ''' get file extension in .py format '''
    return pathlib.Path( filepath ).suffix

def handle_request_exception( logger ):
    ''' handle request exception '''
    def decorator( func ):
        def wrapper( *args, **kwargs ):
            try:
                response = func( *args, **kwargs )
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as err:
                logger.error( err )
                sys.exit( err )
        return wrapper
    return decorator


