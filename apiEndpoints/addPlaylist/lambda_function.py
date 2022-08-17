import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('playlistic-db')

def lambda_handler(event, context):
    """
    This lambda function adds/updates a playlist given userID, playlistID,
    videos in string format seperated by a hyphen, and a name for the playlist.
    If a playlist with some userID and playlistID already exists it is overwritten.
    """
    headers = event['headers']

    #if required headers are present, add playlist to the table
    if 'userID' in headers and 'playlistID' in headers and 'playlistName' in headers and \
        'videosString' in headers:

        #list object to convert string to list before adding to the table
        videos = []
        if len(headers['videosString']) > 0:
            for video in headers['videosString'].split('-'):
                videos.append(video)
        
        #make playlist item and add it to the table
        playlist = {'userID': headers['userID'], 'playlistID': headers['playlistID'] \
                    , 'videos': videos, 'playlistName': headers['playlistName']}
        table.put_item(Item=playlist)

        return {
            'statusCode': 200,
            'body': json.dumps("Successfully added playlist: " + str(playlist))
        }
    return {
        'statusCode': 400,
        'body': json.dumps("Missing header(s) in request. Request must have 'userID', 'playlistID', \
                            'playlistName', and 'videosString'")
        }
