import os
import contentful_management

def get_entry(id=None, content_type_id=None, query=None):
  token = os.environ.get('CONTENTFUL_MANAGEMENT_TOKEN')
  space = os.environ.get('CONTENTFUL_SPACE')
  environment = os.environ.get('CONTENTFUL_ENVIRONMENT')

  client = contentful_management.Client(token)

  entries = client.entries(space, environment).find(id, { 'content_type': content_type_id })

  if entries is None:
    return None

  if query is None:
    return entries
  
  foundedEntry = {}
  for entry in entries:
    if (query['field'] in entry.raw['fields'] and entry.raw['fields'][query['field']]['pt-BR'] == query['value']):
      entry.raw['fields']['id'] = entry.raw['sys']['id']
      foundedEntry = entry.raw['fields']

  return foundedEntry