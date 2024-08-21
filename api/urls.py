from api.views import (
    conversion_rate,
    status_distribution,
    category_type_performance,
    filtered_aggregation
)
from django.urls import path

urlpatterns = [
    path('conversion-rate/', conversion_rate, name='conversion_rate'),
    path('status-distribution/', status_distribution, name='status_distribution'),
    path('category-type-performance/', category_type_performance,
         name='category_type_performance'),
    path('filtered-aggregation/', filtered_aggregation,
         name='filtered_aggregation'),
]
