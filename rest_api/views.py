from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import json
import math

@api_view(['POST'])
@permission_classes((AllowAny,))
def consumption(request):
    response = []
    for airplane_data in  request.data["data"]:
        if (airplane_data.get('id', None) or airplane_data.get("passenger", None)):
            airplane_id = int(airplane_data["id"])
            passenger_cnt = int(airplane_data["passenger"])
            total_fuel = airplane_id * 200
            consumption_per_min = passenger_cnt * 0.002 + math.log(0.80 * airplane_id)
            max_fly_min = total_fuel / consumption_per_min
            response.append({"id": airplane_id, "consumption_per_min": '{:.3f}'.format(consumption_per_min), "max_fly_min": '{:.3f}'.format(max_fly_min)})
        else:
            print("Invalid Json Data")
    return Response(response)