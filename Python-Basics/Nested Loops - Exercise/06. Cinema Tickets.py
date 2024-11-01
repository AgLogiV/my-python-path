movie_name = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0


while movie_name != "Finish":
    free_seats = int(input())
    current_tickets = 0
    for movie in range(free_seats):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
            current_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            current_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
            current_tickets += 1
        total_tickets += 1
    print(f"{movie_name} - {(current_tickets / free_seats) * 100:.2f}% full.")
    movie_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets / total_tickets * 100:.2f}% kids tickets.")
