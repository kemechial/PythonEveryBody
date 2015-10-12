test_word="Hello Jack"
test_replace=test_word.replace("Jack","Bob")
print test_word
print test_replace
test_space="   some space at the beginning, some at the end    "
test_l=test_space.lstrip()
print test_l, "--check"
test_r=test_space.rstrip()
print test_r, "--check"
test_both=test_space.strip()
print test_both, "--check"
