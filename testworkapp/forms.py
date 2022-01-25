from django.forms import *
from .models import NewsList, comment, backsaids

class NewsListForm(ModelForm):
    class Meta:
        model = NewsList
        fields = ["title","desc","img"]
        widgets={
            "title":TextInput(
                attrs={
                    'class' : '',
                    'placeholder': 'Название статьи'
                    }
                ),
            "desc":Textarea(
                attrs={
                    'class' : '',
                    'placeholder': 'Текст статьи'
                    }
                ),
            "img":ClearableFileInput()
        }

class addComm(ModelForm):
    class Meta:
        model = comment
        fields = ['Text']
        widgets = {
            "Text": Textarea(
                attrs={
                    'class': 'add_comm_from-text_textarea',
                    'placeholder': 'Текст комментария'
                }
            )
        }


class addSaid(ModelForm):
    class Meta:
        model = backsaids
        fields = ['Text', 'Email']
        widgets = {
            "Text": Textarea(
                attrs={
                    'class': 'add_said_form-item_textarea',
                    'placeholder': 'Ваш отзыв'
                }
            ),

        }