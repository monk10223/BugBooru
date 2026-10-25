from django import forms
from posts.models import Post
from posts.validators import validate_tags
from tags.models import Tag


def parse_tags(raw):
    tags = []
    for t in raw.split(','):
        tag = t.lower().strip()
        if tag and tag not in tags:
            tags.append(tag)
    return tags


class SearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label='Search',
        help_text='Enter tags separated by commas.',
    )

    def get_tags(self):
        query = self.cleaned_data.get('query', '')
        return parse_tags(query)


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image_url']

    tags = forms.CharField(help_text='Enter tags separated by commas. (For example: bug, four_legs, pink)')

    def clean_tags(self):
        tags = parse_tags(self.cleaned_data['tags'])
        if not tags:
            raise forms.ValidationError('Please enter at least one tag!')
        validate_tags(tags)
        return tags

    def save(self, commit=True):
        post = super().save(commit=commit)

        if commit:
            tags = []
            for name in self.cleaned_data['tags']:
                tag = Tag.objects.get_or_create(name=name)[0]
                tags.append(tag)
            post.tags.set(tags)

        return post