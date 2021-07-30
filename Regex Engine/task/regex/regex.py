def match_rec(regex, text):
    if not regex:
        return True
    if regex == '$':
        return True if not text else False
    if len(regex) > 1:
        if regex[0] == '\\':
            if regex[1] in '\\S.':
                return match_rec(regex[2:], text[1:]) if text and regex[1] == text[0] else False
            return match_rec(regex[1:], text)  # \_
        else:
            if regex[1] == '?':
                return match_rec(regex[2:], text) or match_rec(regex[0] + regex[2:], text)
            if regex[1] == '+':
                return match_rec(regex[0] + regex[2:], text) or match_ite(regex[0] + '?' + regex[2:], text[1:])
            if regex[1] == '*':
                return match_rec(regex[2:], text) or match_ite(regex[0] + '+' + regex[2:], text)
    return match_rec(regex[1:], text[1:]) if text and regex[0] in [text[0], '.'] else False


def match_ite(regex, text):
    for start in range(len(text)):
        if match_rec(regex, text[start:]):
            return True
    return False


def match_bounds(regex, text):  # stage 4
    if not regex:
        return True
    if regex[0] == '^':
        return match_rec(regex[1:], text)
    return match_ite(regex, text)


if __name__ == "__main__":
    print(match_bounds(*input().split('|')))
