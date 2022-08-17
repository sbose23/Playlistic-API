import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('playlistic-db')

def lambda_handler(event, context):
    """
    This lambda function returns playlists belonging to some user
    """
    playlists = {}
    userID = event['headers']['userID']
    response = table.query(KeyConditionExpression=Key('userID').eq(userID))
    for playlist in response['Items']:
        playlists[playlist['playlistID']] = playlist['videos']
    return {
        'statusCode': 200,
        'body': json.dumps(playlists)
    }