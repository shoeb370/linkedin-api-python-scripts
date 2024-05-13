
import json
from linkedin_api.clients.restli.client import RestliClient

bearer_token = 'Your Bearer Token'
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
