class solv:
    def trap(self, a):
        water_occupied = 0
        for height in range(1,max(a)+1):
            stone = []
            full_length = []
            for ind in range(len(a)):
                if a[ind] >= height:
                    stone.append(ind)
            for length in range(min(stone),max(stone)+1):
                full_length.append(length)
            water_occupied += len(set(full_length)-set(stone))
        return water_occupied
a = [0,1,2,2,3,0,4]
sol = solv()
print(sol.trap(a))
