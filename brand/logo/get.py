from image.create import create_image
from image.get import get_image

def get_logo(entry):
  if entry is None or 'logo' not in entry:
    print('Brand Hero Image wasn`t created. No data was passed...')
    return None

  image = get_image(entry['logo'])
  if (image):
    print('Returning Brand Hero Logo...')
    return image

  print('Creating Brand Hero Logo..')

  title = entry['title']
  description = f"{entry['title']} Description"

  return create_image(title, description, entry['image'])