from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib import messages

import hashlib
from urllib.parse import urlparse

from .models import URLMapping


class ShortenURLView(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'index.html')

    def post(self, request, *args, **kwargs):
        url = self.request.POST['url-input']
        if not urlparse(url).scheme:
            url = 'http://' + url

        try:
            validator = URLValidator()
            validator(url)

            domain = urlparse(url).netloc.replace('www.', '')
            hashed = hashlib.md5(domain.encode()).hexdigest()[:7]

            duplicate_counter = 1
            while URLMapping.objects.filter(hashed=hashed).exists():
                hashed = hashed + str(duplicate_counter)
                duplicate_counter += 1

            URLMapping.objects.create(url=url, hashed=hashed)
            messages.success(self.request, f'Your shortened URL is: http://127.0.0.1:8000/{hashed}')
            return redirect('shorten-url')
        except ValidationError:
            messages.error(self.request, f'Please enter a valid URL format.')
            return redirect('shorten-url')


class RedirectURLView(View):
    def get(self, request, *args, **kwargs):
        hash_id = kwargs.get('hash_id')
        try:
            url_map = URLMapping.objects.get(hashed=hash_id)
            return HttpResponseRedirect(url_map.url)
        except URLMapping.DoesNotExist:
            return render(self.request, '404.html', status=404)
        except Exception as e:
            return render(self.request, '404.html', {'exception': e}, status=500)


