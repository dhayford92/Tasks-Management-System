from django import template
from core_utils.models import NotificationModel


register = template.Library()


@register.inclusion_tag('utils/notification_alert.html', takes_context=True)
def show_notifications(context):
    request_user = context['request'].user
    notifications = NotificationModel.objects.filter(to_user=request_user).exclude(isSeen=True).order_by('-create_on')
    return {'notifications': notifications}