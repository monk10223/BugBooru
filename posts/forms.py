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
        fields = ['uploaded_by', 'image_url']
        labels = {'uploaded_by': 'Author'}

    tags = forms.CharField(
        widget=forms.Textarea(),
        help_text='Enter tags separated by commas. (For example: bug, four_legs, pink)'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'uploaded_by' in self.fields:
            self.fields['uploaded_by'].required = False

    def clean_uploaded_by(self):
        return self.cleaned_data['uploaded_by'].strip() or 'Anonymous'

    def clean_tags(self):
        tags = parse_tags(self.cleaned_data['tags'])
        if not tags:
            raise forms.ValidationError('Enter at least one tag!')
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


class PostEditForm(PostCreateForm):
    class Meta(PostCreateForm.Meta):
        fields = ['uploaded_by']
        exclude = ['tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].widget = forms.Textarea(attrs={'rows': 3})
        names = [tag.name for tag in self.instance.tags.all()]
        self.initial['tags'] = ', '.join(names)
        self.fields['uploaded_by'].disabled = True