from rest_framework import viewsets, permissions
from .models import Murojaat
from .serializers import MurojaatSerializer
from .telegram import send_to_admins


class MurojaatViewSet(viewsets.ModelViewSet):
    queryset = Murojaat.objects.all().order_by("-created_at")
    serializer_class = MurojaatSerializer

    def get_permissions(self):
        # Form chiqishi va POST ishlashi uchun
        if self.action in ["create", "list"]:
            return [permissions.AllowAny()]

        # Detail, delete, edit – faqat admin
        return [permissions.IsAdminUser()]

    def perform_create(self, serializer):
        murojaat = serializer.save()

        text = (
            "📨 *Yangi murojaat!*\n\n"
            f"👤 Ism: {murojaat.firstname} {murojaat.lastname}\n"
            f"📧 Email: {murojaat.email}\n"
            f"📝 Murojaat: {murojaat.murojaat}\n"
            f"⏰ Vaqti: {murojaat.created_at.strftime('%d-%m-%Y %H:%M')}"
        )

        send_to_admins(text)
