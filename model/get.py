from logs.logging import logging
from entry.get import get_entry

def get_model_by_title(title, brand):
  logging('Searching Model by title...')
  
  if title is None:
    return False 

  query = {
    'field': 'title',
    'value': title
  }

  linked = {
    'field': 'brand',
    'value': brand['id']
  }
  
  model = get_entry(content_type_id='model', query=query, linked=linked)
  return model