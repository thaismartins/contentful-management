import os
import contentful_management

def get_asset(id=None, query=None):
  token = os.environ.get('CONTENTFUL_MANAGEMENT_TOKEN')
  space = os.environ.get('CONTENTFUL_SPACE')
  environment = os.environ.get('CONTENTFUL_ENVIRONMENT')
  
  client = contentful_management.Client(token)

  assets = client.assets(space, environment).find(id)

  if assets is None:
    return None

  if query is None:
    return assets

  if 'name' in query:
    foundedAsset = None

    for asset in assets:
      if (asset.raw['fields']['file']['pt-BR']['fileName'] == query['name']):
        foundedAsset = dict(asset.raw['fields'])
        foundedAsset['id'] = asset.raw['sys']['id']

  return foundedAsset