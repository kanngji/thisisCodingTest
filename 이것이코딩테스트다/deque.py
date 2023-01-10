# deque 이란?
# deque 이란 collections 모듈에 속해있으며
# 단방향 흐름이던 기존 Queue 자료구조와 달리 
# 앞과 뒤(왼쪽, 오른쪽) 양방향에서 삽입 삭제를 할 수 있는 자료
# 구조입니다.

# deque 사용법
# 1. collection 모듈 및 deque import
# 2. deque 생성

from collections import deque

dq=deque()

# append() : deque 뒤(오른쪽)에 값 추가
# appendleft() : deque 앞(왼쪽)에 값 추가
# remove(): deque 안의 특정 값 삭제
# pop() : deque뒤(오른쪽)의 값 삭제 후 반환
# popleft(): deque앞 (왼쪽)의 값 삭제 후 반환

