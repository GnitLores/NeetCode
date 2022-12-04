class Solution:
    # It seems faster to split the string and join on the new character.
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))

    # Using default function
    def defangIPaddrLib(self, address: str) -> str:
        return address.replace(".", "[.]")

sol = Solution()
print(sol.defangIPaddr(address = "1.1.1.1"))
print(sol.defangIPaddr(address = "255.100.50.0"))
print("")
print(sol.defangIPaddrLib(address = "1.1.1.1"))
print(sol.defangIPaddrLib(address = "255.100.50.0"))