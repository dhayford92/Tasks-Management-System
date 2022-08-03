from django import template
from authentication.models import Profile

register = template.Library()


@register.filter
def user_profile(user):
    userprofile = Profile.objects.get(user=user)
    return userprofile.profile_image.url


@register.filter
def user_name(user):
    userprofile = Profile.objects.get(user=user)
    fullname = userprofile.user.first_name + " " + userprofile.user.last_name
    return fullname