from rest_framework_simplejwt import authentication


def custom_payload_handler(user):
    """
    Özel JWT payload işleyicisi.
    """
    payload = authentication.api_settings.JWT_PAYLOAD_HANDLER(user)
    payload['groups'] = user.groups  # Kullanıcının grubunu payload'a ekleyin
    return payload
