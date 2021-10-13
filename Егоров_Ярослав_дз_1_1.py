seconds = int(input("duration = "))

days = seconds // 86400
seconds -= days * 86400
hours = seconds // 3600
seconds -= hours * 3600
minutes = seconds // 60
seconds -= minutes * 60

if days > 0:
    print(f"{days} дн ", end="")

if hours > 0:
    print(f"{hours} час ", end="")

if minutes > 0:
    print(f"{minutes} мин ", end="")

if seconds > 0:
    print(f"{seconds} сек")
