from pathlib import Path
import time


BASE_DIR = Path(__file__).resolve().parent

class RequestInformationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_t = time.perf_counter()

        response = self.get_response(request)

        end_t = time.perf_counter()

        writable_dict = {
            'user': str(request.user),
            'ip': request.META.get('REMOTE_ADDR'),
            'method': request.method,
            'path': request.path,
            'query params': request.META.get('QUERY_STRING'),
            'user-agent': request.META.get('HTTP_USER_AGENT'),
            'referer': request.META.get('HTTP_REFERER'),
            'status_code': response.status_code,
            'execution_time': round(end_t - start_t, 4),
        }

        log_file = BASE_DIR / 'middlewares_logs' / 'middlewares_logs.txt'

        with open(log_file, 'a', encoding='utf-8') as file:
            file.write(f'{writable_dict}\n')

        return response