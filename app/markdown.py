import houdini
import misaka
from misaka import HtmlRenderer, SmartyPants
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

class MyBlogHtmlRenderer(HtmlRenderer, SmartyPants):

	def _code_no_lexer(self, text):
		# encode to utf8 string
		text = text.encode('utf8').strip()
		return(
		    """
		    <div class="highlight">
		      <pre><code>%s</code></pre>
		    </div>
		    """ % houdini.escape_html(text)
		)

	def block_code(self, text, lang):		
		if not lang:
		    return self._code_no_lexer(text)

		try:
		    lexer = get_lexer_by_name(lang, stripall=True)
		except ClassNotFound:  # lexer not found, use plain text
		    return self._code_no_lexer(text)

		formatter = HtmlFormatter()

		return highlight(text, lexer, formatter)

render = MyBlogHtmlRenderer(flags=misaka.HTML_ESCAPE)

extensions = (
    misaka.EXT_FENCED_CODE |
    misaka.EXT_NO_INTRA_EMPHASIS |
    misaka.EXT_AUTOLINK
)

markdown = misaka.Markdown(render, extensions=extensions)
				