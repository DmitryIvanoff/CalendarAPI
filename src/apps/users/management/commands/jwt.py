from django.core.management.base import BaseCommand
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Command(BaseCommand):
    help = 'Создает JWT токен по ID пользователя'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs=1, type=int)

    def handle(self, *args, **options):
        user_obj = UserModel.objects.get(pk=options['user_id'][0])

        refresh = RefreshToken.for_user(user_obj)

        self.stdout.write(self.style.SUCCESS(f'Successfully created JWT'))
        self.stdout.write(f"\nRefresh token: \n{str(refresh)}\n")
        self.stdout.write(f"\nAccess token: \n{str(refresh.access_token)}\n")
