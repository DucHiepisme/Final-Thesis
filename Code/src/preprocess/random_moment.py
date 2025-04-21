import random

ids = [
    "2bHsPtENhWc",
    "a5_Eqony5RE",
    "BGNUEdyqqy0",
    "dAe0nCZTeao",
    "e1C8F5ewNa8",
    "fj0bvGuQOeA",
    "iCkpNqqJarU",
    "KL_J5Me17LU",
    "MpjqiVweVeM",
    "PQrekQOY-VY",
    "rO7z-Ddl-Yo",
    "RoC4vek5qqc",
    "RR7VricHGAM",
    "rSE2YPcv89U",
    "s3qWsdWfK24",
    "SyVB5ha6PDs",
    "wfRlplcJfXU",
    "WjS-en1B8DE",
    "WkEvdVImkec",
    "WZ9WQURYBTY",
    "Y6psISQAGuY",
    "ZdutvdsIOAk",
    "zUTUA0TKvfQ"
]

def generate_random_interval():
    start_seconds = random.randint(0, 5400)  # Up to almost 1.5 hour
    end_seconds = start_seconds + 10

    start_minutes = start_seconds // 60
    start_seconds %= 60
    end_minutes = end_seconds // 60
    end_seconds %= 60

    start_time = f"{start_minutes:02}:{start_seconds:02}"
    end_time = f"{end_minutes:02}:{end_seconds:02}"
    return start_time, end_time

results = []
for _ in range(50):
    video_id = random.choice(ids)
    start_time, end_time = generate_random_interval()
    results.append((video_id, start_time, end_time))

for result in results:
    print(f'["{result[0]}", "{result[1]}", "{result[2]}"],')