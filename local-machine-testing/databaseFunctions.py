#import python AWS SDK
import boto3
from boto3.dynamodb.conditions import Key

#access DynamoDB resource running at this endpoint on Docker
db = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

#table for later access
table = db.Table('playlistic-local')


def createTable():
    """
    Creates DynamoDB table called 'playlistic-local' with Partion(Hash) key 'userID'
    and Sort(Range) key 'playlistID'
    """

    db.create_table(TableName='playlistic-local',
                    AttributeDefinitions=[{'AttributeName': 'userID', 'AttributeType': 'S'},
                    {'AttributeName': 'playlistID','AttributeType': 'S'}],
                    KeySchema=[{'AttributeName': 'userID','KeyType': 'HASH'},
                    {'AttributeName': 'playlistID','KeyType': 'RANGE'}],
                    ProvisionedThroughput= {'ReadCapacityUnits': 10,'WriteCapacityUnits': 10})
    print("Table Created")


def initializeTable():
    """
    Initializes the table created in createTable() with 3 unique rows
    """

    for i in range(3):
        videos = ["A" + str(i), "B" + str(i), "C" + str(i), "D" + str(i)]
        input = {'userID': 'User' + str(i), 'playlistID': 'Playlist' + str(i), 'videos' : videos}
        table.put_item(Item=input)

    #duplicates of 0 for testing/development
    videos1 = ["A" + str(1), "B" + str(1), "C" + str(1), "D" + str(1)]
    videos2 = ["A" + str(2), "B" + str(2), "C" + str(2), "D" + str(2)]
    input = {'userID': 'User' + str(0), 'playlistID': 'Playlist' + str(1), 'videos' : videos1}
    table.put_item(Item=input)
    input = {'userID': 'User' + str(0), 'playlistID': 'Playlist' + str(2), 'videos' : videos2}
    table.put_item(Item=input)
    print("Initialized Table")


def scanTable():
    """
    Prints the entire database
    """

    print("-------------------------------------------\nDatabase:\n")
    result = table.scan(TableName='playlistic-local')
    for row in result['Items']:
        print(str(row) + '\n')
    print("-------------------------------------------\nFinished printing database\n")

def getUserPlaylists(user):
    """
    Return all playlists belonging to some user
    """

    response = table.query(KeyConditionExpression=Key('userID').eq(user))
    print("Response: " + str(response))
    return response