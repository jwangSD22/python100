
# we have imported the requests module
import requests
import json
# defined a URL variable that we will be
# using to send GET or POST requests to the API
url = "https://api.start.gg/gql/alpha"

headers = {'Authorization': 'Bearer c99c96c1c7c130770b4b2c87d1402925'}

request_data = {
    "query": """
query TournamentsByOwner($perPage: Int!, $ownerId: ID!) {
    tournaments(query: {
      perPage: $perPage
      filter: {
        ownerId: $ownerId
      }
    }) {
    nodes {
      id
      name
      slug
    }
  }
}
    """,
    "variables": {
        "ownerId": 78045,
        "perPage": 4
    }
}
response = requests.post(url=url, json=request_data,headers=headers)
print("response status code: ", response.status_code)
if response.status_code == 200:
    content = response.content.decode('utf-8')
    response_data = json.loads(content)
    pretty = json.dumps(response_data,indent=2)
    print(pretty)


