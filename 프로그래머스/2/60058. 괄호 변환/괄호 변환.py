def check(u):
    stack = []
    for par in u:
        if par == '(':
            stack.append(par)
        else:
            if not stack:
                return False
            stack.pop(-1)
    return True

def solution(p):
    if p == '':
        return ''
    
    u = ''
    count = 0
    for i in range(len(p)):
        u += p[i]
        if p[i] == ')':
            count -= 1
        else:
            count += 1
        if count == 0:
            break
    
    v = p[i+1:]

    if check(u):
        return u + solution(v)
    
    answer = '('
    answer += solution(v)
    answer += ')'
    for par in u[1:-1]:
        if par == '(':
            answer += ')'
        else:
            answer += '('
    
    return answer