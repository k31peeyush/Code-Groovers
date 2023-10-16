from rest_framework.response import Response
from rest_framework.views import APIView
from .models import H1BData
from rest_framework.decorators import api_view
from django.db import connection


@api_view(['GET'])
def get(request):
    count = H1BData.objects.count()
    return Response({'response':count})


@api_view(['GET'])
def mean(request):
    with connection.cursor() as cursor:
        # Replace 'column_name' with the actual column name
        cursor.execute(
            "SELECT AVG(wage_rate_of_pay * wage_unit_of_pay) FROM app_h1bdata")
        # Extract the average value from the query result
        average_value = cursor.fetchone()[0]
    return Response({'response':average_value})


@api_view(['GET'])
def median(request):
    with connection.cursor() as cursor:
        cursor.execute("""
SELECT
    percentile_cont(0.5) WITHIN GROUP (ORDER BY wage_rate_of_pay * wage_unit_of_pay) AS median
FROM
    app_h1bdata;
""")
        median_value = cursor.fetchone()[0]
    return Response({'response':median_value})

@api_view(['GET'])
def get_percentile(request):
    percentile = request.GET.get('val', None)
    if percentile is None:
        return Response({'error': 'Please provide a percentile value using the \'val\' query parameter'})
    percentile = float(percentile)
    with connection.cursor() as cursor:
        cursor.execute("""
SELECT
    percentile_cont(%s) WITHIN GROUP (ORDER BY wage_rate_of_pay * wage_unit_of_pay) AS percentile
FROM
    app_h1bdata;
""", [percentile])
        percentile_value = cursor.fetchone()[0]
    return Response({'response':percentile_value})