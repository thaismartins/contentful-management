from html.parser import HTMLParser

class Mark():
  def __init__(self, type):
      self.type = type

class HTMLParserToRichText(HTMLParser):
  _document = None
  _current_node = None
  _current_tag = None

  def __init__(self, *, convert_charrefs: bool = ...) -> None:
    super().__init__(convert_charrefs=convert_charrefs)
    self._document = {
      "nodeType": "document",
      "data": {},
      "content": []
    }
    self._current_node = None
    self._current_tag = None

  def new_paragraph(data):
    return {
      "nodeType": "paragraph",
      "data": {},
      "content": []
    }

  def add_text(data, textValue, mark=''):
    text = {
      "nodeType": "text",
      "value": textValue,
      "marks": [],
      "data": {}
    }

    if (mark != ''):
      text['marks'].append(Mark(mark).__dict__)
      
    return text

  def handle_starttag(self, tag, attrs):
    self._current_tag = tag
    if (tag == 'p'):
      self._current_node = self.new_paragraph()

  def handle_endtag(self, tag):
    self._current_tag = ''
    if (tag == 'p'):
      self._document['content'].append(self._current_node)
      self._current_node = {}
    

  def handle_data(self, data):
    if (self._current_tag == 'p'):
      self._current_node['content'].append(self.add_text(data))
    elif (self._current_tag == 'b'):
      self._current_node['content'].append(self.add_text(data, 'bold'))
    elif (self._current_tag == 'i'):
      self._current_node['content'].append(self.add_text(data, 'italic'))
    else:
      self._current_node['content'].append(self.add_text(data))

  def get_document(self):
    return self._document

