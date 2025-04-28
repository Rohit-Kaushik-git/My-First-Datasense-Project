import time
import emoji
print(emoji.emojize(":brain: Know Your Personality"))
print(emoji.emojize(":sparkles: Let's discover who you really are with some fun data magic!"))
print("="*80)

name = input("👤 Your Name: ").strip()
age = int(input("🎂 Your Age: "))
city = input("🏙️  City You Live In: ").strip()
food = input("🍕 Your Favourite food: ").strip()
color = input("🎨 Your Favorite Color: ").strip()
animal = input("🐾 Your Spirit Animal: ").strip()
hobby = input("🎮 One Thing You LOVE Doing: ").strip()

time.sleep(1)

print("🔍 Scanning colors, foods, and animal energies...")

time.sleep(2)

print("💫 Calculating your personality type using complex non-scientific logic...")

time.sleep(2)

print(f"🎉 Hey {name}, here's your fun personality report!")

print(f"🌆 You're from {city}, a place of dreams!")
print(f"🍿 You love {food} and enjoy doing {hobby}.")
print(f"🎨 You vibe with the color {color} and your spirit animal is the {animal}.")
print(f"📅 You've lived approximately {age*12} months already.")
if age < 18:
    print(f"🧩 You belong to the {'young explorer'.title()} tribe")
elif age>=18 and age<=30:
    print(f"🧩 You belong to the {'adventurer'.title()} tribe")
else:
    print(f"🧩 You belong to the {'wise owl'.title()} tribe")

print(f"🔐 Your Secret Personality Code is: {name[:2].upper()+str(age%10)+animal[0].upper()+color[0].lower()}")

if len(hobby) <=8:
    print("💡 Time to explore more hobbies? You’ve got hidden sparks waiting!")
else:
    print("✨ You seem deeply passionate — that hobby says a lot about your vibe!")


print("🌈 You are officially certified as: FUNKY AND FABULOUS! 😎")