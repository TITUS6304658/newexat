from django import forms
from .models import result
from .models import title
from .models import owner
from .models import title, contract, project


class AnswerForm(forms.ModelForm):
    

    class Meta:
        model = result
        fields = ('owner_id', 'result', 'problem', 'solution')

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = title
        fields = ('title_name','contract_id')

    
class OwnerForm(forms.ModelForm):
    class Meta:
        model = owner
        fields = ('owner_id', 'title_id')
class projectForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ('project_id', 'project_name','project_year_start','project_year_end')
class contracForm(forms.ModelForm):
    class Meta:
        model = contract
        fields = ('project_id', 'contract_no')
    
class DATEQuestionForm(forms.ModelForm):
    year = forms.DateField(widget=forms.SelectDateWidget)
    quarter_no = forms.ChoiceField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], widget=forms.Select)
    class Meta:
        model = result
        fields = ('year','quarter_no')
