from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRPostalCodeField, BRStateField

from apps.common.models import TimeStampedUUIDModel
from apps.users.models import User


def upload_perfil_user(instance, filename):
    return f"profile_pictures/user_{instance.id}/{filename}"


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(
        User,
        verbose_name='Profile',
        related_name="profile",
        on_delete=models.CASCADE
    )
    about_me = models.TextField(
        verbose_name=_("About me"), default="say something about yourself"
    )
    cell_phone = models.CharField(
        "Telefone Celular",
        max_length=25,
        default="",
        blank=True,
        null=True,
    )
    postal_code = BRPostalCodeField(
        "CEP",
        default="",
        null=True,
        blank=True,
    )
    state = BRStateField(
        "Estado",
        default="",
        null=True,
        blank=True,
    )
    city = models.CharField(
        "Cidade",
        max_length=100,
        default="",
        null=True,
        blank=True,
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"),
        default="profile_default.png",
        upload_to=upload_perfil_user,
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "profiles.profile"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self) -> str:
        return str(self.id)
