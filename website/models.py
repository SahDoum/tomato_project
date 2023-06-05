from django.db import models
from django.db.models import SET_NULL

from datetime import datetime
from django.utils import timezone
import random


from .auth.models import User, Supplier
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

SUPPLIES = [
	"Армен",
	"Василий Петрович",
	"Продуктовый концерн Солнышко",
	"Совхоз имени ушедшего Октября",
]


class Order(models.Model):
	CREATED = 0
	ACCEPTED = 1
	SHIPPING = 2
	DELIVERED = 3
	DECLINED = 4
	DISPUTE = 5

	STATUS_CHOICES = (
	    (CREATED, 'Заказ создан'),
	    (ACCEPTED, 'Заказ принят'),
	    (SHIPPING, 'В пути'),
	    (DELIVERED, "Доставлен"),
	    (DECLINED, "Отказан"),
	    (DISPUTE, "Открыт спор"),
	)

	GREEN = 0
	RIPE = 1
	CHERRY = 2
	UZBEK = 3
	AZER = 4

	TOMATO_TYPE = (
		(GREEN, 'Зеленый'),
		(RIPE, 'Спелый'),
		(CHERRY, 'Черри'),
		(UZBEK, 'Узбекский'),
		(AZER, 'Азербайджанский')
	)

	customer = models.ForeignKey(User, on_delete=models.CASCADE)
	supplier = models.ForeignKey(Supplier, on_delete=SET_NULL, null=True)
	timestamp = models.DateTimeField(default=datetime.now, editable=False)
	status = models.IntegerField(choices=STATUS_CHOICES)
	tomato_type = models.IntegerField(choices=TOMATO_TYPE, default=GREEN)

	# def save(self, *args, **kwargs):
	#     if not self.pk:
	#     	self.supplier = random.choice(SUPPLIES)
	#         # This code only happens if the objects is
	#         # not in the database yet. Otherwise it would
	#         # have pk
	#     super(Order, self).save(*args, **kwargs)

	def update_supplier(self):
		self.supplier = random.choice(SUPPLIES)

	def get_status_display(self):
		return Order.STATUS_CHOICES[self.status][1]

	def get_type_display(self):
		return Order.TOMATO_TYPE[self.tomato_type][1]
