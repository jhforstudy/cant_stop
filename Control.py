from Platform import Platform
from Platform import SerialPacket
from Flag import Flag

import time
import math

import serial
import sys
import os
sys.path.append(os.path.dirname(__file__))

class Control():
    def __init__(self):
        # 제어 알고리즘에 필요한 값을 받아옵니다.
        # 아직 생성자는 안 썼습니다.
        '''
        # PID control
        # 일단 PD제어 기반으로 하고 I제어는 실험 후 추가할 예정.
        # P제어는 각도 오차에 비례하는 값을, D제어는 현재 오차 각도와 이전 오차 각도의 차이값을 이용합니다.
        # I제어는 추후 할 예정입니다.
        #--------------------------------------------------------------------
        # angleError_sum = 0 #PID 제어를 위해 지금까지의 각도 오차 합 저장이 필요.
        angleError_prev = 0 #PID 제어를 위해 이전 각도 오차 저장이 필요.
        #--------------------------------------------------------------------
        '''
        
    def main():
        # path tracking
        # 현재 차의 위치, 타겟 위치, 방향, 이전 차의 위치를 받아옵니다.
        Car_Angle, P_curr, P_targ, P_prev
        angleError_curr = findangleError(Car_Angle, P_curr, P_targ, P_prev) # 각도 오차

        # PID control으로 최종 조향각을 구합니다.
        steer_final = calculatePID(angleError_curr, angleError_prev''', angleError_sum''')

        # 이 값을 통신부로 보내주기 (-2000~2000 으로 변환)
        
        # 보내준 이후, 각도 오차와 '''각도 오차의 합'''을 저장.
        angleError_prev = angleError_curr
        # angleError_sum += angleError_curr
        
    def normalize(vector_x, vector_y):
        norm = ((vector_x * vector_x) + (vector_y * vector_y))**(0.5)
        return (vector_x/norm), (vector_y/norm)
    
    def findangleError(car_angle, position_curr, position_targ, position_prev): # 현재 차의 위치, 타겟 위치, 이전 차의 위
        
        TargetDir = position_targ - position_curr # 타겟 방향 = 타겟 위치 - 현재 위치

        UTargetDir = normalize(TargetDir) # 타겟 방향의 단위벡터
        Unitvec = (1, 0) # 단위 방향벡터

        target_angle = acos((UTargetDir*Unitvec)) # 0도~ 360도 사이의 값을 얻게 됨. (West = 0도)

        # N=0으로 변환해야 함.
        
        angle_error = car_angle - target_angle
        if (angle_error >= 180): angle_error -= 360
        if (angle_error <= -180): angle_error += 360
        # -180도 ~ 180도 사이의 angle_error를 얻게 됨.  

        return angle_error
    
    def calculatePID(current_angleError, prev_angleError, angleError_sum):
        # 결정해야 함
        K_p =
        # K_i =
        K_d =
        dt = current_time - prev_time    # 시간 값을 가져와야 함

        angleError = current_angleError
        # angleError_sum += angleError * dt
        
        # p control
        proportional = K_p*angleError
        # d control
        derivative = K_d*((angleError - past_angleError)/dt)
        # i control
        # integral = K_i*(angleError_sum)

        steerangle = proportional + derivative # + integral
        return steerangle
        
if __name__ == '__main__':
    Control.main()
