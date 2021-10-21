import os
import contentful_management

def create_asset(attributes):
  token = os.getenv('CONTENTFUL_MANAGEMENT_TOKEN')
  space = os.getenv('CONTENTFUL_SPACE')
  environment = os.getenv('CONTENTFUL_ENVIRONMENT')

  client = contentful_management.Client(token)

  return client.assets(space, environment).create(
    None,
    attributes
  )