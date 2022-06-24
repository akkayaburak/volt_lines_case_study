from datetime import timedelta
from time import timezone
from django.db import models
from django.core.validators import RegexValidator,MaxValueValidator,MinValueValidator
from django.utils import timezone

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
default_start_time = timezone.now()
default_est_end_time = timezone.now() + timedelta(minutes=30)


class passenger(models.Model):
    class Meta:
        passenger_id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=100,null=False)
        surname = models.CharField(max_length=100,null=False)
        email = models.EmailField(null=False)
        status = models.BooleanField(default=1)
        phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'
        def __unicode__(self):
            return self.name

class passenger_trip(models.Model):
    passenger_trip_id = models.AutoField(primary_key=True)
    passenger_id = models.ForeignKey(passenger,on_delete=models.CASCADE)
    total_distance = models.IntegerField(null=False,validators=[MaxValueValidator(100),MinValueValidator(1)])
    start_time = models.DateTimeField(default=default_start_time)
    estimated_end_time = models.DateTimeField(default=default_est_end_time)

    def __str__(self):
        return 'passenger_trip_id' + self.passenger_trip_id

    class Meta:
        app_label = 'api'
        def __unicode__(self):
            return self.name

    






