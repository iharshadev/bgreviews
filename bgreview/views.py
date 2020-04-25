from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get(request):
    return HttpResponse("<pre>Hello world</pre>")


@api_view(['POST'])
def post_test(request):
    if request.method == 'POST':
        val = request.POST.get("key")
    else:
        val = "Wrong request type"
    return Response(val)
