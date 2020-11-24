from django.db import models
from users.models import User

# Create your models here.
class FriendRequest(models.Model):
    ''' A class for friend request between accounts '''

    Sent = 0
    Accepted = 1
    Cancelled = 2
    Deleted = 3
      
    STATUS_CODE = (
        (Sent, 'Sent'),
        (Accepted, 'Accepted'),
        (Cancelled, 'Cancelled'),
        (Deleted, 'Deleted')
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name='senders')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name='receivers')
    status = models.PositiveSmallIntegerField(choices=STATUS_CODE, blank=True, null=True)

