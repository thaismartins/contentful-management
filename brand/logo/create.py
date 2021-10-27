from brand.logo.get import get_logo
from image.create import create_image
from logs.logging import logging

def create_or_update_logo(entry):
  logging('Starting Brand | Logo creation...')

  if entry is None or 'logo' not in entry:
    logging('Brand | Logo wasn`t created. No data was passed...')

  logo = get_logo(entry)
  if(logo):
    return update_logo(logo)

  return create_logo(entry)
  
def create_logo(entry):
  logging('Creating Brand | Logo...')
  
  title = entry['title']
  description = f"{entry['title']} Description"

  new_logo = create_image(title, description, entry['logo'])
  return { 'id': new_logo.id }


def update_logo(logo):
  logging('Updating Brand | Logo...')

  # TODO: update logo
  # if (file_name != ''):
  # logo.delete()
  # logo = create_logo()

  # file_name = logo['file']['pt-BR']['fileName']
  return logo