
import json
from linkedin_api.clients.restli.client import RestliClient

bearer_token = 'AQWKzwHiKI9WN2LgeNc0QK3UcH0RScgBiDV446HrOkTgRP1VfVlcpA5EP2KVabIRcAjvBG1OEeO62EZyKn6OyFUBsRCR2RDgTY8XVGf1yFmYMaSUV6XtymKD9XTGIOpYTdT7B5URg0eOiiHHk6UltLRu34TvAlcHex5BOM84XIGN6a1K45O8GS9qwBbqltgMNqmGWcSCjjjVwCNbP3yFrfeXadmiemD9RsnkVnf-TZXjp0oHWgm51gLF9Um4snSIrtvibC6vj2CRAG9BBIiysFY4pwTWR4bD9FVJX2TnhgezhZIwsMt6NGopKV7PupEdPrUzuuI0S2MLco4w9H7t6tcYVoWGeA'
ACCESS_TOKEN = bearer_token

API_VERSION = "202309"
restli_client = RestliClient()
restli_client.session.hooks["response"].append(lambda r: r.raise_for_status())

# Assuming your organization's ID is "urn:li:organization:2414183"
organization_id = "102896812"


# Fetch details about the organization
organization_response = restli_client.get(
    resource_path=f"/organizations/{organization_id}",
    access_token=ACCESS_TOKEN,
    version_string=API_VERSION
)

# Print organization details
print(json.dumps(organization_response.entity, indent=2))
