# Initial Print
print("Enter the following quantities in feet.")
# User Input Values
rowLength = int(input("    How long is this row? "))
endPostSize = int(input("    How wide is teh end-post assembly? "))
spaceBetweenVines = int(input("    How much space should be between the vines? "))

# Calculate number of Grapevines to the nearest integer
# V = (R - 2 * E)/S
grapevineCount = int((rowLength - 2 * endPostSize)/spaceBetweenVines)
# Print result script while changing grapevineCount from int to string
print("\nThis row has enough space for " + str(grapevineCount) + " vine(s)")
# End
