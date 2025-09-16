"""Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  "" """
def solution(s):
    ans = ""
    for l in s:
        if l.isupper():
            ans += " " + l
        else:
            ans += l
    return ans
            
        