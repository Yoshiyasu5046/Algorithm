# Reverse function takes one stirng input and outputs reversed string


def reverse(text):
    if type(text) is not str:
        text = str(text)
    i = len(text) - 1
    output = []
    while i >= 0:
        output.append(text[i])
        i -= 1
    return "".join(output)
            
print reverse("hello")