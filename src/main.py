def main():
    print("Diseased Cell Translator starting...")

from cells import count, disease_percentage
print("testing functions...")

#-------------------------------------------
# Test 1: Simple list of strings
#-------------------------------------------
simple_matrix = ["healthy", "diseased", "healthy", "diseased",
                    "healthy", "diseased", "healthy", "diseased"]

print("Simple dataset:", simple_matrix)
print("Healthy count:", count(simple_matrix , "healthy"))
print("Diseased count:", count(simple_matrix, "diseased"))
print("Disease percentage:", disease_percentage(simple_matrix))
print("\n")

#-------------------------------------------
# Test 2: Real dataset with dictionaries
#-------------------------------------------
real_matrix = [
   {"geneA": 3.2, "geneB": 0.1, "state": "healthy"},
        {"geneA": 7.8, "geneB": 2.3, "state": "diseased"},
        {"geneA": 1.1, "geneB": 0.5, "state": "healthy"},
        {"geneA": 9.4, "geneB": 3.1, "state": "diseased"},
        {"geneA": 2.5, "geneB": 0.2, "state": "healthy"},
        {"geneA": 8.7, "geneB": 4.0, "state": "diseased"},
        {"geneA": 0.9, "geneB": 0.3, "state": "healthy"},
        {"geneA": 6.5, "geneB": 1.8, "state": "diseased"}
]

print("Realistic dataset (list of dicts): ")
for row in real_matrix:
    print(row)

print("\nHealthy count:", count(real_matrix, "healthy"))
print("Diseased count:", count(real_matrix, "diseased"))
print("Disease percentage:", disease_percentage(real_matrix))

if __name__ == "__main__":
        main()