# django-md-field

A Django model field that integrates [Python-Markdown](https://github.com/Python-Markdown/markdown) for handling Markdown content.

## Requirements

- Python: >=3.10, <4
- Django: >=4.2, <6.0

## Installation

```bash
pip install django-md-field
```

## Usage

### Basic Usage

```python
from django.db.models import Model
from markdown_field import MarkdownField

class Post(Model):
    body = MarkdownField("body")
```

### Accessing Content

```python
# Create a post with Markdown content
>>> post = Post.objects.create(body="## Heading\n\nThis is a paragraph.")

# Access the raw Markdown text
>>> post.body.text
'## Heading\n\nThis is a paragraph.'

# Access the rendered HTML
>>> post.body.html
'<h2>Heading</h2>\n<p>This is a paragraph.</p>'

# Access table of contents (if TOC extension is enabled)
>>> post.body.toc
'<li><a href="#heading">Heading</a></li>'
```

### Configuring Markdown Extensions

You can configure Markdown extensions in two ways:

- In your Django settings (`settings.py`):

```python
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify

MARKDOWN_FIELD = {
    "extensions": [
        TocExtension(slugify=slugify, toc_depth=3),
        "pymdownx.highlight",
        "pymdownx.arithmatex",
    ],
    "extension_configs": {
        "pymdownx.highlight": {
            "linenums_style": "pymdownx-inline",
        },
        "pymdownx.arithmatex": {
            "generic": True,
        },
    },
}
```

- Directly in the model field, this will override the `MARKDOWN_FIELD` setting in `settings.py`:

```python
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify

body = MarkdownField(
    "body",
    extensions=[
        TocExtension(slugify=slugify, toc_depth=3),
        "pymdownx.highlight",
        "pymdownx.arithmatex",
    ],
    extension_configs={
        "pymdownx.highlight": {
            "linenums_style": "pymdownx-inline",
        },
        "pymdownx.arithmatex": {
            "generic": True,
        },
    },
)
```

For more information about available extensions, see:

- [Python Markdown Extensions](https://python-markdown.github.io/extensions/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
