# Local Machine Testing for DynamoDB

This directory was created for testing functions/operations on a local instance of DynamoDB.

How to do this:

- install the latest version of python and pip
- install boto3 with pip
- install Docker and DynamoDB local (to run the DynamoDB locally) https://hub.docker.com/r/amazon/dynamodb-local/
- an easy way to start up and manage this is to use the DynamoDB desktop app:
  - navigate to Images and hover over amazon/dynamodb-local and click Run. In optional settings, add the Host port as 8000 and then click Run
  - the functions in databaseFunctions.py (and test.py) should work now
  - note that the data is cleared once the DynamoDB container is stopped or restarted which can be done in the Containers tab