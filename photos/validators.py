from django.core.exceptions import ValidationError

BADWORDS = (
            "Caranabo",
            "Carapan",
            "Chimpamonas",
            "Chupaescrotos",
            "Cuerpoescombro"
            )


def badwords(description):
    """
    Valida que la descripcion no contenga ninguna palabrota
    :return: diccionario con los datos limpios y validados
    """

    for badword in BADWORDS:
        if badword in description:
            raise ValidationError("La palabra {0} no esta permitida".format(badword))
    return True
