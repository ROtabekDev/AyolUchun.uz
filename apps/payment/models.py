from django.db import models

from helpers.models import BaseModel

from apps.user.models import User
from apps.course.models import Course

class Payment(BaseModel):
    """To`lovlar"""

    PAYMENT_TYPE = (
        ('Payme', 'Payme'),
        ('Click', 'Click'),
        ('Apelsin', 'Apelsin'),
        ('KPay', 'KPay'),
        ('Visa', 'Visa'),
        ('MasterCard', 'MasterCard'),
    )

    PAYMENT_STATUS = (
        ('Succes', 'Muvaffaqiyatli'),
        ('Error', 'Xato'),
        ('In_progress', 'Jarayonda')
    )

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.DecimalField('Pul miqdori', max_digits=12, decimal_places=2)
    payment_type = models.CharField('To`lov turi', choices=PAYMENT_TYPE, max_length=15)
    payment_status = models.CharField('To`lov holati', choices=PAYMENT_STATUS, max_length=15)

    def __str__(self):
        return self.price