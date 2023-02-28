from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404
from django.urls import reverse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.account.tasks import send_activation_code
from apps.account.models import CustomUser
from apps.account.serializers import RegisterCustomUserSerializers, LoginUserSerializer


class RegisterView(APIView):

    serializer_class = RegisterCustomUserSerializers

    @swagger_auto_schema(
        request_body=RegisterCustomUserSerializers,
        operation_summary='Регистрация пользователя',
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        email = serializer.data.get('email')

        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            current_site = get_current_site(request=request).domain
            relative_link = reverse('activate-email', kwargs={'activation_code': user.activation_code})
            absolute_link = 'http://' + current_site + relative_link
            send_activation_code.delay(absolute_link, user.email)
        return Response({
            'success': 'Вы успешно зарегистрировались',
            'message': 'Вам отправлено электронное письмо для активации аккаунта.'
        }, status=status.HTTP_201_CREATED
        )


@swagger_auto_schema(
    method='GET',
    operation_summary='Запрос для активации аккаунта',
)
@api_view(['GET'])
def activate_view(request, activation_code):
    user = get_object_or_404(CustomUser, activation_code=activation_code)
    user.is_active = True  # делаем активым
    user.activation_code = ''  # удаляем активационный код
    user.save()
    return Response("Вы успешно активировали аккаунт", 200)


class LoginAPIView(APIView):

    serializer_class = LoginUserSerializer

    @swagger_auto_schema(
        request_body=LoginUserSerializer,
        operation_summary='Авторизация пользователя',
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
