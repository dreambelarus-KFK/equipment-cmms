from django.db import models


class Equipment(models.Model):
    name = models.CharField("Название", max_length=255)
    inventory_number = models.CharField("Инвентарный номер", max_length=100, unique=True)
    manufacturer = models.CharField("Производитель", max_length=255, blank=True, null=True)
    location = models.CharField("Местоположение", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"


class Failure(models.Model):
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name="failures",
        verbose_name="Оборудование"
    )

    title = models.CharField("Краткое описание", max_length=255)
    description = models.TextField("Описание")

    failure_date = models.DateTimeField("Дата отказа")

    status = models.CharField(
        "Статус",
        max_length=50,
        choices=[
            ("open", "Открыт"),
            ("in_progress", "В работе"),
            ("closed", "Закрыт"),
        ],
        default="open"
    )

    def __str__(self):
        return f"{self.equipment.name} - {self.title}"

    class Meta:
        verbose_name = "Отказ"
        verbose_name_plural = "Отказы"