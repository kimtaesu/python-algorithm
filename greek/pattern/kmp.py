# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    """
       패턴 검색은 컴퓨터 과학에서 중요한 문제입니다.
       메모장 / 단어 파일이나 브라우저 또는 데이터베이스에서 문자열을 검색 할 때 패턴 검색 알고리즘이 검색 결과를 표시하는 데 사용됩니다.
       Naive 알고리즘의 최악의 경우의 복잡도는 O (m (n-m + 1))입니다. KMP 알고리즘의 시간 복잡도는 최악의 경우 O (n)이다.

       Preprocessing Overview:

       KMP 알고리즘은 pat []를 사전 처리하고 일치하는 동안 문자를 건너 뛰는 데 사용되는 크기 m (패턴 크기와 동일)의 보조 lps []를 구성합니다.

       이름 lps는 접미사 인 가장 긴 적절한 접두어를 나타냅니다. 적절한 접두사는 접두사이며 전체 문자열은 허용되지 않습니다.
       예를 들어, 'ABC'의 접두사는 '', 'A', 'AB'및 'ABC'입니다. 적절한 접두사는 '', 'A'및 'AB'입니다. 문자열의 접미사는 '', 'C', 'BC'및 'ABC'입니다.

       하위 패턴에서 lps를 검색합니다. 더 명확하게 우리는 접미사와 접미사 중 하나 인 패턴의 하위 문자열에 중점을 둡니다

       i = 0에서 m-1까지의 각 하위 패턴 pat [0..i]에 대해 lps [i]는 하위 패턴 pat [0..i]의 접미사이기도 한 최대 일치 고유 접두사의 길이를 저장합니다. .

          lps[i] = the longest proper prefix of pat[0..i]
                 which is also a suffix of pat[0..i].
       """
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * M
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    print("lps: {}".format(lps))
    print("end lps")
    print()
    while i < N:
        print("pat[j]: {} == {}: txt[i]".format(pat[j], txt[i]))
        print("j: {} == {}: i".format(j, i))
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]

            # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
                print("reset j: {}".format(j))
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        print("lps: {}".format(lps))
        print("before i: {} {}: len  pat[i] : {} == {} : pat[len]".format(i, len, pat[i], pat[len]))
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
        print("after i: {} len: {}".format(i, len))


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)

