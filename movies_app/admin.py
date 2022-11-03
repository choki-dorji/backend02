from django.contrib import admin
from .models import ChildData, Marriage, User
from django.core.mail import EmailMessage
from django.conf import settings
# Register your models here.
# admin.site.register(Watchlist)
# admin.site.register(StreamPlatforms)
@admin.register(User)
class MaleUserDataAdmin(admin.ModelAdmin):
    list_display = ['CID','Name', 'email', 'Village', 'Chiwog', 'HouseHoldNo', 'contact_number', 'status']
    # list_filter = ['CID']
    search_fields = ['CID']
    actions = ['make_published']
    # print(list_display[0])

    # print(list_display[0])
    def make_published(self, request, queryset):
        queryset.update(status=True)

        for obj in queryset:
            print("Hello", obj.email)
            email1 = EmailMessage(
                "Gewog Management System",
                "Hello " + obj.Name + " You have successfully added your data.",
                settings.EMAIL_HOST_USER,
                # [MaleUserData.email],
                [obj.email]
                )
            email1.fail_silently = False
            email1.send()

        # print("model "+ str(model.contact_number))

        # account_sid = 'ACf70ad91e8f4df46cf76d6a474df9b45a'
        # auth_token = 'a41f8a27a9cdd87669caf8b0c9017e2b'
        # client = Client(account_sid, auth_token)
        # message = client.messages.create(
        # body='Dear Customer have won the lottery',
        # from_='[+18582408109]',
        # to=['+97517990855']
        # )
        # print(message.sid)

        # print(MaleUserDataAdmin.list_display[0])
        



# admin.site.register(Review)
# admin.site.register(User)
admin.site.register(Marriage)
admin.site.register(ChildData)
