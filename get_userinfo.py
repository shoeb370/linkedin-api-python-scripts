from linkedin_api.clients.restli.client import RestliClient
bearer_token = 'AQWKzwHiKI9WN2LgeNc0QK3UcH0RScgBiDV446HrOkTgRP1VfVlcpA5EP2KVabIRcAjvBG1OEeO62EZyKn6OyFUBsRCR2RDgTY8XVGf1yFmYMaSUV6XtymKD9XTGIOpYTdT7B5URg0eOiiHHk6UltLRu34TvAlcHex5BOM84XIGN6a1K45O8GS9qwBbqltgMNqmGWcSCjjjVwCNbP3yFrfeXadmiemD9RsnkVnf-TZXjp0oHWgm51gLF9Um4snSIrtvibC6vj2CRAG9BBIiysFY4pwTWR4bD9FVJX2TnhgezhZIwsMt6NGopKV7PupEdPrUzuuI0S2MLco4w9H7t6tcYVoWGeA'
restli_client = RestliClient()

response = restli_client.get(
   resource_path="/userinfo",
  access_token= bearer_token
)
print(response.entity)


#9e5EJ0tYgp