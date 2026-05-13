from graph import graph

problem = """
You are given an integer array nums and an integer k.
Return the maximum sum of any subarray of size k.
"""

initial_state = {
    "problem": problem,
    "topic": "",
    "bruteforce": "",
    "optimized": "",
    "code": "",
    "review": "",
    "explanation": "",
    "needs_fix": False,
}

result = graph.invoke(initial_state)

print("\n========== TOPIC ==========\n")
print(result["topic"])

print("\n========== BRUTE FORCE ==========\n")
print(result["bruteforce"])

print("\n========== OPTIMIZED ==========\n")
print(result["optimized"])

print("\n========== CODE ==========\n")
print(result["code"])

print("\n========== REVIEW ==========\n")
print(result["review"])

print("\n========== EXPLANATION ==========\n")
print(result["explanation"])