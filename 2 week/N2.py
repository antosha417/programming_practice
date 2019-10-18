"""
input: str = text = MIPT Students, n = 5. Output: Hello, MIPT Students, MIPT Students, MIPT Students, MIPT Students, MIPT Students
"""

text = input()
n = int(input())

print("Hello", end = 'qw5')
for i in range(n):
    print(', ', text, end = '')