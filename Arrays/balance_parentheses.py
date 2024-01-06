from collections import deque
"""
For a given number N, write a function to generate all combination of N pairs of balanced parentheses.

Example 1:

Input: N=2
Output: (()), ()()
Example 2:

Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
"""


class ParenthesesString:

    def __init__(self, word: str, openCount: int, closeCount: int) -> None:
        self.word = word
        self.openCount = openCount
        self.closeCount = closeCount


def solve(num: int) -> list[str]:
    """
    To solve this: Breadth First Search (BFS)
    Let's take Example-2 mentioned above to generate all the combinations of balanced parentheses.
    Following a BFS approach, we will keep adding open parentheses ( or close parentheses ). 
    At each step we need to keep two things in mind:

    We can't add more than N open parenthesis.
    To keep the parentheses balanced, we can add a close parenthesis ) only when we have 
    already added enough open parenthesis (. For this, we can keep a count of open and close
    parenthesis with every combination.

    Following this guideline, let's generate parentheses for N=3:
    Start with an empty combination: “”
    At every step, let's take all combinations of the previous step and add ( or ) 
    keeping the above-mentioned two rules in mind.
    For the empty combination, we can add ( since the count of open parenthesis will be less than 
    N. We can't add ) as we don't have an equivalent open parenthesis, so our list of combinations will now be: “(”
    For the next iteration, let's take all combinations of the previous set. For “(” we can add another ( to it since 
    the count of open parenthesis will be less than N. We can also add ) as we do have an equivalent open parenthesis,
    so our list of combinations will be: “((”, “()”
    In the next iteration, for the first combination “((”, we can add another ( to it as the count of open parenthesis 
    will be less than N, we can also add ) as we do have an equivalent open parenthesis. 
    This gives us two new combinations: “(((” and “(()”. For the second combination “()”, we can add another ( to it 
    since the count of open parenthesis will be less than N. We can't add ) as we don't have an equivalent open 
    parenthesis, so our list of combinations will be: “(((”, “(()”, ()("
    Following the same approach, next we will get the following list of combinations: “((()”, “(()(”, “(())”, “()((”, “()()”
    Next we will get: “((())”, “(()()”, “(())(”, “()(()”, “()()(”
    Finally, we will have the following combinations of balanced parentheses: “((()))”, “(()())”, “(())()”, “()(())”, “()()()”
    We can't add more parentheses to any of the combinations, so we stop here.
    """
    ans: list[str] = []
    queue: deque[ParenthesesString] = deque()
    queue.append(ParenthesesString("", 0, 0))
    while queue:
        ps = queue.popleft()
        # when reached max of open and close parentheses, add to result
        if ps.openCount == num and ps.closeCount == num:
            ans.append(ps.word)
        else:
            if ps.openCount < num:
                # we can add open parentheses
                queue.append(ParenthesesString(
                    ps.word + "(", ps.openCount + 1, ps.closeCount
                ))

            if ps.openCount > ps.closeCount:
                # we can add close parentheses
                queue.append(ParenthesesString(
                    ps.word + ")", ps.openCount, ps.closeCount + 1
                ))

    print("Answer is: ", ans)
    return ans


assert solve(2) == ['(())', '()()']
assert solve(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']


"""
Time complexity: O()
Space complexity: S()
"""
