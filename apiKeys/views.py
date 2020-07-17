from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser

from rest_framework import status
from rest_framework.response import Response
from rest_framework_api_key.models import APIKey


# Create your views here.


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createAPIKey(request):
    ''' View basado en funcion empleado para crear un API-KEY para
    la aplicación. El proceso de autenticación es a través de JWT
    y valida que el usuario autenticado sea administrador
    '''

    # El parametro 'name' es obligatorio para proceder con la petición
    try:
        name = request.data['name']
    except:
        name = None
    if name:
        api_key, key = APIKey.objects.create_key(name=name)
        return Response({'detail': 'API Key created successfuly', 'api-key': str(api_key), 'key': str(key)}, status=status.HTTP_201_CREATED)
    else:
        return Response({'detail': 'Param name not provided'}, status=status.HTTP_400_BAD_REQUEST)
