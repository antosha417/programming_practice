def sort(dictionary):
    keys = list(dictionary.keys())
    dictionary_final = {}
    keys.sort()
    for key in keys:
        dictionary_final[key] = dictionary[key]
    return dictionary_final


n = int(input())
summary = {}
for i in range(n):
    customer, item, amount = input().split()
    if summary.get(customer) is None:
        summary[customer] = {}
    if summary[customer].get(item) is not None:
        summary[customer][item] += int(amount)
    else:
        summary[customer][item] = int(amount)
customers = list(summary.keys())
for customer in customers:
    print(customer)
    print(sort(summary[customer]))