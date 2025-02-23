from fastapi import APIRouter
from Domain.balloonData import balloon

router = APIRouter(prefix="/droneServer")

@router.get("/")
def serve(lat, lon, alt):
    test = balloon(lat, lon, alt)
    print(test)
    return f"latitude: {test.lat}, longitude: {test.lon}, altitude: {test.alt}"