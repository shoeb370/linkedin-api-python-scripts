from linkedin_api.clients.restli.client import RestliClient
bearer_token = 'Your Bearer Token'
restli_client = RestliClient()

response = restli_client.get(
   resource_path="/userinfo",
  access_token= bearer_token
)
print(response.entity)


#9e5EJ0tYgp
