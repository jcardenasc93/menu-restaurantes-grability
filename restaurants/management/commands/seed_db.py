from django.core.management.base import BaseCommand
from rest_framework_api_key.models import APIKey
from django.conf import settings
import os.path

from restaurants.factory_data import RestaurantFactory, ProductFactory


class Command(BaseCommand):
    help = 'Populate database for API testing'

    def add_arguments(self, parser):
        ''' Fuunción que define los argumentos de entrada que se pueden
        pasar en la ejecución del comando
        '''
        parser.add_argument(
            '--restaurants',
            default=50,
            type=int,
            help='Number of restaurants to create (default 50)'
        )

        parser.add_argument(
            '--products',
            default=50,
            type=int,
            help='Number of products to create for each restaurant (default 50)'
        )

    def handle(self, *args, **options):
        ''' Crea n restaurantes y n productos definidos por el usuario y
        los almacena en la base de datos. Además genera un API-KEY
        inicial
        '''

        for i in range(options['restaurants']):
            restaurant = (RestaurantFactory.create())
            for j in range(options['products']):
                ProductFactory.create(restaurant=restaurant)

            print('> ' + str(i + 1) + ' created restaurants')

        # Genera el API-KEY de autorización
        api_key, key = APIKey.objects.create_key(name="INITIAL-KEY")

        if key:
            print('> Generating API-KEY ..... Success!')

            # Valida si el archivo api_key.txt existe
            if os.path.isfile(os.path.join(settings.BASE_DIR, 'api_key.txt')):
                with open(os.path.join(settings.BASE_DIR, 'api_key.txt'), 'a') as api_file:
                    # Actualiza el archivo con la información del API_KEY generado
                    print(f'-' * 70, file=api_file)
                    print(f'API-KEY:' + str(api_key), file=api_file)
                    print(f'KEY:' + str(key), file=api_file)
                print('> File api_key.txt file updated')

            else:
                with open(os.path.join(settings.BASE_DIR, 'api_key.txt'), 'w') as api_file:
                    # Crea el archivo con la información del API_KEY generado
                    print(f'-' * 70, file=api_file)
                    print(f'API-KEY:' + str(api_key), file=api_file)
                    print(f'KEY:' + str(key), file=api_file)
                print('> File api_key.txt created')

        else:
            print('> Generating API-KEY ..... Fail!')
