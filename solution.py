import pandas as pd
import numpy as np
from statsmodels. stats.proportion import proportions_ztest

chat_id = 1412519104

def solution(x_success, 
             x_cnt, 
             y_success, 
             y_cnt) -> bool:
  return (proportions_ztest([x_success, y_success], [x_cnt, y_cnt])[0] >= 0 or 
          proportions_ztest([x_success, y_success], [x_cnt, y_cnt])[1] < 0.9)
