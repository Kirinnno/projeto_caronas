# Generated by Django 5.2 on 2025-05-28 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viagens', '0003_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viagem',
            old_name='usuario',
            new_name='motorista',
        ),
        migrations.RemoveField(
            model_name='viagem',
            name='vagas_reservadas',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telefone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tipo_usuario',
            field=models.CharField(choices=[('motorista', 'Motorista'), ('passageiro', 'Passageiro')], max_length=20),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='vagas',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]
