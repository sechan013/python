#신호가 끊겼을때

import math
import matplotlib.pyplot as plt
import numpy as np
import time



def FFT_merge(even, odd):
    N = len(even) * 2
    #FFT는 항상 2의 거듭제곱으로 쪼개짐
    #정렬과 다르게 미리 N칸짜리 배열을 만들어둠
    result = [0.0] * N
    for k in range(N //2): #대칭성을 이용 절반만 돌아도 OK
        #k는 찾고싶은 주파수의 번호
        #k가 증가함에 따라 시간신호 길이의 1/k주기를 가짐
        #나이퀴스트 주파수까지 늘어나고 줄어들며 대칭성을 가짐

        #회전인자
        #정렬에서의 크기비교와 대응되는 값이며,
        #현재 인덱스 k에 해당하는 회전각도를 만든다
        theta = -2 * math.pi * k / N
        twiddle = complex(math.cos(theta), math.sin(theta))
        #내장함수 오일러공식

        T = twiddle * odd[k] #홀수배열값에 회전값 곱해주기

        result[k] = even[k] + T
        #앞부분 절반 주파수성분 결정

        result[k + (N // 2)] = even[k] - T
        #뒷부분 절반 주파수 성분 결정 (대칭성 이용)

    return result

def my_FFT(x):
    if len(x) <= 1: #분할 종료조건(정렬과 동일)
        return x

    even = my_FFT(x[0::2]) #0부터 2칸식 건너뜀 (짝수 인덱스)
    odd = my_FFT(x[1::2]) #(홀수 인덱스)

    return FFT_merge(even, odd)

#시물레이션 데이터 생성
N = 1024 #2의 거듭제곱 형태
fs = 1000  # 샘플링 주파수(1초에 1000번)
t = np.linspace(0, (N-1)/fs, N) #0~1초 시간축 생성
#linspace 일정한 간격으로 나누는 함수

sig50 = np.sin(2 * np.pi * 50 * t)
sig120 = 0.5 * np.sin(2 * np.pi * 120 * t)
x = sig50 + sig120
# 50Hz와 120Hz의 신호를 생성 ( 120Hz는 크기가 절반)

x_cut = np.zeros(N) # 신호가 중간에 끊긴 상황을 시뮬레이션 하기 위해 0으로 채워진 배열 생성
x_cut[:64] = x[:64] # 앞부분 64개 샘플에만 신호를 넣고 나머지는 0으로 둠

start = time.time()
my_result = np.array(my_FFT(list(x)))  #FFT호출
res_cut = np.array(my_FFT(list(x_cut))) # 끊긴 신호에 대해서도 FFT 수행
my_time = time.time() - start


#시각적 구현
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1) # 2행 1열 1번째 (두개를 비교하기위해)
plt.plot(t[:200], x[:200], color='blue', label='Full')
plt.plot(t[:200], x_cut[:200], color='red', label='Cut-off') # 중간에 끊긴 신호를 빨간색으로 추가
#너무 촘촘하지 않게
plt.title("Mixed Signal (50Hz + 120Hz)")
plt.xlabel("Time")                       #x축 시간
plt.ylabel("Amplitude")                  #y축 진폭
plt.legend()                             # 두 신호를 구분하기 위한 범례 추가
plt.grid(True)                           #그리드 표시

#FFT변환
freqs = np.fft.fftfreq(N, 1/fs) #주파수 눈금계산
plt.subplot(2, 1, 2)
signal = np.abs(my_result) #절댓값으로 크기만 비교
plt.plot(freqs[:N//2], signal[:N//2], color='red', label='Full')
plt.plot(freqs[:N//2], np.abs(res_cut)[:N//2], color='blue', label='Cut-off') # 끊긴 신호의 주파수 결과를 파란색으로 추가

plt.title("FFT Result (Peaks)")
plt.xlabel("Frequency [Hz]")             #x축 주파수
plt.ylabel("Magnitude")                  #y축 크기
plt.xlim(0, 200)                         # 피크 높이와 뭉툭함을 잘 비교하기 위해 x축 범위 제한
plt.legend()                             # 두 신호를 구분하기 위한 범례 추가
plt.grid(True)                           #그리드 표시

plt.tight_layout()
plt.show()