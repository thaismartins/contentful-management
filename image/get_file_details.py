from pathlib import Path

def get_content_type(extension):
  if extension == '.jpg' or extension == '.jpeg':
    return 'image/jpg'
  
  if extension == '.png':
    return 'image/png'

def get_file_details(url):
  extension = Path(url).suffix
  content_type = get_content_type(extension)
  filename = Path(url).stem

  return {
    'name': f'{filename}{extension}',
    'extension': extension,
    'content_type': content_type,
  }