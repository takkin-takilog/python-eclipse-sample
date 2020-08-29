
d = {}

print("--- 辞書の中身 ---")
print(d)
print("--- 辞書の要素数 ---")
print(len(d))

print("--- 辞書へ追加(A) ---")
d["one"] = "A"
print(d)
print("--- 辞書の要素数 ---")
print(len(d))

print("--- 辞書へ追加(B) ---")
d["two"] = "B"
print(d)
print("--- 辞書の要素数 ---")
print(len(d))

print("--- 辞書へ追加(C) ---")
d["tree"] = "C"
print(d)
print("--- 辞書の要素数 ---")
print(len(d))

print("--- 全要素表示 ---")
for i in d:
    print("key = {}, value = {}" .format(i, d[i]))

print("--- 要素の削除(B) ---")
del d["two"]
print(d)
print("--- 辞書の要素数 ---")
print(len(d))
