from schedule_machine.chrono import Timers
from news.models import Post, Subscribe
from django.core.mail import send_mail


def send_email_news():
    subs = Subscribe.objects.all()
    for sub in subs:
        latest = Post.objects.all().order_by("-date_created")[:10]
        send_mail(
            subject="Latest news",
            message=f"{latest}",
            from_email="admin@admin.com",
            recipient_list=[f"{sub.email}"],
            fail_silently=True,
        )


def enable_send_email():
    timer_send = Timers()
    timer_send.create_timer("schedule", send_email_news(), "01:00")


def reset_count():
    counts = Post.objects.all()
    for count in counts:
        count.upvotes.all().delete()


def enable_func():
    timer = Timers()
    timer.create_timer("schedule", reset_count, "01:00")
