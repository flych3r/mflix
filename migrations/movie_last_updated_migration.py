import dateutil.parser as parser
from bson import ObjectId
from pymongo import MongoClient, UpdateOne
from pymongo.errors import InvalidOperation

"""
Ticket: Migration

Update all the documents in the `movies` collection, such that the "lastupdated"
field is stored as an ISODate() rather than a string.

The parser.parse() method can transform date strings into ISODate objects for
us. We just need to make sure the correct operations are sent to MongoDB!
"""

# ensure you update your host information below!
host = 'mongodb://localhost:27017'

# don't update this information
MFLIX_DB_NAME = 'sample_mflix'
mflix = MongoClient(host)[MFLIX_DB_NAME]

# TODO: Create the proper predicate and projection
# add a predicate that checks that the "lastupdated" field exists, and then
# checks that its type is a string
# a projection is not required, but may help reduce the amount of data sent
# over the wire!
predicate = {'lastupdated': {'$exists': True, '$type': 'string'}}
projection = {'lastupdated': 1}

cursor = mflix.movies.find(predicate, projection)

# this will transform the "lastupdated" field to an ISODate() from a string
movies_to_migrate = [
    {
        'doc_id': ObjectId(doc.get('_id')),
        'lastupdated': parser.parse(doc.get('lastupdated', None))
    } for doc in cursor
]
print(f'{len(movies_to_migrate)} documents to migrate')

try:
    # TODO: Complete the UpdateOne statement below
    # build the UpdateOne so it updates the "lastupdated" field to contain
    # the new ISODate() type
    bulk_updates = [UpdateOne(
        {'_id': movie.get('doc_id')},
        {'$set': {'lastupdated': movie.get('lastupdated')}}
    ) for movie in movies_to_migrate]

    # here's where the bulk operation is sent to MongoDB
    bulk_results = mflix.movies.bulk_write(bulk_updates)
    print(f'{bulk_results.modified_count} documents updated')

except InvalidOperation:
    print('no updates necessary')
except Exception as e:
    print(str(e))
