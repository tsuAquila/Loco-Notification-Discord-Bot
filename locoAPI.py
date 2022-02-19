import requests
import json
from time import time, sleep

# streamerID = input("Enter the StreamerID: ")

async def stream(streamerID):
  response = requests.post("https://wrapapi.com/use/tsuAquila/locoapi/streamers/0.1.0", json={
  "streamerName": streamerID,
  "wrapAPIKey": "Lwk29zg2OOVXF4nps448ObemSIfTUqtu"
  }).json()
  latency = requests.get('https://wrapapi.com/use/tsuAquila/locoapi/streamers/0.1.0')

  streamer = response["data"]["name"]
  followers = response["data"]["followersViews"][24]
  views = response["data"]["followersViews"][26]
  live = response["data"]["live"][0]
  live1 = live[0:21]
  
  if live1 == "livevideosleaderboard" :
    live1 = live[21:]
    
    if live1 != "This streamer isn’t live right nowCheck out the streamer’s top videos instead!" :
      live3 = "}".join(live1.split("}")[:-1]) + "}"
      liveDict = json.loads(live3)
      liveStatus = True
      streamURL = liveDict['contentUrl']
      streamTitle = liveDict["name"]
      thumbnailURL = liveDict["thumbnailUrl"]
      gameName = liveDict['description']
      streamDateTime = liveDict['uploadDate']
      locoJSON = {
        "streamerID" : streamerID ,
        "streamerName" : streamer ,
        "followers" : followers ,
        "views" : views ,
        "liveStatus" : liveStatus ,
        "streamDetails" : {"streamURL" : streamURL , "streamTitle" : streamTitle , "thumbnailURL" : thumbnailURL , "gameName" : gameName , "streamDateTime" : streamDateTime }
      }

    else :
      liveStatus = False
      locoJSON = {
        "streamerID" : streamerID ,
        "streamerName" : streamer ,
        "followers" : followers ,
        "views" : views ,
        "liveStatus" : liveStatus
      }
  
  else :
    live1 = live[10:]
    
    if live1 != "This streamer isn’t live right nowCheck out the streamer’s top videos instead!" :
      live3 = "}".join(live1.split("}")[:-1]) + "}"
      liveDict = json.loads(live3)
      liveStatus = True
      streamURL = liveDict['contentUrl']
      streamTitle = liveDict["name"]
      thumbnailURL = liveDict["thumbnailUrl"]
      gameName = liveDict['description']
      streamDateTime = liveDict['uploadDate']
      locoJSON = {
        "streamerID" : streamerID ,
        "streamerName" : streamer ,
        "followers" : followers ,
        "views" : views ,
        "liveStatus" : liveStatus ,
        "streamDetails" : {"streamURL" : streamURL , "streamTitle" : streamTitle , "thumbnailURL" : thumbnailURL , "gameName" : gameName , "streamDateTime" : streamDateTime }
      }

    else :
      liveStatus = False
      locoJSON = {
        "streamerID" : streamerID ,
        "streamerName" : streamer ,
        "followers" : followers ,
        "views" : views ,
        "liveStatus" : liveStatus
      }
  with open('locoJSON.json', 'w') as file:
    json.dump(locoJSON, file)
    print("Updated json file at " + streamDateTime)

while True:
  sleep(60 - time() % 60)
  stream(streamerID)