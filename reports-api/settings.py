import os
MONGO_HOST = os.environ.get('MONGO_SERVICE_HOST')
MONGO_PORT = int(os.environ.get('MONGO_SERVICE_PORT'))

MONGO_DBNAME = 'reports'

XML = False
# Enable CORS for all domains
X_DOMAINS = "*"
X_HEADERS = "Content-Type, Accept, Authorization, X-Requested-With, " \
    " Access-Control-Request-Headers, Access-Control-Allow-Origin, " \
    " Access-Control-Allow-Credentials, X-HTTP-Method-Override, mozSystem, " \
    " Access-Control-Allow-Methods, If-Match "

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

PUBLIC_METHODS = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']
PUBLIC_ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'POST', 'DELETE']

# reports = {
#     'schema': {
#         'build': {'type': 'string'},
#         'branch': {'type': 'string'},
#         'repo': {'type': 'string'},
#         'report': {
#             'type': 'dict',
#             'schema': {
#                 'tests': {'type': 'number'},
#                 'testsuite': {
#                     'type': 'list',
#                     'schema': {
#                         'type': 'dict',
#                         'schema': {
#                             'classname': {'type': 'string'},
#                             'testcase': {'type': 'string'},
#                             'name': {'type': 'string'},
#                             'failure': {
#                                 'type': 'dict',
#                                 'required': False,
#                                 'schema': {
#                                     'failure': {'type': 'string'},
#                                     'type': {'type': 'string'}
#                                 }
#                             }
#                         }
#                     }
#                 }
#             }
#         },
#         'timestamp': {'type': 'string'}
#     }
# }

reports = {
    'schema': {
        'build': {'type': 'string'},
        'branch': {'type': 'string'},
        'repo': {'type': 'string'},
        'report': {'type': 'string'},
        'timestamp': {'type': 'string'}
    }
}

DOMAIN = {'reports': reports}
