from django.http import HttpResponse

# data = {

#    "Name" : "Oluwafemi Adenuga",

#     "Track" : "Backend(Python)",

#     "Message" : "Hi, mentor, you're doing a great job"


# Create your views here.
def index(request):
    #for key,value in data.items():
        return HttpResponse("My Name is Frederick Kwarteng \n I belong to Backend(Python) track\nHi, mentor, you are the best")
    #    return HttpResponse(data, headers={"Name" : "Oluwafemi Adenuga",

    # "Track" : "Backend(Python)",

    # "Message" : "Hi, mentor, you're doing a great job" })
