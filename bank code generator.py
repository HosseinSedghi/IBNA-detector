import pprint

op = open('data.txt', encoding='utf-8', mode='r').readlines()

print(op)
print(len(op))

output = {}
for i in op:
	m = i.strip().split('\t')

	output[m[1]] = m[0]

pprint.pprint(output)
print(len(output))

ops = open('bank_codes.py', mode='w', encoding='utf-8')
ops.write(output)
ops.close()