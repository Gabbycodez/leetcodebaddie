def helper(self, n, seen):   
        if n == 1:
            return True
        if n in seen:
            return False

        seen.add(n)


        n = [int(d) for d in str(n)]
        
        total = 0
        for d in n:
            total += d * d
        return self.helper(total, seen)
End