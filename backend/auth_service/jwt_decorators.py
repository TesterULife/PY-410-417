from functools import wraps

from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication


def jwt_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        auth = JWTAuthentication()

        try:
            user_auth_tuple = auth.authenticate(request)

            if user_auth_tuple is None:
                return JsonResponse(
                    {'detail': 'Authentication credentials were not provided'},
                    status=401
                )

            user, token = user_auth_tuple

            request.user = user
            request.auth = token

        except Exception as e:
            return JsonResponse(
                {'detail': str(e)},
                status=401
            )

        return view_func(request, *args, **kwargs)

    return wrapper