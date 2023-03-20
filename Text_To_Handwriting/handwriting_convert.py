import pywhatkit 

text = """Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types, and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming."""

pywhatkit.text_to_handwriting(text,"image.png",[0,0,138])
print("Done!")