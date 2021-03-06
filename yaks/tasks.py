__author__ = 'Jack'
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from yaks.models import Yak, YakLocation, Comment
from YikYakTerminal.API import Location, Yakker
import datetime, pytz

@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
def getYaks():
    for location in YakLocation.objects.all():
        yakker = Yakker(location=Location(location.latitude, location.longitude))
        for yak in yakker.get_yaks():
            if Yak.objects.filter(message_id=yak.message_id).count() == 0:
                tztime = datetime.datetime.strptime(yak.time, "%Y-%m-%d %H:%M:%S")
                tztime = pytz.timezone(location.timezone).localize(tztime)
                tztime = tztime.astimezone(pytz.timezone(location.timezone))
                y = Yak(poster_id=yak.poster_id, hide_pin=yak.hide_pin, message_id=yak.message_id,
                        delivery_id=yak.delivery_id, comments=int(yak.comments),
                        time=tztime, longitude=yak.longitude,
                        latitude=yak.latitude, likes=yak.likes, message=yak.message,
                        reyaked=yak.reyaked, handle=yak.handle, type=yak.type, yaklocation=location)
                y.save()
            else:
                y = Yak.objects.get(message_id=yak.message_id)
                y.comments = int(yak.comments)
                y.likes = yak.likes
                y.save()
            for comment in yakker.get_comments(yak.message_id):
                if Comment.objects.filter(comment_id=comment.comment_id).count() == 0:
                    tztime = datetime.datetime.strptime(comment.time, "%Y-%m-%d %H:%M:%S")
                    tztime = pytz.timezone(location.timezone).localize(tztime)
                    tztime = tztime.astimezone(pytz.timezone(location.timezone))
                    c = Comment(message_id=comment.message_id, comment_id=comment.comment_id, comment=comment.comment,
                                time=tztime, likes=comment.likes,
                                poster_id=comment.poster_id)
                    c.save()
                else:
                    c = Comment.objects.get(comment_id=comment.comment_id)
                    c.likes = comment.likes
                    c.save()
