from rest_framework import generics, status
from rest_framework.response import Response
from .models import BloodRequest, Donor, Notification, Donation
from .serializers import BloodRequestSerializer, DonationSerializer
from datetime import timedelta
from django.utils import timezone
import requests

class BloodRequestCreateView(generics.CreateAPIView):
    serializer_class = BloodRequestSerializer

    def perform_create(self, serializer):
        blood_request = serializer.save()

        # Find eligible donors
        eligible_donors = Donor.objects.filter(
            blood_type=blood_request.blood_type,
            status='AV',
            last_donated_date__lte=timezone.now().date() - timedelta(days=90)
        )

        # Send notifications to eligible donors
        for donor in eligible_donors:
            Notification.objects.create(donor=donor, blood_request=blood_request)
            if donor.fcm_token:
                self.send_push_notification(donor.fcm_token, blood_request)

        return blood_request

    def send_push_notification(self, token, blood_request):
        url = "https://fcm.googleapis.com/fcm/send"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=YOUR_SERVER_KEY'  # Replace with your Firebase server key
        }
        data = {
            "to": token,
            "notification": {
                "title": "Blood Donation Request",
                "body": f"A new blood donation request for {blood_request.blood_type} blood type. Please help if you can!"
            }
        }
        requests.post(url, headers=headers, json=data)

class DonorAcceptRequestView(generics.UpdateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.approved_by_receiver = True
        instance.save()

        # Add donor's name to blood unit database
        BloodUnit.objects.create(donor=instance.donor, blood_request=instance.blood_request)

        # Send notification to the requester
        blood_request = instance.blood_request
        receiver = blood_request.receiver
        if receiver.fcm_token:
            self.send_push_notification(receiver.fcm_token, blood_request)

        return Response({"status": "Donation accepted and added to blood unit database"}, status=status.HTTP_200_OK)

    def send_push_notification(self, token, blood_request):
        url = "https://fcm.googleapis.com/fcm/send"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=YOUR_SERVER_KEY'  # Replace with your Firebase server key
        }
        data = {
            "to": token,
            "notification": {
                "title": "Donation Accepted",
                "body": f"Your request for {blood_request.blood_type} blood type has been accepted by a donor."
            }
        }
        requests.post(url, headers=headers, json=data)

class ConfirmDonationView(generics.UpdateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.approved_by_receiver = True
        instance.save()

        # Add points to donor account
        if instance.donor:
            instance.donor.points += 10  # Assuming donation through app gives 10 points
            instance.donor.save()

        # Generate certificate (placeholder for actual certificate generation logic)
        self.generate_certificate(instance)

        return Response({"status": "Donation confirmed, points added and certificate generated"}, status=status.HTTP_200_OK)

    def generate_certificate(self, donation):
        # Placeholder for actual certificate generation logic
        pass
