# -*- coding: utf-8 -*-

import re

from docutils import nodes

from docutils.writers.latex2e import Writer as LatexWriter, LaTeXTranslator

class TweakedLatexWriter(LatexWriter):

  def __init__(self):
    super().__init__()
    self.translator_class = TweakedTranslator


class TweakedTranslator(LaTeXTranslator):

  def __visit_reference_attach(self, node, href):
    self.requirements['attachfile'] = '\\usepackage{attachfile}\n\\attachfilesetup{appearance=false}'
    if node['refuri'] == node.astext():
      self.out.append(r'\url{%s}\attachfile{%s}{download}' % (href, href))
      raise nodes.SkipNode
    else:
      self.out.append(r'\attachfile{%s}{' % (href, ))
      node['__tweaked_href'] = href
      node['__tweaked_use_attachfile'] = True

  def visit_reference(self, node):

    special_chars = {ord('#'): r'\#', ord('%'): r'\%', ord('\\'): r'\\'}

    # external reference (URL)
    if 'refuri' in node:
      href = str(node['refuri']).translate(special_chars)
      if not re.match("https?://.*]", href):
        return self.__visit_reference_attach(node, href)

    return super().visit_reference(node)
