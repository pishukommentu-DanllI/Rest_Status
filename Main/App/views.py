from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from rest_framework.views import APIView


class Api(APIView):
    model = None
    serializer = None
    model_name = None

    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if pk:
            try:
                obj = self.model.objects.get(id=pk)
                response = {self.model_name: self.serializer(obj, many=False).data}
                return JsonResponse(response, status=HTTP_200_OK)
            except:
                return JsonResponse({'error': 'Object does not exit'}, status=HTTP_404_NOT_FOUND)

        objs = self.model.objects.all()
        response = {self.model_name: self.serializer(objs, many=True).data}
        return JsonResponse(response, status=HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = {self.model_name: serializer.data}
        return JsonResponse(response, status=HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return JsonResponse({'error': 'Method PUT not allowed'})

        try:
            instance = self.model.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'Object does not exit'})

        serializer = self.serializer(data=request.data, instance=instance)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = {self.model_name: serializer.data}
        return JsonResponse(response, status=HTTP_204_NO_CONTENT)

    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk', None)

        if not pk:
            return JsonResponse({'error': 'Method DELETE not allowed'}, status=HTTP_404_NOT_FOUND)

        try:
            obj = self.model.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'Object does not exit'}, status=HTTP_404_NOT_FOUND)

        obj.delete()

        return JsonResponse({'product': 'delete ' + str(obj)}, status=HTTP_204_NO_CONTENT)
