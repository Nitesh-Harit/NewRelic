import requests
import guid_for_apm
# API Endpoint
URL = "https://api.newrelic.com/graphql"

# Replace with your personal New Relic API Key and Account ID

'''
#this nrql to get service apm guids
{
  actor {
    entitySearch(
      queryBuilder: {domain: APM, type: APPLICATION, tags: {key: "AccountID", value: "3675479"}}
      options: {}
    ) {
      query
      results {
        entities {
          name
          entityType
          guid
          accountId
          type
        }
      }
    }
  }
}

after running this query you will get guids of all the APM.
make a new file with the name guid_for_apm, create a function with the anem give_guids and then create a dictionary with name d and do the below.


result =  (d["data"]["actor"]["entitySearch"]["results"]["entities"])
 lis_of_guid = []
  for i in result:
      lis_of_guid.append(i["guid"])
      #print(i["guid"])
  #print (len(lis_of_guid))
  return(lis_of_guid)
give_guid()


'''
API_KEY = "YOUR NEW RELIC API KEY"
ACCOUNT_ID = "ACCOUNT ID"

HEADERS = {
    "Content-Type": "application/json",
    "API-Key": API_KEY
}

def delete_entity(forceDelete,guids):
    # Define the GraphQL mutation
    
    mutation = """
    mutation entityDelete ($forceDelete: Boolean!, $guids: [EntityGuid!]!) {
    entityDelete (forceDelete: $forceDelete, guids: $guids) {
        deletedEntities
        failures {
            guid
            message
            type
        }
    }
}
    """
    variables = {"forceDelete": forceDelete,"guids": guids}

    response = requests.post(URL, json={'query': mutation, 'variables':variables}, headers=HEADERS)
    print(response.content)

#list_of_guid = guid_for_apm.give_guid()
#list_first = list_of_guid[0:100]
#list_second = list_of_guid[100:]
#delete_entity(True,list_first)
#delete_entity(True,list_second)

def delete_Browser_application(guids):
    mutation = """
    mutation agentApplicationDelete ($guids: EntityGuid!) {
    agentApplicationDelete (guid: $guids) {
        
        success
    }
}
    """
    variables = {"guids": guids}

    response = requests.post(URL, json={'query': mutation, 'variables':variables}, headers=HEADERS)
    print(response.content)

list_of_guid = guid_for_apm.give_guid()
#taking only guid as this mutation will take only one guid at a time. 
#print(list_of_guid)
for i in range(len(list_of_guid)):

    delete_Browser_application(list_of_guid[i])