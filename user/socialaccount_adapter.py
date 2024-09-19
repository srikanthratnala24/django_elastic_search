from allauth.socialaccount.models import SocialToken, SocialAccount
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added

@receiver(social_account_added)
def retrieve_access_token(sender, request, sociallogin, **kwargs):
    user = sociallogin.user
    token = SocialToken.objects.filter(account__user=user, account__provider='google').first()
    if token:
        access_token = token.token
        # Do something with the access token, like store it or use it to fetch additional data
