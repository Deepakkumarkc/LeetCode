
nums = [8,4,2,8,4]
res = []
for Display in nums:
    print ("lists: ", Display)
    Mup = Display * 2
    if Mup in nums:
        if nums.count(Mup) == 2 and Mup not in res:
            res.append(Mup)
            print ("Result:", res)
            print ("Result:", len(res))

