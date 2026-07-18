class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position,speed))
        cars.sort()

        for i in range(len(cars)-1, -1, -1):
            pos, spd = cars[i]
            time = (target-pos)/spd

            # sorted by position and traversing reverse,
            # if curr time is more than the car ahead of it,
            # it will definitely form another fleet, hence append
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)



