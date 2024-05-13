
from linkedin_api.clients.restli.client import RestliClient
import json
bearer_token = 'Your Bearer Token'
ACCESS_TOKEN = bearer_token

    
ME_RESOURCE = "/me"
UGC_POSTS_RESOURCE = "/ugcPosts"
POSTS_RESOURCE = "/posts"
API_VERSION = "202309"
restli_client = RestliClient()
restli_client.session.hooks["response"].append(lambda r: r.raise_for_status())

me_response = restli_client.get(resource_path=ME_RESOURCE, access_token=ACCESS_TOKEN)

posts_create_response = restli_client.create(
    resource_path=POSTS_RESOURCE,
    entity={
        "author": f"urn:li:person:{me_response.entity['id']}",
        "lifecycleState": "PUBLISHED",
        "visibility": "PUBLIC",
        "commentary": """Sample text post created with /posts API using python \n #PythonLinkedAPI
        #Python Learning #LinkedinPOSTAPI""",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
    },
    version_string=API_VERSION,
    access_token=ACCESS_TOKEN,
)
print(f"Successfully created post using /posts: {posts_create_response.entity_id}")
