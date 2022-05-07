import profile
from login_predict import login_predict
from fastapi import APIRouter
from .monitor.timer import CustomMetrics

router = APIRouter()
custom_metrics = CustomMetrics("predict_service")
login = login_predict.LoginPredict()


# @profile
@router.get(path='/predict/x1/{x1}/x2/{x2}/x3/{x3}/x4/{x4}/is_verified_login/{is_verified_login}')
def predict(x1: float, x2: float, x3: float, x4: float, is_verified_login: bool):
    try:
        with custom_metrics.model_latency_histogram.time():
            return login.predict(x1, x2, x3, x4, is_verified_login)
    except Exception as err:
        print(err)
        return f"error: {str(err)}"
