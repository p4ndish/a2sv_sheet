class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imaginary1 = num1.split("+")
        real2, imaginary2 = num2.split("+")
        # Remove the "i" from the imaginary parts
        imaginary1 = imaginary1[:-1]
        imaginary2 = imaginary2[:-1]
        # Convert the parts to integers
        real1, imaginary1, real2, imaginary2 = int(real1), int(imaginary1), int(real2), int(imaginary2)
        # Calculate the real and imaginary parts of the result
        real_result = real1 * real2 - imaginary1 * imaginary2 
        imaginary_result = real1 * imaginary2 + real2 * imaginary1
        # Return the result as a string
        return str(real_result) + "+" + str(imaginary_result) + "i"
    #str(x1*x2-y1*y2) + "+" + str(x1*y2+x2*y1)+"i"
