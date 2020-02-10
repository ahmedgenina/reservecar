from django.db import models
# Create your models here.


class Motorista(models.Model):
    SEXO_CHOICES = (
        ("feminino", "Feminino"),
        ("masculino", "Masculino"),
    )
    nome = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=11, null=False)
    telefone = models.CharField(max_length=20, null=False)
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    ESTADO_CHOICES = (
        ("disponível", "Disponível"),
        ("manutenção", "Manutenção"),
    )
    modelo = models.CharField(max_length=50, null=False)
    placa = models.CharField(max_length=8, null=False)
    ano = models.CharField(max_length=4, null=False)
    estado = models.CharField(max_length=20, null=False, choices=ESTADO_CHOICES)
    foto_veiculo = models.ImageField(upload_to='images')

    def __str__(self):
        return 'Modelo: ' + self.modelo + ' Placa: ' + self.placa


class Reserva(models.Model):
    data_inicio = models.DateTimeField(null=False)
    data_final = models.DateTimeField(null=False)
    veiculo = models.ForeignKey('Veiculo', on_delete=models.PROTECT)
    motorista = models.ForeignKey('Motorista', on_delete=models.PROTECT)
    estado_reserva = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.veiculo
