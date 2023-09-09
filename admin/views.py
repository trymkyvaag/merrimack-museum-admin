from django_nextjs.render import render_nextjs_page_sync

def home(request):
    return render_nextjs_page_sync(request)
