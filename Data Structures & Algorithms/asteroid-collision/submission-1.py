class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for asteroid in asteroids:
            destroyed = False
            while stk and stk[-1] > 0 and asteroid < 0:
                if abs(asteroid) > stk[-1]:
                    stk.pop()
                elif abs(asteroid) == stk[-1]:
                    stk.pop()
                    destroyed = True
                    break
                else:
                    destroyed = True
                    break
            
            if not destroyed:
                stk.append(asteroid)

        return stk


            