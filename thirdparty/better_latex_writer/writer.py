# -*- coding: utf-8 -*-

import re

from docutils import nodes

from docutils.writers.latex2e import Writer as LatexWriter, LaTeXTranslator, \
  Babel


class TweakedLatexWriter(LatexWriter):

  def __init__(self):
    super(TweakedLatexWriter, self).__init__()
    self.translator_class = TweakedTranslator



class TweakedTranslator(LaTeXTranslator):

  def to_latex_encoding(self,docutils_encoding):
    return "utf8x"


  def __init__(self, document, babel_class=Babel):
    super(TweakedTranslator, self).__init__(document, babel_class)
    self.latex_preamble.append(r"\setlength{\parindent}{0em}")
    # self.latex_preamble.append("\setlength{\parskip}{1em}")
    self.latex_preamble.append(r"\usepackage{parskip}")

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
      if not re.match("https?://.*", href):
        return self.__visit_reference_attach(node, href)

    return super(TweakedTranslator, self).visit_reference(node)

  def visit_literal_block(self, node):
    if 'code' in node.attributes['classes']:
      # code-block
      # self.requirements['listings'] = "\\usepackage{listings}"
      # self.out.append('\n\\begin{lstlisting}\n%s\n\\end{lstlisting}\n' % node.astext())
      self.requirements['upquote'] = '\\usepackage{upquote}'
      self.out.append('\n\\begin{verbatim}\n%s\n\\end{verbatim}\n' % node.astext())
      raise nodes.SkipNode
    super(TweakedTranslator, self).visit_literal_block(node)


