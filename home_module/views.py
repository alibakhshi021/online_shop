from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView
from product_module.models import Product, ProductCategory
from site_module.models import SiteSetting, FooterLinkBox, Slider
from utils.conventors import group_list


class HomeView(TemplateView):
    template_name = "index_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        context["sliders"] = sliders
        latest_products = Product.objects.filter(
            is_active=True, is_delete=False
        ).order_by("id")[:12]
        most_visit_product = (
            Product.objects.filter(is_active=True, is_delete=False)
            .annotate(visit_count=Count("productvisit"))
            .order_by("-visit_count")[:12]
        )
        context["latest_products"] = group_list(latest_products)
        context["most_visit_product"] = group_list(most_visit_product)
        categories = list(
            ProductCategory.objects.annotate(
                products_count=Count("product_categories")
            ).filter(is_active=True, is_delete=False, products_count__gt=0)[:6]
        )
        categories_products = []
        for category in categories:
            item = {
                "id": category.id,
                "title": category.title,
                "products": list(category.product_categories.all()),
            }
            categories_products.append(item)
            print(categories_products)
        context["categories_products"] = categories_products
        return context


def site_header_partial(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    return render(request, "shared/site_header_partial.html", {"setting": setting})


def site_footer_partial(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_box = FooterLinkBox.objects.all()
    for item in footer_link_box:
        item.footerlink_set.all()
    return render(
        request,
        "shared/site_footer_partial.html",
        {"setting": setting, "footer_link_box": footer_link_box},
    )


class AboutView(TemplateView):
    template_name = "about_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(
            is_main_setting=True
        ).first()
        context["site_setting"] = site_setting
        return context
