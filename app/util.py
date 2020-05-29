from django import forms


class ChangeDateInput(forms.DateInput):
    input_type = 'date'






def adiciona_form_control(self):
    for field_name, field in self.fields.items():
        if field and isinstance(field, forms.DateField):
            # field.widget.attrs['data-provide'] = 'datepicker2'
            field.widget.attrs['class'] = 'form-control '
        elif field and isinstance(field, forms.DateTimeField):
            # field.widget.attrs['data-provide'] = 'datepicker2'
            field.widget.attrs['class'] = 'form-control '
        else:
            field.widget.attrs['class'] = 'form-control'
