import contentful_management

def create_entry(attributes):
  client = contentful_management.Client('')

  space = '46aggqlli43a'
  environment = 'master'

  return client.entries(space, environment).create(
    None,
    attributes
  )