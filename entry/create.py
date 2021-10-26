import os
import contentful_management

def create_entry(attributes):
  token = os.environ.get('CONTENTFUL_MANAGEMENT_TOKEN')
  space = os.environ.get('CONTENTFUL_SPACE')
  environment = os.environ.get('CONTENTFUL_ENVIRONMENT')

  client = contentful_management.Client(token)

  return client.entries(space, environment).create(
    None,
    attributes
  )