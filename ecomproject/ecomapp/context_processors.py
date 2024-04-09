from .models import Carts

def count_context(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        count = Carts.objects.filter(user_id=user_id).exclude(status="order-placed").count()
    else:
        count = 0  # or any default value if user is not authenticated
    return {'cart_count': count}