a = {
    'x1': 123,
    'x2': 'abc',
    'x3': {
        'x31': 11,
        'x32': 'qwer',
    },
    'x4': [1, 2, 3],
    'x5': [
        {
            'x51': 123,
            'x52': {
                'bb': 'bb'
            }
        }
    ]
}

b = {
    'x3': {
        'x31': 11,
        'x32': 'qwer',
    },
    'x4': [1, 2, 3],
    'x5': [
        {
            'x51': 123,
            'x52': {
                'bb': 'bb'
            }
        }
    ],
    'x1': 123,
    'x2': 'abc',
}

c = {
    'x1': 123,
    'x2': 'abc',
    'x3': {
        'x31': 11,
        'x32': 'qwer',
    },
    'x4': [1, 2, 3, 4],
    'x5': [
        {
            'x51': 123,
            'x52': {
                'bb': 'bb'
            }
        }
    ]
}

d = {
    'x1': 123,
    'x2': 'abc',
    'x3': {
        'x31': 11,
        'x32': 'qwer',
    },
    'x4': [1, 2, 3],
    'x5': [
        {
            'x51': 123,
            'x52': {
                'bb': 'aa'
            }
        }
    ]
}



if a == b:
    print('Yes. a == b')
else:
    print('No. a != b')

if a == c:
    print('Yes. a == c')
else:
    print('No. a != c')

if a == d:
    print('Yes. a == d')
else:
    print('No. a != d')
