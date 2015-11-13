MONGO_HOST = 'mongosvc'
MONGO_PORT = 27017
MONGO_DBNAME = 'cilog'

XML = False
# Enable CORS for all domains
X_DOMAINS = "*"

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

PUBLIC_METHODS = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']
PUBLIC_ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'POST', 'DELETE']


deploys = {
    'schema': {
        'created': {
            'type': 'string'
        },
        'image': {
            'type': 'string'
        },
        'tag': {
            'type': 'string'
        },
        'namespace': {
            'type': 'string'
        },
        'target': {
            'type': 'string'
        },
        'source': {
            'type': 'string'
        }
    }
}


DOMAIN = {'deploys': deploys, 'dependencies': {}, }
