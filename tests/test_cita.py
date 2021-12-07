import json
import pytest
from django.test import Client, TestCase, client
from Citas.models import Cita, Pediatra
from datetime import datetime

@pytest.mark.django_db
def test_cita_create():
    pediatra = Pediatra.objects.create(
        nombre = "PediatraTest",
        apellidos = "ApellidosTest"
    )
    
    cita = Cita.objects.create(
        comentario = "Comentario de prueba",
        fechaHora = datetime.strptime('01/01/2021 00:00:00', '%d/%m/%Y %H:%M:%S'),
        pediatra = pediatra,
        emailContacto = "test@mail.com"
    )
    assert cita.emailContacto == "test@mail.com"

def test_solicitar_cita():
    client = Client()
    request_body = {
        "comentario" : "Un comentario",
        "fechaHora" : "07/12/2021 15:00:00",
        "idPediatra" : "1"
    }
    response = client.post(
        '/api/solicitarCita/',
        request_body,
        'application/json'
    )

    assert response.status_code == 200
    expected = {
        "msg": "Solicitud recibida"
    }
    expected_trs = {
        "msg": "Request received"
    }

    assert response.json() == expected or response.json == expected_trs