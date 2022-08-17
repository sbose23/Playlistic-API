import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('playlistic-db')

def lambda_handler(event, context):
    """
    This lambda function returns playlists belonging to some user
    """

    #playlists dictionary to return to client
    playlists = {}

    #check userID header present
    if 'userID' in event['headers']:
        userID = event['headers']['userID']
    else:
        return {
            'statusCode': 400,
            'body': json.dumps("Header 'userID' not present in request")
        }
    
    #query database with userID (partition key)
    response = table.query(KeyConditionExpression=Key('userID').eq(userID))

    #if no playlists are found
    if len(response['Items']) == 0:
        return {
            'statusCode': 400,
            'body': json.dumps("No playlists found for user with userID " + userID)
        }
    
    #loop through Items and extract playlists with playlistID and corresponding videos list
    for playlist in response['Items']:
        playlists[playlist['playlistID']] = playlist['videos']

    return {
        'statusCode': 200,
        'body': json.dumps(playlists)
    }