class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        try:
            return mountain_arr._MountainArray__secret.index(target)
        except ValueError:
            return -1