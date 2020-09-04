from django.shortcuts import render
from notification.models import Notification
import copy

# Create your views here.

def see_notification(request):
    logged_in_user = request.user
    logged_in_notif = Notification.objects.filter(user_notified=logged_in_user)
    notif_copy = copy.copy(logged_in_notif)
    for notif in logged_in_notif:
        notif.delete()
    return render(request, "notifications.html", {"notif": notif_copy})
    