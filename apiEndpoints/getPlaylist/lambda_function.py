import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('playlistic-db')

def lambda_handler(event, context):
    """
    This lambda function returns a playlist given userID and playlistID
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

    #query database with userID (partion key) and playlistID (sort key)
    response = table.query(KeyConditionExpression=Key('userID').eq(userID)&Key('playlistID').eq(playlistID))

    #if no playlists are present
    if len(response['Items']) == 0:
        return{
            'statusCode': 400,
            'body': json.dumps("No playlist exists with userID " + userID + " and " + "playlistID " + playlistID)
        }
    
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'][0]['videos'])
    }