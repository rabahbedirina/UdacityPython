scores=['A','B','C','D','E','F','G']
grades=scores
print('grades', ''.join(grades).lower())


print('scores', scores)
print('grades', grades)
print('max', max(scores) )
print('sort' , sorted(grades , reverse=1) , 'len' , len(grades))
print(scores[0:2] == scores[:3] , scores[0:2] , scores[:3])
