# Generated by Django 4.2.7 on 2024-01-17 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("agency_system", "0011_comment_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReplyComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reply_body", models.TextField()),
                ("reply_date", models.DateTimeField(auto_now_add=True)),
                (
                    "reply_author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author_replies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "reply_comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_replies",
                        to="agency_system.comment",
                    ),
                ),
            ],
        ),
    ]
