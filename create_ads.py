
from linkedin_api.clients.restli.client import RestliClient

bearer_token = 'Your Bearer Token'
ACCESS_TOKEN = bearer_token


# ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
if ACCESS_TOKEN is None:
    raise Exception(
        'A valid access token must be defined in the /examples/.env file under the variable name "ACCESS_TOKEN"'
    )

AD_ACCOUNTS_RESOURCE = "/adAccounts"
AD_ACCOUNTS_ENTITY_RESOURCE = "/adAccounts/{id}"
API_VERSION = "202309"

restli_client = RestliClient()
restli_client.session.hooks["response"].append(lambda r: r.raise_for_status())


"""
Create a test ad account
"""
create_response = restli_client.create(
    resource_path=AD_ACCOUNTS_RESOURCE,
    entity={
        "name": "Test Ad Account",
        "reference": "urn:li:organization:123",
        "status": "DRAFT",
        "type": "BUSINESS",
        "test": True,
    },
    access_token=ACCESS_TOKEN,
    version_string=API_VERSION,
)
ad_account_id = create_response.entity_id
print(f"Successfully created ad account: {ad_account_id}\n")
