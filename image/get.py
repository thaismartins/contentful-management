from asset.get import get_asset
from image.get_file_details import get_file_details

def get_image(url):
  file_details = get_file_details(url)
  return get_asset(query={ 'name': file_details['name'] })