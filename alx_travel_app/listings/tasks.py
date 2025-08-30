from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(user_email, booking_id):
    subject = "Booking Confirmation"
    message = f"Thank you for your booking! Your booking ID is {booking_id}."
    send_mail(subject, message, "no-reply@alxtravel.com", [user_email])
    return f"Booking confirmation sent to {user_email}"
