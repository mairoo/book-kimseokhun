from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField('Title', max_length=50)
    slug = models.SlugField('Slug', unique=True, allow_unicode=True, help_text='title alias for SEO')
    description = models.CharField('Description', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('Content')
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'blog_posts'
        ordering = ('-updated',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug))

    def get_previous_post(self):
        return self.get_previous_by_updated()

    def get_next_post(self):
        return self.get_next_by_updated()
