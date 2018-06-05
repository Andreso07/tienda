from django.urls import path
from tiendaDia import views 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('', login_required(views.first_view), name='base'),
    path('producto/', login_required(views.ProductoListView.as_view()), name='producto-list'),
    path('producto/<int:pk>/detail', login_required(views.ProductoDetailView.as_view()), name='producto-detail'), 

    path('venta/', login_required(views.VentaListView.as_view()), name='venta-list'),
    path('venta/<int:pk>/detail', login_required(views.VentaDetailView.as_view()), name='venta-detail'), 

    path('venta/create/', login_required(views.VentaCreate.as_view()), name='venta-create'),
    path('producto/create/', login_required(views.ProductoCreate.as_view()), name='producto-create'),

    path('producto/<int:pk>/update/', login_required(views.ProductoUpdate.as_view()), name='producto-update'),
    path('venta/<int:pk>/update/', login_required(views.VentaUpdate.as_view()), name='venta-update'),

    path('producto/<int:pk>/delete/', login_required(views.ProductoDelete.as_view()), name='producto-delete'),
    path('venta/<int:pk>/delete/', login_required(views.VentaDelete.as_view()), name='venta-delete'),
]