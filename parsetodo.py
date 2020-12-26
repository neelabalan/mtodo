import os
import codecs
import tokenize
import json

from util   import get_extension 
from logger import Logger
from io     import StringIO

logger = Logger.get_logger( logpath = '/tmp/mitodo-logs.log' )

PYFILE = '.py'

def get_comments( path ):
    ''' get comments from the source file '''
    with open( path ) as source:
        source = StringIO( source ) if not hasattr( source, 'readline' ) else source
        tokenizer = tokenize.generate_tokens(source.readline)
        for token in tokenizer:
            if token[0] == tokenize.COMMENT and 'TODO:' in token.string:
                comment = token.string.split( 'TODO:' )[ -1 ].strip()
                yield token.start[ 0 ], comment


def get_all_pyfiles( dirpath ):
    ''' get all py files in the directory and directores within that directory '''
    ar = list()
    for path, dirs, files in os.walk( dirpath ):
        for filename in files:
            if  get_extension( filename ) == PYFILE: 
                ar.append( os.path.join( path, filename ) )
    return ar

def construct_todos( entries ):
    ''' map todos with files '''
    comment_list = list() 
    for entry in entries:
        if os.path.isfile( entry ):
            with codecs.open( entry, 'r', encoding='utf-8', errors='ignore' ) as file: 
                filename = os.path.basename( entry )
                for line, comment in get_comments( entry ):
                    comment_list.append( 
                        ''.join( 
                            [ 
                                '#', 
                                filename, 
                                ' ', 
                                comment, 
                                ' - Line #', 
                                str( line ) 
                            ] 
                        )
                    )
    logger.info( comment_list )
    return comment_list 
