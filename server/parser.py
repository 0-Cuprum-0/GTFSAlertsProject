from google.transit import gtfs_realtime_pb2
import requests
import json

def fetchFeed():
    response = requests.get('https://mkuran.pl/gtfs/warsaw/alerts.pb')
    if response.status_code == 200:

        return response
    else:
        return False 


def checkFields(response,feed):
        feed.ParseFromString(response.content)
        s=0
        for entity in feed.entity:
            if entity.HasField('alert') and len(entity.alert.informed_entity) > 0 and entity.alert.description_text  and entity.alert.header_text:
                s+=1
            else:
                return False
        if s == len(feed.entity):
            return True
                #print("Feed fetched and has all the fields nessesary")


def constructAlertsList(feed, alerts, alert_keys, alerts_keys):
    alerts["timestamp"] = feed.header.timestamp
    alerts["alert_list"] = []
    i = 0
    for entity in feed.entity:
        alert_ind = {key: None for key in alert_keys}
        alert_ind["id"] = i
        alert_ind["affected"] = []
        for informed_entity in entity.alert.informed_entity:
            alert_ind["affected"].append(str(informed_entity.route_id))
        alert_ind["title"] = entity.alert.header_text.translation[0].text

        alert_ind["url"] = entity.alert.url.translation[0].text
        #alert_ind["text"] = entity.alert.description_text.translation[0].text 
        #print(alert_ind["title"])
        #print(alert_ind["id"] )
        #print(alert_ind["affected"][0]) prints only the first route id for each
        alerts["alert_list"].append(alert_ind)
        i=1+i

         
    print(alerts)
    with open("../json/data.json", "w") as f:
        json.dump(alerts, f, indent = "     ", ensure_ascii=False)


 




response=fetchFeed()
feed = gtfs_realtime_pb2.FeedMessage()
alerts_keys = ["timestamp", "alert_list"]
alerts ={key: None for key in alerts_keys}
alert_keys =[ "id", "affected", "title", "url"] 

if response != False:
    print("Connected to url")
    if checkFields(response,feed):
        print("Fetched all fields")
    else:
        print("Error while fetching some fields")

    # #Test getting the needed field for the very first entity in feed
    # print("Text:-------------------------------------------------")
    # print(feed.entity[0].alert.description_text.translation[0].text)
    # print("Title:------------------------------------------------")
    # print(feed.entity[0].alert.header_text.translation[0].text)
    # print("informed_entities(Iterating over):--------------------")
    # for informed_entity in feed.entity[10].alert.informed_entity:
    #     print(informed_entity)
    #
    print(len(feed.entity),"entities found")
    constructAlertsList(feed, alerts, alert_keys, alerts_keys)

else:
        print("There is an error while fetching.")




