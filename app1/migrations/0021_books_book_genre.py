# Generated by Django 4.2.1 on 2023-06-02 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_remove_books_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app1.bookgenre'),
        ),
    ]
