def compression(s, l):
    now = s[:l]
    count = 1
    idx = l
    compressed = ''
    while idx + l <= len(s):
        next = s[idx:idx+l]
        if next == now:
            count += 1
        else:
            if count > 1:
                compressed += str(count)
            compressed += now
            now = next
            count = 1
        idx += l
    
    if count > 1:
        compressed += str(count)
    compressed += now
    
    if idx < len(s):
        compressed += s[idx:]
    
    return compressed

def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        answer = min(answer, len(compression(s, i)))
    
    return answer