def main(data):
    rules_part, updates_part = data.strip().split('\n\n')
    rules = [list(map(int, rule.split('|'))) for rule in rules_part.split('\n')]
    updates = [list(map(int, line.split(','))) for line in updates_part.split('\n')]

    # Make a dictionary where the key is the page number and the values are the pages that should appear after the key in the update
    rule_dict = {}
    for rule in rules:
        if rule[0] in rule_dict:
            rule_dict[rule[0]].extend(rule[1:])
        else:
            rule_dict[rule[0]] = rule[1:]
    
    counter = 0
    
    for update in updates:
        if right_order(update, rule_dict):  # Check if update is correct (i.e. in right_order)
            counter += middle_page(update)  # Sum the middle page numbers of correct update lists
    
    return counter

# Check if each page number of the update follows the rules
def right_order(pages, rules_dict):
    for i in range(len(pages) - 1):
        if pages[i+1] not in rules_dict.get(pages[i], []): # Check if current page should be left to the next page
            return False
    return True
    
# Determine the middle page number
def middle_page(pages):
    middle = pages[(len(pages) - 1)//2]
    return middle

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    print(main(content))
