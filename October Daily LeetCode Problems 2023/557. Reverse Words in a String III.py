class Solution:
    def reverseWords(self, s):

        s = s.strip()

        List = []
        a = ""
        for i in s:
            if i == " ":
                List.append(a)
                a = ""
            else:
                a+=i
        List.append(a)
        ans = ""
        for i in List:
            rev = i[::-1]
            ans+=rev+" "
        return ans.strip()