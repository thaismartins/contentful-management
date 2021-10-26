import os
import contentful_management

def create_asset(attributes):
  token = os.environ.get('CONTENTFUL_MANAGEMENT_TOKEN')
  space = os.environ.get('CONTENTFUL_SPACE')
  environment = os.environ.get('CONTENTFUL_ENVIRONMENT')
  
  client = contentful_management.Client(token)

  new_asset = client.assets(space, environment).create(
    None,
    attributes
  )

  new_asset.process()

  return new_asset