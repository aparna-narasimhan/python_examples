def subsets(nums):
  if nums is None:
      return None
  subsets = [[]]
  next = []
  for n in nums:
    for s in subsets:
      next.append(s + [n])
    subsets += next
    next = []
  return subsets

sets=subsets([1,2,3])
print(sets)
