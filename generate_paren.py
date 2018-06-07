# Time complexity O(4^n / √n)
# Space complexity O(n)


def generate_paren(n):
    arr = []

    def backtrack(s='', left=0, right=0):
        if len(s) is 2 * n:
            arr.append(s)
            return

        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    backtrack()
    return arr
