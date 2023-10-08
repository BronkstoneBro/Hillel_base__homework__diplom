class String(str):
    def __add__(self, other):
        return String(super().__add__(str(other)))

    def __sub__(self, other):
        return String(self.replace(str(other), '', 1))


print(String('New') + String(890))    # 'New890'
print(String(1234) + 5678)            # '12345678'
print(String('New') + 'castle')       # 'Newcastle'
print(String('New') + 77)             # 'New77'
print(String('New') + True)           # 'NewTrue'
print(String('New') + ['s', ' ', 23])  # "New['s', ' ', 23]"
print(String('New') + None)           # 'NewNone'

print(String('New bala7nce') - 7)               # 'New balance'
print(String('New balance') - 'bal')            # 'New ance'
print(String('New balance') - 'Bal')            # 'New balance'
print(String('pineapple apple pine') - 'apple')   # 'pine apple pine'
print(String('New balance') - 'apple')          # 'New balance'
print(String('NoneType') - None)                # 'Type'
print(String(55678345672) - 7)                  # '5568345672'
