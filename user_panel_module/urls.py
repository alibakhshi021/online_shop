from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserPanelDashboardPageView.as_view(), name="user_panel_dashboard"),
    path(
        "change-pass/", views.ChangePasswordPageView.as_view(), name="change_password"
    ),
    path(
        "edit-profile/", views.EditUserProfilePageView.as_view(), name="edit_user_panel"
    ),
    path("user-basket", views.user_basket, name="user_basket_product"),
    path("remove-order-detail", views.remove_order_detail, name="remove_order_detail"),
    path(
        "change-order-detail",
        views.change_order_detail_count,
        name="remove_order_detail",
    ),
]
