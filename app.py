import requests
import json
from util import handle_request_exception 
from logger import Logger

logger = Logger.get_logger( logpath = '/tmp/mtodo-logs.log' )

class TodoApi:
    def __init__( self, access_token ):
        self.access_token = access_token 
        self.base_url =  'https://graph.microsoft.com/v1.0/me/todo'
        self.headers = { 
            'Content-Type': 'application/json', 
            'Authorization': 'Bearer ' + self.access_token 
        }

    @handle_request_exception( logger )
    def get_task_list( self ):
        ''' get response for all task list '''
        resp = requests.get(
            url = self.get_url_for_api( 'list' ),
            headers = self.headers
        )
        return resp 

    @handle_request_exception( logger )
    def create_task_list( self, tasklist ):
        ''' create task list '''
        resp = requests.post(
            url = self.get_url_for_api( 'list' ),
            data = json.dumps({
                'displayName': tasklist 
            }),
            headers = self.headers,
        )
        return resp

    @handle_request_exception( logger )
    def create_task( self, task, listid ):
        ''' create a task within a list '''
        resp = requests.post(
            self.get_url_for_api( 'task', listid ),
            data = json.dumps({
                'title': task,
            }),
            headers = self.headers,
        )
        return resp

    @handle_request_exception( logger )
    def delete_task( self, list_id, task ):
        ''' delete a task within list '''
        pass

    @handle_request_exception( logger )
    def get_task(self, list_id ):
        ''' get all task from list '''
        pass

    def get_url_for_api( self, call, listid = None ):
        call_map = {
            'list': '{}/lists'.format( self.base_url ),
            'task': '{}/lists/{}/tasks'.format( self.base_url, listid )
        }
        return call_map.get( call )


class MSTodoApp( TodoApi ):
    def __init__( self, access_token ):
        super( MSTodoApp, self ).__init__( access_token = access_token )

    # TODO: return and raise value error or specific exception
    def get_all_lists_and_id( self ):
        response = self.get_task_list()
        if response:
            response_json = response.json()
            todolistdata = [ 
                ( todolist.get( 'displayName' ), todolist.get( 'id' ) ) \
                    for todolist in response_json.get('value')
            ]
            logger.info( todolistdata )
            return todolistdata

    def create_list( self, tasklist ):
        response = self.create_task_list( tasklist ).json()
        return response.get( 'id' )


    # def create_task( self, task_name, list_id ):
    #     pass


    # def get_all_tasks( self, list_name ):
    #     pass
