import toml
import mtodo.auth as auth
import sys
import os
import argparse
from mtodo.app import MSTodoApp
from mtodo.parsetodo  import construct_todos, get_all_pyfiles

def main():
    config = toml.load( 'config.toml' )
    config = config.get( 'config' )

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-l',
        '--list',
        help = 'provide name of the list to which the tasks need to be added'
    )
    parser.add_argument(
        '-p',
        '--path',
        help = 'provide path from which the TODO need to be parsed'
    )
    args = parser.parse_args()

    access_token = auth.msal_auth( config )
    if access_token:
        todoapp = MSTodoApp( access_token ) 
        if args.path and args.list and os.path.exists( args.path ):
            all_modules = get_all_pyfiles( args.path )
            todos = construct_todos( all_modules )
            listid = todoapp.create_list( args.list )
            for todo in todos:
                todoapp.create_task( todo, listid )
        else:
            print( 'no proper args provided' )
    else:
        print( 'unable to get access token' )

if __name__ == '__main__':
    main()


