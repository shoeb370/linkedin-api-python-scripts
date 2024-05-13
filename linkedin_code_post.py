
from linkedin_api.clients.restli.client import RestliClient
import json
bearer_token = 'AQWKzwHiKI9WN2LgeNc0QK3UcH0RScgBiDV446HrOkTgRP1VfVlcpA5EP2KVabIRcAjvBG1OEeO62EZyKn6OyFUBsRCR2RDgTY8XVGf1yFmYMaSUV6XtymKD9XTGIOpYTdT7B5URg0eOiiHHk6UltLRu34TvAlcHex5BOM84XIGN6a1K45O8GS9qwBbqltgMNqmGWcSCjjjVwCNbP3yFrfeXadmiemD9RsnkVnf-TZXjp0oHWgm51gLF9Um4snSIrtvibC6vj2CRAG9BBIiysFY4pwTWR4bD9FVJX2TnhgezhZIwsMt6NGopKV7PupEdPrUzuuI0S2MLco4w9H7t6tcYVoWGeA'
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