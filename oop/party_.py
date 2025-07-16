class Party:
    def __init__(self):
        self.people = []


party = Party()

while (name := input()) != 'End':
    party.people.append(name)


print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")