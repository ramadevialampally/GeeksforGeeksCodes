// Function to calculate factorial of a number.
int factorial(int n) {
    // code here
    int fact,i;
    fact=1;
    for(i=1;i<=n;i++){
        fact=fact*i;
    }
    return fact;
}
