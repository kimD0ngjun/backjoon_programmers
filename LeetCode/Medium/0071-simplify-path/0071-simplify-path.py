"""
3개 이상의 점: 경로 혹은 파일명으로 처리
2개 이상의 /: 1개로만 취

일단 / 기준으로 스플릿
"""

class Solution:
    def __init__(self):
        self.stack = []

    def simplifyPath(self, path: str) -> str:
        routes = path.split('/')

        for route in routes:
            self.manipulate(route)

        return "/" + "/".join(self.stack)

    def manipulate(self, route: str) -> None:
        if route == "" or route == ".":
            return
        elif route == "..":
            if self.stack:
                self.stack.pop()
        else:
            self.stack.append(route)