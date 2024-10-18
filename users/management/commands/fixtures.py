import json

from django.core.management import BaseCommand

from school.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    @staticmethod
    def json_read_payment():
        """Читает данные оплаты из JSON-файла"""
        with open('data_payment.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):
        # Удаляет существующие данные
        Payment.objects.all().delete()
        payment_for_create = []

        for pay in self.json_read_payment():
            try:
                user = User.objects.get(pk=pay['user'])  # Получаем пользователя
                course = Course.objects.get(pk=pay['course'])  # Получаем курс
                lesson = Lesson.objects.get(pk=pay['lesson'])  # Получаем урок

                payment = Payment(
                    id=pay['id'],
                    date=pay['date'],
                    amount=pay['amount'],
                    payment_method=pay['payment_method'],
                    user=user,
                    course=course,
                    lesson=lesson,
                )
                payment_for_create.append(payment)
            except User.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"User with id {pay['user']} does not exist"))
            except Course.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Course with id {pay['course']} does not exist"))
            except Lesson.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Lesson with id {pay['lesson']} does not exist"))

        Payment.objects.bulk_create(payment_for_create)
        self.stdout.write(self.style.SUCCESS(f"Successfully added {len(payment_for_create)} payments."))
