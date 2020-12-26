import logging
import os
from datetime import datetime

class Logger:

    @staticmethod
    def get_logger( 
        logpath    = '/tmp/{}'.format( datetime.now().strftime('%c').replace( ' ', '-' ) ),
        level      = logging.INFO,
        logformat  = '%(asctime)s - %(levelname)s - %(message)s',
        timeformat = '%d-%m-%Y--%H:%M:%S'
    ):
        logging.basicConfig( 
            filename = logpath, 
            level=logging.INFO,
            format = logformat, 
            datefmt = timeformat
        )
        logger = logging.getLogger( __name__ )
        logger.setLevel( logging.INFO )
        formatter = logging.Formatter( logformat, timeformat )
        handler   = logging.FileHandler( logpath )
        handler.setLevel( level )
        handler.setFormatter( formatter )

        logger.addHandler( handler )
        return logger

    