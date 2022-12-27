def find(arr):
    max_count = [0] * len(arr)
    word_index = 0
    for v in arr:
        a = list(v)
        a.sort()
        r = dict()
        for c in a:
            if c not in r:
                r.update({c: 0})
            r[c] += 1

        temp = 0
        for values in r.values():
            if values > temp:
                temp = values
        max_count[word_index] = temp
        word_index += 1

    final_max = 0
    index = 0
    for i in range(1, len(max_count)):
        if max_count[i] > final_max:
            final_max = max_count[i]
            index = i

    return arr[index]


def find2(arr) -> str:
    final_max_len = 0
    final_max_index = -1
    for i, a in enumerate(arr):
        chars = [0] * 128
        max_len = 0
        for c in a:
            chars[ord(c)] += 1
            if chars[ord(c)] > max_len:
                max_len = chars[ord(c)]
            if max_len > final_max_len:
                final_max_len = max_len
                final_max_index = i

    return arr[final_max_index]


if __name__ == "__main__":
    print(find(["abbc", "bbabc", "abcderf"]))
