import requests

#you can have to extract data from NewRelic using the below Query
'''
{
  actor {
    entitySearch(query: "domain = 'SYNTH' AND type = 'MONITOR'") {
      results {
        entities {
          ... on SyntheticMonitorEntityOutline {
            guid
            name
            accountId
            monitorType
            tags {
              key
              values
            }
          }
          account {
            id
            name
          }
        }
      }
    }
  }
}

'''

#below is the result of the query to use as input for API to add users to group

d = {
                      "displayName": "GROUP",
                      "users": {
                        "users": [
                          {
                            "id": "1002804694"
                          },
                          {
                            "id": "1002804696"
                          },
                          {
                            "id": "1002804697"
                          },
                          {
                            "id": "1002804699"
                          },
                          {
                            "id": "1002804703"
                          },
                          {
                            "id": "1002804705"
                          },
                          {
                            "id": "1002804706"
                          },
                          {
                            "id": "1002804709"
                          },
                          {
                            "id": "1002804710"
                          },
                          {
                            "id": "1002804711"
                          },
                          {
                            "id": "1002804713"
                          },
                          {
                            "id": "1002804714"
                          },
                          {
                            "id": "1002804716"
                          },
                          {
                            "id": "1002804717"
                          },
                          {
                            "id": "1002804718"
                          },
                          {
                            "id": "1002804720"
                          },
                          {
                            "id": "1002804722"
                          },
                          {
                            "id": "1002804725"
                          },
                          {
                            "id": "1002804726"
                          },
                          {
                            "id": "1002804728"
                          },
                          {
                            "id": "1002804731"
                          },
                          {
                            "id": "1002804732"
                          },
                          {
                            "id": "1002804739"
                          },
                          {
                            "id": "1002804740"
                          },
                          {
                            "id": "1002804741"
                          },
                          {
                            "id": "1002804745"
                          },
                          {
                            "id": "1002804746"
                          },
                          {
                            "id": "1002804748"
                          },
                          {
                            "id": "1002804754"
                          },
                          {
                            "id": "1002804756"
                          },
                          {
                            "id": "1004015709"
                          },
                          {
                            "id": "1004298649"
                          },
                          {
                            "id": "1004300253"
                          },
                          {
                            "id": "1004453555"
                          },
                          {
                            "id": "1004542140"
                          },
                          {
                            "id": "1004744779"
                          },
                          {
                            "id": "1004805042"
                          },
                          {
                            "id": "1004866738"
                          },
                          {
                            "id": "1004873997"
                          },
                          {
                            "id": "1004875400"
                          },
                          {
                            "id": "1004910515"
                          },
                          {
                            "id": "1004914103"
                          },
                          {
                            "id": "1004914553"
                          },
                          {
                            "id": "1004916117"
                          },
                          {
                            "id": "1004916118"
                          },
                          {
                            "id": "1004916138"
                          },
                          {
                            "id": "1004957073"
                          },
                          {
                            "id": "1004968855"
                          },
                          {
                            "id": "1004968858"
                          },
                          {
                            "id": "1004968862"
                          },
                          {
                            "id": "1004968869"
                          },
                          {
                            "id": "1004968874"
                          },
                          {
                            "id": "1004968883"
                          },
                          {
                            "id": "1004968980"
                          },
                          {
                            "id": "1005000043"
                          },
                          {
                            "id": "1005130443"
                          },
                          {
                            "id": "1005247159"
                          },
                          {
                            "id": "1005255708"
                          },
                          {
                            "id": "1005297160"
                          },
                          {
                            "id": "1005346461"
                          },
                          {
                            "id": "1005349324"
                          },
                          {
                            "id": "1005430451"
                          }
                        ]
                      }
                    }

list_of_users = d["users"]["users"]
ls = []

for i in list_of_users:
    ls.append(i['id'])

new = ls[3:53]
new_1= ls[53:]



# API Endpoint
URL = "https://api.newrelic.com/graphql"

# Replace with your personal New Relic API Key and Account ID
API_KEY = "YOUR_API_KEY"
ACCOUNT_ID = "YOUR_ACCOUNT_ID"

HEADERS = {
    "Content-Type": "application/json",
    "API-Key": API_KEY
}

def create_user_group(user_id):
    # Define the GraphQL mutation
    
    mutation = """
    mutation($name: [ID!]!){
  userManagementAddUsersToGroups(
    addUsersToGroupsOptions: {groupIds: "GUID", userIds: $name}
  ) {
    groups {
      displayName
      id
    }
  }
}
    """
    variables = {'name':user_id}

    response = requests.post(URL, json={'query': mutation, 'variables':variables}, headers=HEADERS)
    print(response.content)

create_user_group(new)
create_user_group(new_1)


'''below code is working just replace the mutation in the above one and give correct display name it will create group and second one is to
    create account access on the group so you can make changes to this mutation and function
'''

'''
working to create group
mutation($name: String!) {
  userManagementCreateGroup(
    createGroupOptions: {authenticationDomainId: "GUID", displayName:$name}
  ) {
    group {
      displayName
      id
    }
  }
}'''

'''
working role addition to group
mutation {
  authorizationManagementGrantAccess(
    grantAccessOptions: {
      groupId: "GUID"
      accountAccessGrants: {
        accountId: ID
        roleId: "ID"
      }
    }
  ) {
    roles {
      displayName
      accountId
    }
  }
}
'''