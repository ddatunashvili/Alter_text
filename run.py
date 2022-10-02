
with open(r"_input.txt","r",   encoding="utf-8") as text:
    text = text.read()


with open(r"alter_base.txt", "r", encoding="utf-8") as base:
    change_base = {}
    base = base.read().split("\n")
    for a in    base:
        a = a.split("->")
        try:
            change_base[a[0]] = a[1]
        except Exception as e:
            pass

for key,value in change_base.items():
    text = text.replace(key,value)


with open(r"_output.txt","w",   encoding="utf-8") as out_text:
    out_text.write(text)
