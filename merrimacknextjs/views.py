from django.views import View
from django.conf import settings
from django_nextjs.render import render_nextjs_page_sync
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render_nextjs_page_sync(request)

def gallery(request):
    return render_nextjs_page_sync(request)

def request(request):
    return render_nextjs_page_sync(request)

def about(request):
    return render_nextjs_page_sync(request)

def dashboard(request):
    return render_nextjs_page_sync(request)

class ProxyView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.path.startswith('/api/auth/'):
            nextjs_url = f'http://localhost:3000{request.path}'
            response = requests.request(
                request.method,
                nextjs_url,
                data=request.body,
                headers={key: value for key, value in request.headers.items() if key != 'Host'}
            )

            content_type = response.headers.get('Content-Type', 'text/plain')

            print("ProxyView - Next.js Response Status:", response.status_code)
            print("ProxyView - Next.js Response Headers:", response.headers)
            print("ProxyView - Next.js Response Content:", response.content)

            # Check for an empty response
            if not response.content:
                return HttpResponse(status=response.status_code, content_type=content_type)

            return HttpResponse(response.content, content_type=content_type)

        print("ProxyView - Not an API route, rendering Django view.")
        return self.handle_django_view(request, *args, **kwargs)

    def handle_django_view(self, request, *args, **kwargs):
        print("ProxyView - Rendering Django view using render_nextjs_page_sync.")
        response = render_nextjs_page_sync(request)
        print("ProxyView - Django view response:", response)
        return response   
        
# class ProxyView(View):
#     def dispatch(self, request, *args, **kwargs):
#         # Forward the request to the Next.js server
#         nextjs_url = f'http://localhost:3000{request.path}'
#         response = requests.request(request.method, nextjs_url, data=request.body, headers=request.headers)

#         # Get the 'Content-Type' header or provide a default value
#         content_type = response.headers.get('Content-Type', 'text/plain')

#         # Return the response from the Next.js server
#         return HttpResponse(response.content, content_type=content_type)