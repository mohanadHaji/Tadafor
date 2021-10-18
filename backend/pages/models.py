from django.db import models
from django.contrib.auth.models import User
import datetime
    
class Message(models.Model):
    from_id = models.ForeignKey(User, related_name='fromm',on_delete=models.CASCADE)
    to_id = models.ForeignKey(User, related_name='to', on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    time = models.DateTimeField(default=datetime.date.today)
    def __str__(self):
        return self.message+" "+str(self.from_id.id)+" " + str(self.to_id.id)