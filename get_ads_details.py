

from linkedin_api.clients.restli.client import RestliClient
bearer_token = 'Your Bearer Token'
restli_client = RestliClient()

response = restli_client.get(
   resource_path="/adAccountsV2/513424108",
  # resource_path= f'/v2/posts',
  access_token= bearer_token
)
print(response.entity)
