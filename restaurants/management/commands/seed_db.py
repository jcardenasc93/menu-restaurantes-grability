from django.core.management.base import BaseCommand

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
        los almacena en la base de datos
        '''

        for i in range(options['restaurants']):
            restaurant = (RestaurantFactory.create())
            for j in range(options['products']):
                ProductFactory.create(restaurant=restaurant)
                
            print('> ' + str(i + 1) + ' ceated restaurants')
