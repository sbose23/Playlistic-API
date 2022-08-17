import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('playlistic-db')

def lambda_handler(event, context):
    """
    This lambda function deletes a playlist given userID and playlistID
    """

    #check if required headers are present
    if 'userID' in event['headers']:
        userID = event['headers']['userID']
    else:
        return {
            'statusCode': 400,
            'body': json.dumps("Header 'userID' not present in request")
        }

    if 'playlistID' in event['headers']:
        playlistID = event['headers']['playlistID']
    else:
        return {
            'statusCode': 400,
            'body': json.dumps("Header 'playlistID' not present in request")
        }
    table.delete_item(Key={'userID': userID, 'playlistID': playlistID})
    return {
        'statusCode': 200,
        'body': json.dumps("Playlist " + playlistID + " is no more")
    }