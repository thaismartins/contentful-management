from entry.get import get_entry

def get_hero(entry):
  if entry is None:
    return False

  hero = get_entry(entry['pt-BR']['sys']['id'], 'sectionBrandHero')
  return hero