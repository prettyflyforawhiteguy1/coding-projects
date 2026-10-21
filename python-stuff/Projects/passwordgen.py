import secrets
import string
import time

def generate_password(length, lower_set, upper_set, digits_set, special_set, all_chars_list):
    choose_char = secrets.choice
    
    while True:
        password = ''.join(choose_char(all_chars_list) for _ in range(length))
        p_set = set(password)
        
        criteria_met = (
            (not p_set.isdisjoint(lower_set)) +
            (not p_set.isdisjoint(upper_set)) +
            (not p_set.isdisjoint(digits_set)) +
            (not p_set.isdisjoint(special_set))
        )
        if criteria_met >= 3:
            return password

def export_passwords(filename, count, log_interval=1000):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "~!@#$%^&*-="
    all_chars_list = list(lower + upper + digits + special)
    
    l_set = set(lower)
    u_set = set(upper)
    d_set = set(digits)
    s_set = set(special)
    
    passwords = []
    lengths = [6, 7, 8]
    
    print(f"[*] Starting high-speed generation of {count:,} passwords...")
    start_time = time.time()
    
    for i in range(count):
        length = lengths[i % 3]
        passwords.append(generate_password(length, l_set, u_set, d_set, s_set, all_chars_list))

        if log_interval and (i + 1) % log_interval == 0:
            elapsed = time.time() - start_time
            print(f"[>] Generated {i + 1:,} / {count:,} passwords... (Elapsed: {elapsed:.2f}s)")
            
    # Production Improvement: explicitly enforce UTF-8 encoding for safety with symbols
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(passwords))
        
    total_time = time.time() - start_time
    print(f"\n[SUCCESS] Successfully saved {count:,} passwords to '{filename}' in {total_time:.2f} seconds!")

if __name__ == "__main__":
    export_passwords("fast_passwords.txt", count=int(input("Enter the number of passwords to generate: ")), log_interval=5000)