import contentful_management

def create_asset(attributes):
  client = contentful_management.Client('CFPAT-63UXLAFIfBrTo5oHcrTHNdYe8YIV7ErSeGP4gxemnOU')

  space = '46aggqlli43a'
  environment = 'master'

  return client.assets(space, environment).create(
    None,
    attributes
  )