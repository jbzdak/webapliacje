# -*- coding: utf-8 -*-
from docutils.core import Publisher
from docutils.nodes import title
from pelican.readers import PelicanHTMLTranslator, RstReader, docutils


class EnhancedTranslator(PelicanHTMLTranslator):

  __admonition_map = {
    'note': ('bs-callout-primary', 'Na marginesie:'),
    'default': ('bs-callout-default', None),
    'caution': ('bs-callout-warning', 'Uwaga:'),
    'danger': ('bs-callout-dangera', 'Uwaga:'),
  }

  def __get_admonitoon_metadata_from_classes(self, node):
    for c in node.attributes['classes']:
      if c in self.__admonition_map:
        return self.__admonition_map[c]
    return self.__admonition_map['default']

  def visit_admonition(self, node):

    css, header = self.__get_admonitoon_metadata_from_classes(node)

    # We remove title given by docutils becouse we add our own
    # if first node is not a title something is screwed
    assert isinstance(node.children[0], title)

    node.children.pop(0)

    self.body.append(self.starttag(node, 'div', **{'class': 'bs-callout ' + css}))

    if header is not None:
      self.body.append("<h4>{}</h4>".format(header))

    self.set_first_last(node)


class EnchancedRstReader(RstReader):
  def _get_publisher(self, source_path):

    # This needs to be copy-pasted from pelican sources.
    extra_params = {'initial_header_level': '2',
                    'syntax_highlight': 'short',
                    'input_encoding': 'utf-8',
                    'exit_status_level': 2,
                    'embed_stylesheet': False}
    user_params = self.settings.get('DOCUTILS_SETTINGS')
    if user_params:
        extra_params.update(user_params)

    pub = Publisher(
        source_class=self.FileInput,
        destination_class=docutils.io.StringOutput)
    pub.set_components('standalone', 'restructuredtext', 'html')
    pub.writer.translator_class = EnhancedTranslator
    pub.process_programmatic_settings(None, extra_params, None)
    pub.set_source(source_path=source_path)
    pub.publish(enable_exit_status=True)
    return pub