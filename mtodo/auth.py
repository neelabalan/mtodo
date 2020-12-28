import msal
import toml
import requests
import json
import sys, os, atexit
from mtodo.logger import Logger

logger = Logger.get_logger( logpath = '/tmp/mtodo-logs.log' )

authority  = 'https://login.microsoftonline.com/common'
scope      = [ 'User.ReadBasic.All', 'Tasks.ReadWrite' ]

def msal_auth( config = '~/.config/mtodo/config.toml' ):
    ''' msal device authentication flow '''
    cache = _check_and_get_cache()
    app = msal.PublicClientApplication(
        client_id   = config[ 'client_id' ],
        authority   = authority,
        token_cache = cache
    )

    accounts = app.get_accounts()
    result = _acquire_token( app, accounts  )

    if not result:
        logger.info( 'No suitable token exists in cache. Getting a new one from AAD' )
        flow = app.initiate_device_flow( scopes = scope )
        if 'user_code' not in flow:
            raise ValueError( 
                'Fail to create device flow. Err: {}'.format(
                    json.dumps( flow, indent = 4 )
                )
            )
        print( flow['message'] )
        result = app.acquire_token_by_device_flow( flow )  

    return result[ 'access_token' ] if 'access_token' in result else None

def _check_and_get_cache( path = '/tmp/mtodo-cache.bin' ):
    cache = msal.SerializableTokenCache()
    if os.path.exists( path ):
        cache.deserialize( open( path, 'r' ).read() )

    atexit.register(
        lambda: open( path, 'w' ).write( cache.serialize() )
        if cache.has_state_changed else None
    )
    return cache

def _acquire_token( app, accounts ):
    ''' acquired toekn using acquire_token_silent '''
    if accounts:
        # print(logger.handlers)
        logger.info( 'Account(s) exists in cache {}'.format( accounts ) )
        chosen = accounts[0]
        result = app.acquire_token_silent( 
            scope, 
            account = chosen
        )
        return result

