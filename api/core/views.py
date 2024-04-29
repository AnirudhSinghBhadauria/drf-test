from django.http import JsonResponse

def home_view(request, *args, **kwargs):
    return JsonResponse(
        {
            "name": "anirudh",
            "middle": "Singh",
            "last": "Bhadauria"
        }
    )

