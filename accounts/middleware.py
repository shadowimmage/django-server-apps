from social_django.middleware import SocialAuthExceptionMiddleware
from django.shortcuts import redirect

class CustomSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_message(self, request, exception):
        # default_msg = super(CustomSocialAuthExceptionMiddleware).get_message(request, exception)
        
        return 'A login error occurred: {cause}'.format(cause=exception)