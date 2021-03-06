from django.shortcuts import render
from faker import Faker
from .models import Job
from decouple import config
import requests


# Create your views here.
def index(request):
  return render(request,'jobs/index.html')

def past_job(request):
  name = request.POST.get('name')
  user = Job.objects.filter(name=name).first()

  if user :
    past_job = user.past_job

  else:

    faker = Faker()
    past_job = faker.job()
    job = Job(name=name, past_job=past_job)
    job.save()

  api_url = config('API_URL')
  api_key = config('API_KEY')

  data = requests.get(f'{api_url}?api_key={api_key}&q={past_job}&limit=1&lang=ko').json()

  try: img_url = data.get('data')[0].get('images').get('original').get('url')
  except IndexError:
    img_url = None

  context = {
    'name': name,
    'past_job':past_job,
    'img_url' : img_url,
  }
  return render(request,'jobs/past_job.html', context)
