import profile
from fastapi import APIRouter
from .monitor.timer import CustomMetrics
import math
import asyncio
router = APIRouter()
custom_metrics = CustomMetrics("predict_service")


#@profile
@router.get(path='/predict/x1/{x1}/x2/{x2}/x3/{x3}/x4/{x4}/is_verified_login/{is_verified_login}')
def predict(x1: float, x2: float, x3: float, x4: float, is_verified_login: bool):
    with custom_metrics.model_latency_histogram.time():
        return asyncio.run(calc_fraud_score(x1, x2, x3, x4, is_verified_login))


async def calc_fraud_score(x_1, x_2, x_3, x_4, is_verified_login):
    bias = 0.623
    w_1 = 2.734
    w_2 = 0.263
    w_3 = -4.342
    w_4 = 0.234

    Z = bias + x_1 * w_1 + x_2 * w_2 + x_3 * w_3 + x_4 * w_4

    fraud_score = 1.0 / (1.0 + math.exp(-Z))

    if (is_verified_login):
        return 0.0
    else:
        return fraud_score