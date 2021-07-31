def match_stage_5(regex, text):
    print(f"5:  '{regex}'  '{text}'")
    if regex[1] == '?':
        return True if match_stage_2(regex[0] + regex[2:], text) or \
                       match_stage_2(regex[2:], text) else False
    elif regex[1] == '+':
        return True if match_stage_2(regex[0] + regex[2:], text) or \
                       match_stage_5(regex[0] + '?' + regex[2:], text[1:]) else False
    elif regex[1] == '*':
        return True if match_stage_2(regex[2:], text) or \
                       match_stage_5(regex[0] + '+' + regex[2:], text[1:]) else False
    return match_stage_2(regex[2:], text)

#  stage 2/6 (recursive)
def match_stage_2(regex, text):
    print(f"2:  '{regex}'  '{text}'")
    if not regex:
        return True
    if regex == '$':
        return True if not text else False
    if regex[1:] and regex[1] in '?+*':
        return match_stage_5(regex, text)
    return match_stage_2(regex[1:], text[1:]) if text and regex[0] in ['.', text[0]] else False


    #  stage 3/6 (iterative)
def match_stage_3(regex, text):
    print(f"3:  '{regex}'  '{text}'")
    for start in range(len(text)):
        if match_stage_2(regex, text[start:]):
            return True
    return False


#  stage 4/6 (add '^', '$')
def match_stage_4(regex, text):
    print(f"4:  '{regex}'  '{text}'")
    if not regex:
        return True
    if regex[0] == '^':
        return match_stage_2(regex[1:], text)
    return match_stage_3(regex, text)


#print(match_stage_4(*input().split('|')))
