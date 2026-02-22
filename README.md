# MOSFET_NonIdeal_IdVgs_Analysis
Analysis of non-ideal MOSFET Id–Vgs characteristics (Subthreshold Conduction) 

## Background
이전 프로젝트에서는 이상적인 MOSFET 모델을 가정하여  
Id–Vgs 특성과 transconductance(gm)를 분석하였다.
하지만 실제 MOSFET에서는 문턱 전압(Vth) 이하에서도  
전류가 완전히 0이 되지 않는 비이상적인 특성이 나타난다.

본 프로젝트에서는 이러한 비이상성 중  
**Subthreshold Conduction** 현상에 집중하여 분석한다.

## Question
- 왜 Vgs가 문턱 전압 이하인데도 Id가 흐르는가?
- Subthreshold 영역에서 Id는 Vgs에 대해 어떤 형태로 증가하는가?
- 이러한 특성은 gm에 어떤 영향을 미치는가?

## Plan
- Subthreshold 영역의 MOSFET 전류 모델 적용
- Id–Vgs 관계를 로그로 시각화
- 이상적인 MOSFET 특성과 비교
- Subthreshold 영역에서 gm 변화 관찰 및 해석

## Result:Subthreshold Id–Vgs (Log Scale)  
 ![Subthreshold Id–Vgs (Log Scale)](results/Subthreshold%20Id–Vgs%20(Log%20Scale).png)

## Observation
- Vgs가 문턱 전압(Vth) 이하에서 Id는 0이 아니다.
- Id는 매우 작은 값에서 시작하여 Vgs가 증가할수록 빠르게 증가한다.
- 로그 스케일에서 Id–Vgs 관계는 거의 직선 형태를 보인다.

## Interpretation
- Subthreshold 영역은 Vgs가 문턱 전압(Vth)보다 낮은 구간이다.
  이 구간에서 전류는 0이 아니라 매우 작은 값을 가진다.

- 로그 스케일에서 Id–Vgs 그래프가 거의 직선 형태를 보이는 것으로부터
  지수적으로 증가함을 확인 할 수 있다.

- 이러한 지수 증가 특성은 Subthreshold 영역에서 확산(diffusion) 메커니즘에 의해
  전류가 발생한다는 이론과 일치하는 경향을 보인다.
