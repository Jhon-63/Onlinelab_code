from django.utils.deprecation import MiddlewareMixin


class MyTest(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = "http://127.0.0.1:8080"


        return response