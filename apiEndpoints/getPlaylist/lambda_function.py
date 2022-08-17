import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('playlistic-db')

def lambda_handler(event, context):
    """
    This lambda function returns a playlist given userID and playlistID
    """
    userID = event['headers']['userID']
    playlistID = event['headers']['playlistID']
    response = table.query(KeyConditionExpression=Key('userID').eq(userID)&Key('playlistID').eq(playlistID))
    if len(response['Items']) == 0:
        return{
            'statusCode': 400,
            'body': json.dumps("No playlist exists with userID " + userID + " and " + "playlistID " + playlistID)
        }
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'][0]['videos'])
    }