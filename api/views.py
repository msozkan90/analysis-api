from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.service import AnalysisService

service = AnalysisService()

@api_view(['GET'])
def conversion_rate(request):
    return Response(service.conversion_rate_calculation())

@api_view(['GET'])
def status_distribution(request):
    return Response(service.status_based_analysis())

@api_view(['GET'])
def category_type_performance(request):
    return Response(service.category_type_analysis())

@api_view(['GET'])
def filtered_aggregation(request):
    return Response(service.filter_and_aggregate())
