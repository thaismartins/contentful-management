from pathlib import Path
import requests
import mimetypes

def get_content_type(url):
  response = requests.get(url)
  return response.headers['content-type']

def get_extension(content_type):
  return mimetypes.guess_extension(content_type)

def get_file_details(url):
  content_type = get_content_type(url)
  extension = get_extension(content_type)
  filename = Path(url).stem

  return {
    'name': f'{filename}{extension}',
    'extension': extension,
    'content_type': content_type,
  }