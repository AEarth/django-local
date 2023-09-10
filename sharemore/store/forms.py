from django import forms

from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        
        fields = ('category', 'title', 'description', 'value', 'image',)
        label = {'category': "", 'title': "", 'description': "", 'value': "", 'image': "Image"}
        widgets = {
            'category': forms.Select(attrs=
                {
                'class': 'm-2 shadow menu dropdown-content z-[1] bg-base-100 rounded-box w-32 hidden-label'
                }),
            'title': forms.TextInput(attrs=
                {
                'class': 'm-2 input input-bordered input-sm w-1/2 max-w-xs'
                }),
            'description': forms.Textarea(attrs=
                {
                'class': 'textarea textarea-bordered textarea-md w-full max-w-xs',
                'rows': 2,
                'placeholder': 'item description',
                }),
            'value': forms.TextInput(attrs=
                {
                'class': 'm-2 input input-bordered input-sm w-1/4 max-w-xs'
                }),
            'image': forms.FileInput(attrs=
                {
                'class': 'file-input file-input-bordered file-input-sm w-full max-w-xs'
                }),
        }


