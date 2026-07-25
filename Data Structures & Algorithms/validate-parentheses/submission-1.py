class Solution:
    def isValid(self, s: str) -> bool:
        paras = {'(':')','{':'}','[':']'}
        paraMap = []
        for i in s:
            if i in paras:
                paraMap.append(i)
            elif len(paraMap) > 0:
                if paras[paraMap.pop()] != i:
                    return False
            else:
                return False
        return True if len(paraMap) == 0 else False

        