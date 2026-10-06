def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError('Пустой список')
    maxx=nums[0]
    minn=nums[0]
    for num in nums:
        if num <minn:
            minn=num
        if num >maxx:
            maxx=num
    return minn,maxx

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    for num in nums:
        if not isinstance(num,(int,float)):
            raise TypeError('Все элементы списка должны быть числами')
    uniq=list(set(nums))
    for i in range(len(uniq)):
        for x in range(i+1,len(uniq)):
            if uniq[i]<uniq[x]:
                uniq[i],uniq[x]=uniq[x],uniq[i]
    return uniq
    
def flatten(mat: list[list | tuple]) -> list:
    flat=[]
    for row in mat:
        if not isinstance(row,(list,tuple)):
            raise TypeError('Все элементы должны быть списками или кортежами')
        flat.extend(row)
    return flat
