import pytest
from Citas.models import Pediatra

@pytest.mark.django_db
def test_pediatra_create():
    pediatra = Pediatra.objects.create(
        nombre = "PediatraTest",
        apellidos = "ApellidosTest"
    )
    assert pediatra.nombre == "PediatraTest"