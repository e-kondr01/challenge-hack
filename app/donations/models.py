from django.db import models


class Donation(models.Model):

    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Сумма")

    currency = models.CharField(max_length=15, default="руб.", verbose_name="Валюта")

    author_name = models.CharField(max_length=127, verbose_name="Имя автора")

    message = models.CharField(max_length=1023, verbose_name="Текст сообщения")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания"
    )

    attachment_url = models.URLField(blank=True, verbose_name="URL вложения")

    def __str__(self) -> str:
        return f"{self.author_name}: {self.message}"

    class Meta:
        verbose_name = "Донат"
        verbose_name_plural = "Донаты"
