import re
from rest_framework.serializers import ValidationError


class TitleValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('^[a-zA-Z0-9а-яА-Я\.\-\ ]+$')
        tmp_val = dict(value).get(self.field)
        if tmp_val is None or not bool(reg.match(tmp_val)):
            raise ValidationError('Неверное название')
