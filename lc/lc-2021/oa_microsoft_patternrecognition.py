def get_count(pattern, source):
    pattern_len = len(pattern)
    start = 0
    end = pattern_len
    count = 0

    while start <= len(source)-pattern_len:
        cut = source[start:end]
        # print(len(source), start, cut, pattern)
        if cut==pattern:
            count += 1
        start += 1
        end += 1
    return count


def patternrecognition(input):
    # exception
    if input==None:
        return None
    # separate pattern and reference
    pattern, blobs = input.split(';')
    if blobs=='': # empty pattern
        return 0
    elif pattern=='':
        count_pipe=0
        for s in input:
            if s=='|':
                count_pipe+=1
        return '|'.join(['0']*(count_pipe+2))

    else:
        counts = [
            get_count(pattern,blob)
            for blob in blobs.split('|')
        ]
        return '{partial}|{total}'.format(
            partial = '|'.join([str(c) for c in counts]),
            total = sum(counts)
        )

if __name__ == '__main__':
    testcases = [
        "bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32",
        "aa;aaaakjlhaa|aaadsaaa|easaaad|sa",
        "b;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32",
        ";bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32"
    ]

    answers = [
        "3|2|1|2|8",
        "4|4|2|0|10",
        "4|2|3|2|11",
        "0|0|0|0|0"
    ]

    res1 = patternrecognition(testcases[0])
    print(res1, answers[0])

    res2 = patternrecognition(testcases[1])
    print(res2, answers[1])

    res3 = patternrecognition(testcases[2])
    print(res3, answers[2])

    res4 = patternrecognition(testcases[3])
    print(res4, answers[3])
