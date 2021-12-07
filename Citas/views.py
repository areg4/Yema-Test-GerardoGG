from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.translation import ugettext as _

# Create your views here.
@csrf_exempt
def solicitarCita(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        comentario = json_data["comentario"]
        fechaHora = json_data['fechaHora']
        idPediatra = json_data['idPediatra']

        msg_response = _("Solicitud recibida")

        return JsonResponse({"msg":msg_response}, status=200)
    msg_bad_response = _("La Solicitud no está por POST")
    return JsonResponse({"msg":msg_bad_response},status=400)