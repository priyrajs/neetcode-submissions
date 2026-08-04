class Solution:
    def countSeniors(self, details: List[str]) -> int:
        op = 0
        for i in details:
            # gender = 'M' if 'M' in i else 'F' if 'F' in i else 'O'
            # age = i.split(gender)[1][:2]
            age = i[11]+i[12]
            if int(age) > 60:
                op += 1
        return op
