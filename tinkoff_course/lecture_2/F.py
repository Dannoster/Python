n = int(input())
hours = n % (24*60*60) // (60*60)
minutes = n % (60*60) // 60
seconds = n % 60
print(f"{hours}:{minutes:02}:{seconds:02}")