from django.db import models
from ..account.models import CustomUserModel


class TicketCategories(models.Model):
    name = models.CharField(max_length=150)
    COLORS = [
        ('red', 'Kırmızı'),
        ('blue', 'Mavi'),
        ('green', 'Yeşil'),
        ('orange', 'Turuncu')
    ]
    color = models.CharField(max_length=20, choices=COLORS, default='red')

    class Meta:
        db_table = 'ticket_categories'
        verbose_name = 'Destek Kategorisi'
        verbose_name_plural = 'Destek Kategorileri'

    def __str__(self):
        return self.name


class TicketStatuses(models.Model):
    name = models.CharField(max_length=150)
    COLORS = [
        ('red', 'Kırmızı'),
        ('blue', 'Mavi'),
        ('green', 'Yeşil'),
        ('orange', 'Turuncu')
    ]
    color = models.CharField(max_length=20, choices=COLORS, default='green')

    class Meta:
        db_table = 'ticket_statuses'
        verbose_name = 'Destek Durumu'
        verbose_name_plural = 'Destek Durumları'

    def __str__(self):
        return self.name


class TicketPriorities(models.Model):
    name = models.CharField(max_length=150)
    COLORS = [
        ('red', 'Kırmızı'),
        ('blue', 'Mavi'),
        ('green', 'Yeşil'),
        ('orange', 'Turuncu')
    ]
    color = models.CharField(max_length=20, choices=COLORS, default='blue')

    class Meta:
        db_table = 'ticket_priorities'
        verbose_name = 'Destek Önceliği'
        verbose_name_plural = 'Destek Öncelikleri'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    subject = models.CharField(max_length=150)
    content = models.TextField()
    status = models.ForeignKey(TicketStatuses, on_delete=models.SET_DEFAULT, related_name='status_tickets', default=1)
    priority = models.ForeignKey(TicketPriorities, on_delete=models.SET_DEFAULT, related_name='priority_tickets',
                                 default=1)
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='user_tickets')
    agent = models.ForeignKey(CustomUserModel, on_delete=models.SET_NULL, related_name='agent_tickets',
                              limit_choices_to={'ticket_admin': True, 'ticket_agent': True}, null=True, blank=True)
    category = models.ForeignKey(TicketCategories, on_delete=models.SET_DEFAULT, related_name='category_tickets',
                                 default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'tickets'
        verbose_name = 'Destek Talebi'
        verbose_name_plural = 'Destek Talepleri'

    def __str__(self):
        return self.user.get_full_name()


class TicketReplies(models.Model):
    content = models.TextField()
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='ticket_comments')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ticket_replies'
        verbose_name = 'Destek Yanıtı'
        verbose_name_plural = 'Destek Yanıtları'

    def __str__(self):
        return self.user.get_full_name()


class TicketCategoriesUsers(models.Model):
    category = models.ForeignKey(TicketCategories, on_delete=models.CASCADE, related_name='categories_user')
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='categories_category')

    class Meta:
        db_table = 'ticket_categories_users'
        verbose_name = 'Destek Kategori Yetkisi'
        verbose_name_plural = 'Destek Kategori Yetkileri'

    def __str__(self):
        return self.category.name
