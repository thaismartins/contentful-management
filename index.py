import logging
from landing.brand.create import create_landing_brand

logging.basicConfig(level=logging.DEBUG)

def create_landings():
  new_brand = create_landing_brand()


create_landings()
