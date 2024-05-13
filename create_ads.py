
from linkedin_api.clients.restli.client import RestliClient

bearer_token = 'AQWKzwHiKI9WN2LgeNc0QK3UcH0RScgBiDV446HrOkTgRP1VfVlcpA5EP2KVabIRcAjvBG1OEeO62EZyKn6OyFUBsRCR2RDgTY8XVGf1yFmYMaSUV6XtymKD9XTGIOpYTdT7B5URg0eOiiHHk6UltLRu34TvAlcHex5BOM84XIGN6a1K45O8GS9qwBbqltgMNqmGWcSCjjjVwCNbP3yFrfeXadmiemD9RsnkVnf-TZXjp0oHWgm51gLF9Um4snSIrtvibC6vj2CRAG9BBIiysFY4pwTWR4bD9FVJX2TnhgezhZIwsMt6NGopKV7PupEdPrUzuuI0S2MLco4w9H7t6tcYVoWGeA'
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
