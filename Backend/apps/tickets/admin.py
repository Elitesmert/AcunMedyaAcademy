from django.contrib import admin
from .models import Ticket, TicketCategories, TicketPriorities, TicketStatuses, TicketReplies

admin.site.register(Ticket)
admin.site.register(TicketCategories)
admin.site.register(TicketPriorities)
admin.site.register(TicketStatuses)
admin.site.register(TicketReplies)
