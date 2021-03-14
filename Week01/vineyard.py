# Initial Print
print("Enter the following quantities in feet.")
# User Input Values
rowLength = float(input("  How long is this row? "))
endPostSize = float(input("  How wide is the end-post assembly? "))
spaceBetweenVines = float(input("  How much space should be between the vines? "))

# Calculate number of Grapevines to the nearest integer
# V = (R - 2 * E)/S
grapevineCount = int((rowLength - 2 * endPostSize)/spaceBetweenVines)
# Print result script while changing grapevineCount from int to string
print("\nThis row has enough space for " + str(grapevineCount) + " vine(s).")
# End
