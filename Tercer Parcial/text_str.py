from functools import reduce

new = "Tolerably earnestly middleton extremely distrusts she boy now not. Add and offered prepare how cordial two promise. Greatly who affixed suppose but enquire compact prepare all put. Added forth chief trees but rooms think may. Wicket do manner others seemed enable rather in. Excellent own discovery unfeeling sweetness questions the gentleman. Chapter shyness matters mr parlors if mention thought."
new = new.split()
print(new)

lenghts = map(len, new)
avg = sum(lenghts) / len(new)
print(avg)

stop_words = ['of', 'the', 'to']

s = filter(lambda x: x not in stop_words, new)
count, total = reduce(
    lambda anterior, actual: (anterior[0] + 1, anterior[1] + len(actual)), 
    s,
    (0, 0)
)

print(total / count)

# avg = sum(map(len, filter(lambda x: x not in stop_words, new))) / reduce(
#     lambda suma, elemento: suma + 1, filter(lambda x: x not in stop_words,
#                                             new), 0)
# print(avg)