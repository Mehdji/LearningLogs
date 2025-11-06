from django.shortcuts import render
from .models import Topic

# filter() will always give you a QuerySet, even if only a single object matches the query - in this case, it will be a QuerySet containing a single element.
# If you know there is only one object that matches your query, you can use the get() method on a Manager which returns the object directly:
# >>> one_entry = Entry.objects.get(pk=1)

# Create your views here.

def index(request):
    """The home page for Learning log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by("date_added")
    context = {"Topics": topics}
    #print("Topics=",topics)
    return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
    """Show a single topoic and all its entries."""
    topic= Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {"topic": topic, "entries": entries}
    return render(request, 'learning_logs/topic.html', context)
