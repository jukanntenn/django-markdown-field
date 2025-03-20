from django.db.models import Model

from markdown_field.fields import MarkdownField


class Post(Model):
    body = MarkdownField("body")
