from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import ugettext as _

# Create your models here.
class Pediatra(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        txt = "{0} {1}".format(self.nombre,self.apellidos)
        return txt
    

class Cita(models.Model):
    comentario = models.TextField(null=False,blank=False,max_length=500)
    fechaHora = models.DateTimeField(null=False, blank=False)
    pediatra = models.ForeignKey(Pediatra, null=False,blank=False, on_delete=models.CASCADE)
    emailContacto = models.EmailField(null=False,blank=False)

    def __str__(self):
        fechaHora = timezone.localtime(self.fechaHora)
        fechaFormated = fechaHora.strftime("%d/%m/%Y %H:%M:%S")
        txt = _("Cita con el pediatra: ")
        txt += "{} ".format(self.pediatra)
        txt += _("para el día ")
        txt += "{} ".format(fechaFormated)
        return txt

    def save(self, *args, **kwargs):
        txt_mail = self.make_email_txt()
        self.send_email(txt_mail,self.emailContacto)
        super(Cita, self).save(*args, **kwargs)

    def send_email(self,txt_mail,emailContacto):
        asunto = _("Registro de Cita")
        email_desde = settings.EMAIL_HOST_USER
        email_para = [emailContacto]
        send_mail(asunto,txt_mail,email_desde,email_para,fail_silently=False)

    def make_email_txt(self):
        txt_mail = _("Buen día,")
        txt_mail += "\n\n"
        txt_mail += _("Se ha registrado una cita para el día ")
        txt_mail += "{} ".format(self.fechaHora.strftime("%d/%m/%Y %H:%M"))
        txt_mail += _("con el Pediatra: ")
        txt_mail += "{}.".format(self.pediatra)
        txt_mail += "\n\n"
        txt_mail += _("Con los siguientes comentarios:")
        txt_mail += "\n\n"
        txt_mail += "{}".format(self.comentario)
        txt_mail += "\n\n"
        txt_mail += _("Saludos")
        
        return txt_mail
