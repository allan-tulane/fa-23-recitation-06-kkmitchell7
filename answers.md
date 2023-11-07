# CMPS 2200 Recitation 06
## Answers

**Name:**Kailen Mitchell
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**

W(n) = W(n-1) + W(n-2) + 1
W(n) = 2^n

- **3)**

S(n) = S(n/2) + n
S(n) = n

- **4)**

The counts array is the fibonacci sequence itself

- **6)**


The maximum number of times that fib_top_down(i) will be called is i times because we only need to find each fib number once
The span is also n since we keep an array of size n+1

W(n) = O(n)
S(n) = O(n)

- **8)**

The maximum number of times that $F_i$ will be read for any value i is i times because we only need to find each fib number once as well
The span is 1 since we only use two varibles to keep track of intermediate results

W(n) = O(n)
S(n) = O(1)
