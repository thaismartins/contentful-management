from rich_text.HTMLParserToRichText import HTMLParserToRichText

def convert_html(html):
  parser = HTMLParserToRichText()
  parser.feed(html)
  document = parser.get_document()
  return document