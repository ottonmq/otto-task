from django.apps import AppConfig

class MarketappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marketapp'
    # Nombre estético para el panel
    verbose_name = 'Otto-market'
