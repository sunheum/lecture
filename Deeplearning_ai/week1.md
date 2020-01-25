## What is a Neural Network?
![집값에 따른 가격 예측](./Dimg/week1_01.png)
x값(집의 크기)를 input으로 넣으면 y값(가격)이 output으로 나오는 형태  
활성화함수로 ReLU(Rectified Linear Unit)을 많이 사용한다.
![집값을 결정하는 요소 계산 예시](./Dimg/week1_02.png)
위의 예시를 신경망으로 나타내면 아래와 같다.
![집값 결정 신경망 표현](./Dimg/week1_03.png)
input으로 집의 크기, 방의 수, 주소, 부유한 정도 가 들어가면 hidden layer를 거쳐 output으로 집값이 나오게 된다.  
hidden layer의 첫번째 노드(family size)에 x1~x4가 모두 연결되어 있는데, 학습하는 과정에서 가중치가 부여되기 때문에 우리가 x1,x2와만 관련있을 것으로 예측했어도 무관하다.
## Supervised Learning with Neural Network
![Supervised Learning 예시](./Dimg/week1_04.png)
시퀀스 데이터는 RNN을 가장 많이 사용한다.  
오디오는 시간에 따라 재생되고 언어는 단어들이 나열되는 특성이 있어 시퀀스에 의해 가장 자연스럽게 표현된다.
![Neural Network 예시](./Dimg/week1_05.png)
RNN은 시간적은 요소를 담고있는 일차원적인 데이터를 다루는데 좋다.
![데이터 구조](./Dimg/week1_06.png)
지금까지 경체적 가치를 이끌어 온 신경망 분야는 structured data에 관한 부분이었다.
## Why is Deep Learning taking off?
![딥러닝 과정의 변화_1](./Dimg/week1_07.png)
위 그래프와 같이 매우 큰 신경망을 학습시키는 경우 성능이 향상될 수 있다.  
고성능의 프로그램을 위해서는 큰 신경망을 트레이닝 할 수 있어야 하고, 그만큼 방대한 양의 데이터가 있어야 한다.
![딥러닝 과정의 변화_2](./Dimg/week1_08.png)
알고리즘 부분의 혁신으로 활성화함수의 변화(Sigmoid -> ReLU)가 있다.  
이를 통해 계산속도의 증가, 빠른 결과 확인으로 새로운 아이디어 도출이 가능해지며 사이클의 순환 속도가 증가하였다.