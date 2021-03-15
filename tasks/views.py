from django.shortcuts import render
from django.views import View


# Create your views here.
class home(View):
    #need to para di na paulot ulit ng template name sa return self.template_name nalang gagamitin
    template_name = 'tasks/home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
