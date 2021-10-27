from entry.get import get_entry
from logs.logging import logging

def get_brand_by_title(title):
  logging('Searching Brand by title...')
  
  if title is None:
    return False 

  query = {
    'field': 'title',
    'value': title
  }
  
  brand = get_entry(content_type_id='brand', query=query)
  return brand