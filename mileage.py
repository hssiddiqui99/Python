print("How many kilometers did you run today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles,2)
print(f"Your {kms}km ride is equal to {miles}mi ")

exhausted = input()
print("How exhausted were you on a scale of 1-10?")
scale = int(exhausted)
print(f"You stated a exhaustion level of {scale}.")