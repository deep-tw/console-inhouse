# Generated by Django 4.1.3 on 2022-12-29 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("account_system", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, default="")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Not Started", "Not Started"),
                            ("In Progress", "In Progress"),
                            ("Closed", "Closed"),
                            ("Terminated", "Terminated"),
                        ],
                        max_length=55,
                    ),
                ),
                ("start_date", models.DateField(null=True)),
                ("close_date", models.DateField(null=True)),
                (
                    "bde_manager",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_set",
                        to="account_system.manager",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "reporting_manager",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project",
                        to="account_system.manager",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]