# is not 은 객체 비교, != 는 값 비교
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def find(a, is_left):
            if a == None: return True
            
            ans = 0
            l = find(a.left, True)
            r = find(a.right, False)
            if l is not True: ans += l
            if r is not True: ans += r

            # 누군가의 왼쪽 자식인데 자식이 없어.
            if is_left and l is True and r is True:
                return a.val
            
            return ans

        return find(root, False)