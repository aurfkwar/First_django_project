from django.shortcuts import render

# Create your views here.
def dict_lookup(request):
    #creating a dictionary of items
    data = ({'Name': 'Frederick Kwarteng',
    'Track': 'Backend(python)',
    'Message': 'You are doing a great job! I am priviledged to have you as my mentor.'})

    #creating a content to refer the dictionary elements
    data2 = {'data1': data}

    #calling the render() method to render the request from template_ex.htm page by using the dictionary data2
    return render(request, "template.htm", data2)
