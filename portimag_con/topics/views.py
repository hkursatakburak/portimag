from django.shortcuts import render
from . models import Topic,Category,Tag


def topic_list(request):
    topics = Topic.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'topics' : topics,
        'categories' : categories,
        'tag' : tags
    }
    return render(request, 'topics.html', context)

def topic_detail(request, topic_slug, topic_id):
    topics = Topic.objects.get(category__slug = topic_slug, id = topic_id)

    context = {
        'topics' : topics
    }
    return render(request, 'topic.html', context)

def category_list(request, category_slug,):
    topic= Topic.objects.all().filter(category__slug = category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'topic' : topic,
        'categories' : categories,
        'tag' : tags
    }
    return render(request, 'topics.html', context)

def tag_list(request, tag_slug,):
    topic= Topic.objects.all().filter(tag__slug = tag_slug)
    categories = Category.objects.all()
    tags = Category.objects.all()

    context = {
        'topic' : topic,
        'categories' : categories,
        'tag' : tags
    }
    return render(request, 'topics.html', context)
