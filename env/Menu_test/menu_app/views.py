from django.shortcuts import render



def example_page(request):
    
    return render(request, 'menu/menu_template.html')
