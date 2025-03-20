import pytest

from markdown_field.fields import MarkdownText

from .models import Post

pytestmark = pytest.mark.django_db


class TestMarkdownText:
    def test_html_property(self):
        value = "## Heading\n\nThis is a paragraph."
        md_text = MarkdownText(value)
        assert md_text.html == "<h2>Heading</h2>\n<p>This is a paragraph.</p>"

    def test_toc_property(self):
        value = "## Heading\n\nThis is a paragraph."
        md_text = MarkdownText(value)
        assert md_text.toc is None

    def test_str(self):
        value = "## Heading\n\nThis is a paragraph."
        md_text = MarkdownText(value)
        assert str(md_text) == value

    def test_with_extensions(self):
        value = "## Heading\n\nThis is a paragraph."
        md_text = MarkdownText(value, extensions=["toc"])
        assert md_text.toc == '<li><a href="#heading">Heading</a></li>'


class TestMarkdownField:
    def test_get(self):
        p = Post.objects.create(body="## Heading\n\nThis is a paragraph.")
        assert p.body.text == "## Heading\n\nThis is a paragraph."
        assert p.body.html == "<h2>Heading</h2>\n<p>This is a paragraph.</p>"
        assert p.body.toc is None

    def test_get_with_extensions(self, settings):
        settings.MARKDOWN_FIELD = {
            "extensions": ["toc"],
        }

        p = Post.objects.create(body="## Heading\n\nThis is a paragraph.")
        assert (
            p.body.html == '<h2 id="heading">Heading</h2>\n<p>This is a paragraph.</p>'
        )
        assert p.body.toc == '<li><a href="#heading">Heading</a></li>'

    def test_set(self):
        p = Post.objects.create(body="")
        p.body = "**Bold**"
        p.save()
        p.refresh_from_db()
        assert p.body.html == "<p><strong>Bold</strong></p>"

    def test_set_with_extensions(self, settings):
        settings.MARKDOWN_FIELD = {
            "extensions": ["toc"],
        }

        p = Post.objects.create(body="")
        p.body = "## Heading\n\nThis is a paragraph."
        p.save()
        p.refresh_from_db()
        assert (
            p.body.html == '<h2 id="heading">Heading</h2>\n<p>This is a paragraph.</p>'
        )
        assert p.body.toc == '<li><a href="#heading">Heading</a></li>'
