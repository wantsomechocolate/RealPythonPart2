## app/tasks/forms.py

from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, SelectField,
from wtforms.validators import DataRequired


class AddTask(Form):

    task_id = IntegerField('Priority')
    
    name = TextField('Task Name', validators=[DataRequired()])
    
    due_date = DateField('Date Due (mm/dd/yyyy)', validators=[DataRequired()],
                         format='%m/%d/%Y')

    choices=[]
    for i in range(10):
        choices.append((str(i+1),str(i+1)))
  
    priority = SelectField('Priority', validators=[DataRequired()], choices=choices,
                           id='priority_dropdown')

    status = IntegerField('Status')

    posted_date = DateField('Posted Date (mm/dd/yyyy)', validators=[DataRequired()],
                            format='%m/%d/%Y')



    



    
