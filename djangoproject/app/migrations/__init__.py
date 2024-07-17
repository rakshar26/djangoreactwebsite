from django.db import migrations

def create_data(apps, schema_editor):
    Student = apps.get_model('app', 'Student')
    Student(name="Joe Silver", email="joe@email.com", description="22342342", phone="00000000").save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]