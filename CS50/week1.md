## C언어로 Hello World를 출력하는 과정
```#include<stdio.h>
int main(void)
{
  printf("Hello World!\n");
}```
prompt 창에 다음과 같이 입력하여 Hello World! 출력
```clang -o hello hello.c # hello 이름의 machine code 생성
./hello # machine code 실행```

## Compile
- 컴퓨터는 0 or 1을 인식하므로 우리가 입력한 코드를 컴퓨터가 이해할 수 있도록 바꿔주는 작업이 필요   
**source code -> compiler -> machine code**

## Terminal 명령어
- mkdir : make directory
- rmdir : remove directory
- ls : list
- rm : remove
- cd : change directory

## C언어 코딩 문법
- #include<헤더파일> : 컴파일러의 라이브러리 폴더에서 헤더파일을 찾는다. python의 import와 유사
- 프로그래밍에서의 = 기호는 오른쪽에서 왼쪽으로 assign 한다는 의미이다.
- 문자를 입력할 때 double quotation 사용
- C언어에서 동적 데이터 입력을 위해 placeholder 사용 (%s)

## if문 사용

```#include<stdio.h>
if (x < y)
{
  printf("x is less than y\n");
}
  else if (x > y)
{
  printf("x is greater than y\n");
}
  else
{
  printf("x is equal to y\n");
}```

## while문 사용

```#include<stdio.h>
int i = 0;
while (i < 50)
{
  printf("Hello World!\n");
  i++;
}```

## for문 사용

```#include<stdio.h>
for (int i = 0; i < 50; i++)
{
  printf("Hello World!\n");
}```

i = 0 -> i < 50 -> printf -> i++ 순서로 반복
## 변수 타입(placeholder)
- bool : True/False
- char(%c) : 2byte(16bits), 16진수로 0000~ffff 까지 문자를 표현
- int(%i) : 32bits 정수
- long(%li) : 64bits 정수
- float(%f) : 32bits 실수 / %.2f 와 같은 방식으로 소수점 지정
- double(%f) : 64bits 실수
- string(%s) : 문자열

## Example

```#include<stdio.h>
int main(void)
{
int n = get_int("n: ");
if (n %2 ==0)
{
  printf("even"\n);
}
else
{
  printf("odd\n");
}
}```

입력받은 n 값이 짝수이면 even, 홀수이면 odd 출력

```#include<stdio.h>
void hello(void);
int main(void)
{
for (int i = 0; i < 3; i++)
{
  hello();
}
}
void hello(void)
{
  printf("hello\n");
}```

hello 함수를 정의하고 반복문에서 사용  
정의된 함수가 main 뒤에 있을 경우 앞에 정의해줘야함  
void hello(void) 에서 앞의 void는 리턴타입을 나타내며 뒤의 void는 input값을 나타낸다.

```#include<stdio.h>
void hello(int n);
int main(void)
{
  hello(3);
}
void hello(int n)
{
for (i = 0; i < n; i++)
{
  print("hello\n");
}
}```

hello함수의 리턴값을 int로 변경
## Overflow

```#include<stdio.h>
int main(void)
{
  float x = get_float("x: ");
  float y = get_float("y: ");
  printf("x / y : %.50f\n", x / y);
}```
x에 1, y에 10을 넣을 경우 0.10000000149011... 과 같은 값이 나온다.