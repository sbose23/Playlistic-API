"""
This file executes the database functions for testing functionality on local machine
"""

import databaseFunctions as db

print("-------------------------------------------\nStart of operations:\n")

def makeTable():
    db.createTable()
    db.initializeTable()
    db.scanTable()

def printUserPlaylists():
    response = db.getUserPlaylists("User1")
    print("-------------------------------------------\nPrinting playlists...\n")
    for playlist in response['Items']:
        print(str(playlist['playlistID']) + ": " + str(playlist['videos']))
    print("-------------------------------------------\nFinished printing playlists.\n")

