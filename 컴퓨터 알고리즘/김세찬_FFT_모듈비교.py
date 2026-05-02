import math
import matplotlib.pyplot as plt
import numpy as np
import time


# [1] 직접 구현한 FFT 함수
def FFT_merge(even, odd):
    N = len(even) * 2
    result = [0.0] * N
    for k in range(N // 2):
        # 나이퀴스트 주파수 지점까지 회전 인자 적용
        theta = -2 * math.pi * k / N
        twiddle = complex(math.cos(theta), math.sin(theta))
        T = twiddle * odd[k]

        # 버터플라이 연산: 대칭성을 이용해 앞뒤를 동시에 채움
        result[k] = even[k] + T
        result[k + (N // 2)] = even[k] - T
    return result


def my_FFT(x):
    if len(x) <= 1:
        return x
    even = my_FFT(x[0::2])
    odd = my_FFT(x[1::2])
    return FFT_merge(even, odd)


# [2] 시뮬레이션 데이터 생성 (나이퀴스트 정리 준수)
N = 32768
fs = 1000  # 샘플링 주파수 (최대 주파수 120Hz의 2배 이상 확보)
t = np.linspace(0, (N - 1) / fs, N)

# 50Hz와 120Hz 신호 합성
x = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# [알고리즘 측정 및 모듈 비교]
# 1. 직접 구현한 my_FFT 시간 측정
start = time.time()
my_result = np.array(my_FFT(list(x)))
my_time = time.time() - start

# 2. Numpy 표준 모듈 fft 시간 측정
start = time.time()
np_result = np.fft.fft(x)
np_time = time.time() - start

# 3. 결과 출력
print("-" * 30)
print(f"직접 구현 FFT 시간: {my_time:.6f}초")
print(f"Numpy 모듈 FFT 시간: {np_time:.6f}초")
print(f"속도 차이: 약 {my_time / np_time:.1f}배 차이")
print("-" * 30)

# 시각화는 기존처럼 정확도 비교로 유지 (두 선이 겹쳐 보이는 것 확인)
# [4] 정확도 및 시각적 구현
max_error = np.max(np.abs(my_result - np_result))
freqs = np.fft.fftfreq(N, 1 / fs)

print(f"직접 구현 시간: {my_time:.5f}s / 모듈 시간: {np_time:.5f}s")
print(f"최대 오차: {max_error:.2e}")

plt.figure(figsize=(10, 8))

# 시간 영역 그래프
plt.subplot(2, 1, 1)
plt.plot(t[:200], x[:200], color='blue')
plt.title("Mixed Signal (50Hz + 120Hz)")
plt.grid(True)

# 주파수 영역 그래프 (비교)
plt.subplot(2, 1, 2)
plt.plot(freqs[:N // 2], np.abs(my_result)[:N // 2], color='blue', label='My FFT')
plt.plot(freqs[:N // 2], np.abs(np_result)[:N // 2], color='red', linestyle='--', label='Numpy FFT')
plt.title(f"FFT Comparison (Max Error: {max_error:.2e})")
plt.xlabel("Frequency [Hz]")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()