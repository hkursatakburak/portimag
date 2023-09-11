from django.shortcuts import render,get_object_or_404
from . models import Topic,Category,Tag

def topic_list(request, category_slug = None, tag_slug = None):
    category_page = None
    tag_page = None
    category = Category.objects.all()
    tag = Tag.objects.all()

    if category_slug != None:
        category_page = get_object_or_404(Category, slug = category_slug)
        topics = Topic.objects.filter(available = True, category = category_page)
    
    elif tag_slug != None:
        tag_page = get_object_or_404(Tag,slug = tag_slug)
        topics = Topic.objects.filter(available = True, tag = tag_page)
    
    else:
        topics = Topic.objects.all().order_by("-date")

    context = {
        'topics' : topics,
        'categories' : category,
        'tags' : tag
        }
    return render(request, 'topics.html', context)
    
def topic_detail(request, category_slug, topic_id):
    topics = Topic.objects.get(category__slug = category_slug, id = topic_id)

    context = {
        'topics' : topics
    }
    return render(request, 'topic.html', context)

def search(request):
    topics = Topic.objects.filter(name__contains = request.GET['search'])
    category = Category.objects.all()
    tag = Tag.objects.all()

    context = {
        'topics' : topics,
        'categories' : category,
        'tags' : tag
        }
    return render(request, 'topics.html', context)