from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers

from agenda.models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ["id", "data_horario", "nome_cliente", "email_cliente", "telefone_cliente", "deletado", "prestador"]

    prestador = serializers.CharField()

    def validate_prestador(self, value):
        """ Buscar um user no BD que esteja associado ao username que foi passado."""
        try:
            prestador_obj = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("username não existe!")
        return prestador_obj
    
    
    def validate_data_horario(self, value):
        if value < now():
            raise serializers.ValidationError("Agendamento não pode ser feito no passado!")
        return value


    def validate(self, attrs):
        telefone_cliente = attrs.get("telefone_cliente", "")
        email_cliente = attrs.get("email_cliente", "")
        
        if email_cliente.endswith(".br") and telefone_cliente.startswith("+") and not telefone_cliente.startswith("+55"):
            raise serializers.ValidationError("Email brasileiro deve estar associado a um número de telefone do Brasil (+55).")
        
        # Adiciona validação para impedir modificações em agendamentos deletados
        if attrs.get("deletado", False):
            raise serializers.ValidationError("Não é permitido modificar um agendamento deletado.")
        
        return attrs
