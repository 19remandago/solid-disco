import random

options = ['rock', 'paper', 'scissors']
player = input("Choose rock, paper, or scissors: ").lower()
cpu = random.choice(options)

print(f"🧠 CPU chose: {cpu}")
if player == cpu:
    print("🤝 It's a tie!")
elif (player == 'rock' and cpu == 'scissors') or \
     (player == 'paper' and cpu == 'rock') or \
     (player == 'scissors' and cpu == 'paper'):
    print("✅ You win!")
else:
    print("❌ You lose!")
