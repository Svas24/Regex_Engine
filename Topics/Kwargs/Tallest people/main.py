def tallest_people(**kw):
    print('\n'.join(sorted([f'{n} : {h}' for n, h in kw.items() if h == max(kw.values())])))
