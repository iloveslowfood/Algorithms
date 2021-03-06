"""https://programmers.co.kr/learn/courses/30/lessons/60058
균형잡힌 괄호 문자열: 좌/우 괄호 수가 같은 경우 <- (()))(
올바른 괄호 문자열: 좌/우 괄호 수가 같은 경우 & 짝이 다 맞을 경우 <- (())()

1. 입력 길이 0 => 그대로 반환
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리 / 갯수 맞게 나눠라 이말이여
    *u는 "균형잡힌 괄호 문자열"로 더 분리할 수 없음 & v는 빈 문자열이 될 수 있음
3. 문자열 u가 "올바른 괄호 문자열" -> 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
"""
