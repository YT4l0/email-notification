# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

from .serializers import NotificationSerializer
from .models import Notification

class NotificationView(APIView):
    """
    Endpoint para enviar notificações por e-mail.
    """
    def post(self, request, *args, **kwargs):
        serializer = NotificationSerializer(data=request.data)
        
        # Valida os dados recebidos (email, subject, message)
        if serializer.is_valid():
            data = serializer.validated_data
            email_to = data['email']
            subject = data['subject']
            message = data['message']

            # Verificação: já existe notificação idêntica para esse usuário?
            if Notification.objects.filter(email=email_to, subject=subject, message=message).exists():
                return Response(
                    {"message": "Essa notificação já foi enviada anteriormente."},
                    status=status.HTTP_200_OK
                )
            
            try:
                # Tenta enviar o e-mail usando as configurações do settings.py
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER, # Remetente
                    [email_to],               # Destinatário
                    fail_silently=False,
                )
                
                # Se o e-mail for enviado com sucesso, salva a notificação no banco
                Notification.objects.create(
                    email=email_to,
                    subject=subject,
                    message=message
                )
                
                return Response({"message": "Notificação enviada com sucesso!"}, status=status.HTTP_200_OK)
            
            except Exception as e:
                # Em caso de erro no envio, retorna uma mensagem de erro
                return Response({"error": f"Falha ao enviar e-mail: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
        # Se os dados forem inválidos, retorna os erros de validação
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        nova-funcionalidade
