# SchoolInfoBringer

한국 학교의 이름으로 학교코드,학교종류,지역을 받아오세요

오픈소스초보자라서 그리고One-Day프로젝트라서
상당히 코드가 난해할수도있습니다.

뭐 그래도 [아희](https://aheui.github.io/)  보다야....



## 1. 쓰는법

### 1.1. 불러오기

```python
from SchoolInfoBringer import SchoolInfoBringer
```

### 1.2. 데이터 받아오기

```python
c=SchoolInfoBringer()
c.getSchoolInfo("학교이름 적절히")#EX)파썬중, 씨샵고등학교
```

~~에? 그래서 정보는?~~

### 1.3. 데이터 사용하기

```python
c.result#배열입니다 키워드가 정확하면 1개내외지만 아니면 가능한 모든학교가 나옵니다
sel=c.result[0]
sel.schoolname#학교이름(str)
sel.schoolcode#학교코드(str)
sel.schoolarea#학교구역(int)
sel.schooltype#학교종류(int)
```



## 2. 학교구역? 학교종류?

어.... 사실저도 잘몰릅니다

그래도 아는거만 말을해본다면

### 2.1. 학교구역

1. 서울
2. 부산
3. 대구
4. 인천
5. 광주
6. 대전
7. 울산
8. 세종
9. 없음 ~~왜없어요?아시는분?~~
10. 경기
11. 강원
12. 충북
13. 충남
14. 전북
15. 전남
16. 경북
17. 경남
18. 제주

## 2.2. 학교종류

1. 유치원
2. 초등학교
3. 중학교
4. 고등학교



## 3.그래서 어따쓰는데?

글세요 [샘플](https://github.com/Party4Bread/SchoolInfoBringer/blob/master/source/schoolcodesample.py) 넣어놨으니 암 봐보세요

