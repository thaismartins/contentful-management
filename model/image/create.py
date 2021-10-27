from logs.logging import logging
from image.create import create_image
from image.get import get_image

def create_or_update_image(entry):
  logging('Creating Model | Image...')

  if entry is None or 'image' not in entry:
    logging('Model | Image wasn`t created. No data was passed...')
    return None

  image = get_image(entry['image'])
  if (image):
    logging('Returning Model | Image...')
    return image

  logging('Creating Model | Image..')

  title = entry['title']
  description = f"{entry['title']} Description"

  new_image = create_image(title, description, entry['image'])

  return { 'id': new_image.id }
