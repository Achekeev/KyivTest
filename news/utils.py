from schedule_machine.chrono import Timers
from news.models import Post


def reset_count():
    counts = Post.objects.all()
    for count in counts:
        count.upvotes.all().delete()


def enable_func():
    timer = Timers()
    timer.create_timer("schedule", reset_count, "01:00")