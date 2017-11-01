import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import keyboards
from . import library_crawl

# Create your views here.
def keyboard(request):
    return JsonResponse(keyboards.default_keyboard())

@csrf_exempt
def message(request):
    json_str = (request.body).decode('utf-8')
    received_json_data = json.loads(json_str)
    content_msg = received_json_data['content']

    if content_msg == "도서관현황":
        return JsonResponse({
            'message' :{
                'text' : library_crawl.get(),
            },
            'keyboard' : keyboards.default_keyboard()
})
