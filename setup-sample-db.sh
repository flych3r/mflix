#!bin/bash

wget https://atlas-education-staging.s3.amazonaws.com/sampledata.archive.gz
docker cp sampledata.archive.gz mongodb_devcontainer_db_1:sampledata.archive.gz
docker exec -it mongodb_devcontainer_db_1 mongorestore --gzip --archive=sampledata.archive.gz
