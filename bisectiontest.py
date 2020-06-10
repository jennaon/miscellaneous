'''
Wanted to prove that methods using simple match could sometimes replace efficient
search algorithms such as binary search.

Conclusion: Bisection pacakge > numpy > home cooked bisection

Numpy-based math works faster than home-cooked bisection method.
Home-cooked bisection can't handle large data
Bisection package bisect is incredibly fast, and doesn't run out of memory even
with large dataset.

'''
import numpy as np
import bisect
import time


class Test():
    def __init__(self,N):
        #generate a massive sorted matrix
        self.N = N
        self.M = np.array(range(self.N)).reshape(-1,1) #(M,1)

        self.target = np.random.randint(0,self.N) + 0.5

    def bisection(self,low,high):
        '''
        simple bisection implementation. should converge in O(logN).
        '''
        mid = int((low+high)/2)
        if self.M[mid] < self.target:
            if self.M[mid+1]>=self.target:
                print('%d is good'%mid)
                return mid
            else:
                self.bisection(low,mid)
        if self.target > self.M[mid]:
            self.bisection(mid,high)

    def usemath(self,):
        res = np.ones((self.N,1))*self.target - self.M
        res = np.where(res>0,res,float('inf'))
        ind = np.argmin(res)

        return ind



def main():

    N = int(1e3)
    print('Testing with %d samples '%N)
    t1 = Test(N)

    start = time.time()
    t1.usemath()
    end = time.time()
    print("Numpy: %.6fs"%(end-start))

    start = time.time()
    t1.bisection(0,N)
    end = time.time()
    print("Bisection (home implementation): %.6fs"%(end-start))

    # print('Testing with Bisection package...')
    start = time.time()
    bisect.bisect(t1.M,0,N)
    end = time.time()
    print("Bisection package: %.6fs"%(end-start))

    N = int(1e8)
    print('Testing with %d samples '%N)
    t2 = Test(N)


    start = time.time()
    t2.usemath()
    end = time.time()
    print("Numpy: %.4fs"%(end-start))

    '''bisection on large data will cause an error'''
    # start = time.time()
    # t2.bisection(0,N)
    # end = time.time()
    # print("Bisection (home implementation): %.6fs"%(end-start))

    start = time.time()
    bisect.bisect(t2.M,0,N)
    end = time.time()
    print("Bisection package: %.6fs"%(end-start))




if __name__=="__main__":
    main()
