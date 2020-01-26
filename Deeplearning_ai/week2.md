## Binary Classification
![Binary Classification](./img/week2_01.PNG)  
- 64x64 사이즈의 이미지가 주어졌을 때, RGB로 이루어진 3개의 64x64 행렬로 표현 가능하다.
- input X벡터는 [255,231,...,255,134,...]의 Transpose 형태로 64x64x3개의 원소를 갖는다.
- input값을 통해 y=1 or y=0을 예측하는 것이 이진 분류 방식이다.
## Notation
![Notation](./img/week2_02.PNG)  
- 학습 데이터의 쌍을 (x,y)라 하며 x는 n_x차원을 갖고 y는 0또는 1값을 갖는다.
- m은 학습 데이터의 개수이며 위첨자 (m)은 m번째 데이터라는 의미이다.
- X는 학습 데이터 input값을 모두 담은 행렬이다. 가로로 쌓는 것이 학습시키기에 유리하다.
- Y는 학습 데이터 output값을 모두 담은 행렬이다. 0 또는 1 값을 갖는다.
## Logistic Regression
![Logistic Regression](./img/week2_03.PNG)  
- x값이 주어졌을 때, y=1일 확률을 계산하는 과정이 필요하며 이 값을 y^ 이라 한다.
- y^을 1차 선형 식으로 `wx+b`와 같이 표현할 수 있고 이 값을 0~1사이로 만들기 위해 활성화함수를 사용한다. 위의 예시는 Sigmoid함수를 적용한 것이다.
- parameter인 w와 b는 나누어 표현하는 것이 좋다. 오른쪽의 표현방법은 w와 b를 한 개의 벡터로 나타낸 것이며 사용하지 않는다.
## Cost Function
![Cost Function](./img/week2_04.PNG)  
- Loss function을 정의할 때, $$$frac { 1 }{ 2 } { (\hat { y } -y) }^{ 2 }$$$ 으로 한다면 경사하강법 실행 시 local minimun에 빠지기 쉽다.
- 따라서 Loss function은 $$$\L (\hat { y } ,y)\quad =\quad -(y\log { \hat { y }  } +(1-y)\log { (1-\hat { y } )) }$$$ 으로 정의한다.
- 손실함수를 작게 만드는 것이 목표이므로, y=1인 경우 y hat값은 커져야 하고 y=0인 경우 y hat값은 작아져야 한다.
- Cost function은 각 학습 데이터의 Loss function을 더한 값이며 `J(w,b)` 로 나타낸다.