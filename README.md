# Playlistic-API

This REST API is hosted on AWS and is deployed on the Amazon API Gateway. It serves as the backend for Playlistic. This API is not accessible to the public as both the API domain name and key used to for consuming this API key are private. Under the folder, apiEndpoints, the code for Lambda functions can be found. The documentation for this API is available at https://documenter.getpostman.com/view/18990227/VUqmwKfb. 

# How the API works

When an endpoint of this API is called, the API Gateway first checks that there is a valid API key which is the 'x-api-key' header. Then, if the key is valid and within the assigned rate limit, the request with contents is relayed to the respective Lambda function in an Integration Request. The Lambda function then does whatever it needs to do with the data and returns a response to the API Gateway which is relayed to the caller.

The Lambda functions use the boto3 AWS SDK for calling a DynamoDB instance. 

# The DynamoDB database

The database schema is structured as follows:

* Partition (hash) key: userID
* Sort (range) key: playlistID
* Attributes: playlistName, videos

Each row of this table is one playlist. The partition and sort key combination provides a One-to-Many relationship where each user can have one or more playlists.

Querying or deleting a certain playlist requires both the playlistID and userID. Due to the nature of the database as a key-value store, accessing some playlist is very fast/efficient.

