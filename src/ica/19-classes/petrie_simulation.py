"""
Extended Petrie Multiplier Simulation (conversation-based model)
Implements Steps 1–5 as described in the assignment.
"""

import random


# -----------------------------
# STEP 1: Comment probability distribution
# -----------------------------
COMMENT_PROBABILITIES = [
    0.0,          # 50% will not make comments
    0.20, 0.40, 0.60, 0.80, 1.00  # each 10%
]
COMMENT_WEIGHTS = [0.5, 0.1, 0.1, 0.1, 0.1, 0.1]   # sums to 1


# -----------------------------
# Employee class
# -----------------------------
class Employee:
    def __init__(self, gender: str, comment_prob: float):
        self.gender = gender              # "Man" or "Woman"
        self.comment_prob = comment_prob  # probability this employee comments
        self.comments_received = 0        # counter

    def __str__(self):
        return (self.gender.rjust(5)
                + f": {self.comments_received} sexist comments received")


# -----------------------------
# Helper printing function
# -----------------------------
def print_employee_list(lst):
    for emp in lst:
        print(emp)
    print()


# -----------------------------
# STEP 2: create employees (80% men, 20% women)
# each with assigned comment probability from distribution
# -----------------------------
def create_employees(total_num):
    employees = []

    for i in range(total_num):
        gender = "Man" if random.random() < 0.8 else "Woman"
        comment_prob = random.choices(COMMENT_PROBABILITIES, COMMENT_WEIGHTS)[0]
        employees.append(Employee(gender, comment_prob))

    return employees


# -----------------------------
# STEP 3: Generate one conversation size
# (distribution: 30% size2, 20% size3, 10% each for 4–8)
# -----------------------------
def random_conversation_size():
    r = random.random()
    if r < 0.30:
        return 2
    elif r < 0.50:
        return 3
    else:
        return random.randint(4, 8)  # 10% each for 4,5,6,7,8 → total 50%


# -----------------------------
# STEP 4 & 5:
# Simulate one conversation:
#   - random subset of employees
#   - sexist remarks only if speaker NOT outnumbered by opposite gender
#   - each speaker attempts 1 possible sexist remark (Bernoulli trial)
# -----------------------------
def simulate_conversation(employees):

    # Pick a random group size
    size = random_conversation_size()
    group = random.sample(employees, size)

    men = [p for p in group if p.gender == "Man"]
    women = [p for p in group if p.gender == "Woman"]

    num_men = len(men)
    num_women = len(women)

    for speaker in group:
        # Speaker decides whether they TRY to make a sexist remark
        if random.random() < speaker.comment_prob:

            # Can only make a sexist remark if not outnumbered
            if speaker.gender == "Man":
                if num_men < num_women:
                    continue  # outnumbered → cannot comment
                target_group = women
            else:
                if num_women < num_men:
                    continue  # outnumbered → cannot comment
                target_group = men

            if target_group:  # target exists
                target = random.choice(target_group)
                target.comments_received += 1


# -----------------------------
# Run many conversations
# -----------------------------
def simulate_many_conversations(employees, num_conversations):
    for _ in range(num_conversations):
        simulate_conversation(employees)


# -----------------------------
# Calculate averages
# -----------------------------
def average_comments(lst):
    men_comments = [p.comments_received for p in lst if p.gender == "Man"]
    women_comments = [p.comments_received for p in lst if p.gender == "Woman"]

    men_avg = sum(men_comments) / len(men_comments)
    women_avg = sum(women_comments) / len(women_comments)

    return men_avg, women_avg


# -----------------------------
# Main simulation
# -----------------------------
def main():
    num_employees = 100
    num_conversations = 5000   # simulation now based on # of conversations

    employees = create_employees(num_employees)
    simulate_many_conversations(employees, num_conversations)

    men_avg, women_avg = average_comments(employees)
    print("Men received on average   ", men_avg, "sexist comments")
    print("Women received on average ", women_avg, "sexist comments")


# ------------
