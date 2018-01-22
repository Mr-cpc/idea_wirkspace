def repdna(s:str):
    return [s[i:i+10] for i in range(len(s)-9) if s[i:i+10] in s[i+10:]]

print(repdna("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))